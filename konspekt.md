# UniBook: system rezerwacji sal i sprzętu na uczelni

**Konspekt** (21.10.2026)

- Autorzy: Marcin Pupek, Paula Brajczewska, Mateusz Perkowski, Mateusz Drewnowski, Mikołaj Malinowski
- Przedmiot: Projekt zespołowy
- Rok akademicki: 2026/27

## Spis treści

1. [Wstęp](#1-wstęp)
   1. [Opis biznesowy](#11-opis-biznesowy)
   2. [Cel pracy](#12-cel-pracy)
   3. [Analiza istniejących rozwiązań](#13-analiza-istniejących-rozwiązań)
   4. [Wymagania funkcjonalne i niefunkcjonalne](#14-wymagania-funkcjonalne-i-niefunkcjonalne)
   5. [FURPS, MoSCoW, SWOT](#15-furps-moscow-swot)

## 1. Wstęp

### 1.1 Opis biznesowy

Na uczelni rezerwacje sal i sprzętu (projektory, laptopy, aparaty, zestawy laboratoryjne) często odbywają się mailowo, na kartkach albo ustnie. Skutkuje to podwójnymi rezerwacjami, brakiem wiedzy o tym, co jest wolne, i brakiem historii, kto i co wypożyczył.

UniBook zbiera to w jednym miejscu. System ma cztery role:

- **student** i **pracownik**: przeglądają zasoby i ich dostępność, składają rezerwacje i zarządzają własnymi,
- **administrator**: zarządza kontami i zasobami, zatwierdza lub odrzuca rezerwacje,
- **obsługa**: wydaje sprzęt i przyjmuje jego zwroty.

### 1.2 Cel pracy

Zaprojektowanie i wykonanie działającego systemu rezerwacji, złożonego z backendu (REST API), aplikacji webowej i aplikacji desktopowej.

Kluczowa cecha: system nie pozwala zarezerwować tego samego zasobu w tym samym terminie. Gwarantuje to ograniczenie w bazie danych, a nie tylko kod aplikacji.

### 1.3 Analiza istniejących rozwiązań

Porównano cztery popularne narzędzia:

| Narzędzie | Rodzaj i koszt | Sale | Sprzęt | Zatwierdzanie rezerwacji | Wydawanie i zwroty sprzętu | Dopasowanie do uczelni |
|---|---|---|---|---|---|---|
| Booked Scheduler | otwarte oprogramowanie, własny hosting, darmowe | tak | tak | tak | nie | duże, ale wymaga instalacji i konfiguracji |
| Skedda | usługa w chmurze, płatna | tak | ograniczone | tak | nie | średnie, nastawiona na biura i przestrzenie |
| Microsoft 365 / Outlook | część pakietu Microsoft, licencja | tak (sale w kalendarzu) | słabo | częściowo (delegaci) | nie | średnie, to kalendarz, nie system zasobów |
| Calendly / Microsoft Bookings | usługa w chmurze, płatna lub częściowo darmowa | nie | nie | nie | nie | małe, służy do umawiania spotkań z osobami |

Wniosek: gotowe narzędzia są albo płatne, albo ogólne (kalendarz zamiast zasobów), albo trudne do dopasowania do procesu uczelni (zatwierdzanie przez administratora, wydawanie i zwroty sprzętu, role). Żadne z nich nie prowadzi historii wydań sprzętu. Dlatego powstaje własne, prostsze rozwiązanie dopasowane do uczelni.

### 1.4 Wymagania funkcjonalne i niefunkcjonalne

**Funkcjonalne, czyli co system potrafi:**

- **Konta i role:** rejestracja i logowanie, cztery role (student, pracownik, administrator, obsługa), zarządzanie kontami przez administratora, blokada kont.
- **Zasoby:** dodawanie i edycja sal i sprzętu, dezaktywacja zamiast usuwania, przeglądanie i filtrowanie (typ, budynek, pojemność, wyposażenie), kalendarz dostępności.
- **Rezerwacje:** składanie rezerwacji bez kolizji terminów, edycja i anulowanie własnych rezerwacji przed rozpoczęciem, historia ze statusami, zatwierdzanie i odrzucanie z uzasadnieniem przez administratora.
- **Wydania i zwroty:** wydanie konkretnego egzemplarza sprzętu, przyjęcie zwrotu, historia wydań.

**Niefunkcjonalne, czyli jaki system ma być:**

- **Bezpieczeństwo:** uprawnienia sprawdzane po stronie serwera, a nie tylko w aplikacji.
- **Spójność danych:** nakładające się rezerwacje blokuje baza danych.
- **Otwartość:** API opisane w standardzie OpenAPI (specyfikacja zamrożona do 18.11).
- **Jakość:** testy automatyczne, w tym kolizji rezerwacji i uprawnień.
- **Łatwe uruchomienie:** całe środowisko startuje przez Docker Compose, instrukcja w README.
- **Czas:** wszystkie terminy przechowywane w UTC.

**Architektura i technologie:** dwa klienty (webowy i desktopowy) komunikują się przez REST API (JSON) z backendem, a ten z bazą danych. Całość uruchamia się w kontenerach Docker.

| Warstwa | Technologia | Dlaczego |
|---|---|---|
| Backend | Python, Django i Django REST Framework | gotowe konta, uprawnienia i **panel administratora**, mało kodu do wersji minimalnej |
| Baza danych | PostgreSQL | pozwala zablokować nakładające się rezerwacje na poziomie bazy |
| Środowisko | Docker Compose | cały system startuje jedną komendą |
| Klient webowy | do ustalenia | korzysta z tego samego API |
| Klient desktopowy | JavaFX lub PyQt (decyzja do 04.11) | korzysta z tego samego API |

Główne dane w systemie: użytkownicy, zasoby (sale i sprzęt), rezerwacje oraz wydania i zwroty.

### 1.5 FURPS, MoSCoW, SWOT

**Jakość systemu (FURPS)**

| Kategoria | Co oznacza w UniBook |
|---|---|
| Funkcjonalność | rezerwacje, zatwierdzanie, wydania i zwroty, role |
| Użyteczność | prosty widok dostępności, filtry zasobów |
| Niezawodność | brak kolizji terminów dzięki ograniczeniu w bazie |
| Wydajność | szybkie wyszukiwanie i kalendarz dostępności |
| Utrzymanie i wsparcie | dokumentacja API, testy, uruchomienie jedną komendą |

**Priorytety (MoSCoW)**

| Priorytet | Zakres |
|---|---|
| Musi być | logowanie, role, zasoby, rezerwacje bez kolizji, zatwierdzanie, wydania i zwroty |
| Powinno być | historia rezerwacji, filtrowanie, kalendarz dostępności |
| Nie teraz | potwierdzanie adresów e-mail przy rejestracji |

**Analiza SWOT**

| | |
|---|---|
| Mocne strony | dopasowanie do procesu uczelni, ochrona przed kolizjami w bazie, jedno API dla dwóch aplikacji |
| Słabe strony | mały zespół i krótki czas, dwie aplikacje klienckie, brak potwierdzania e-mail |
| Szanse | powiadomienia, integracja z planem zajęć, rozwój po semestrze |
| Zagrożenia | terminy, konkurencja gotowych narzędzi |
