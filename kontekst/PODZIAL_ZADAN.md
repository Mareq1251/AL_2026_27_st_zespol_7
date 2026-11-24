# UniBook — podział zadań zespołu

Stan na 24 listopada 2026.

Dokument przedstawia wykonane prace oraz zadania pozostałe do realizacji. Zadania oznaczone jako planowane nie są jeszcze potwierdzeniem wykonania danego modułu.

## Wykonane prace

- **Cały zespół:** wspólne opracowanie konspektu, wymagań i ogólnej koncepcji systemu.
- **Marcin Pupek:** diagramy i model danych, konfiguracja Docker, PostgreSQL i Django, logowanie, katalog zasobów, formularz rezerwacji, lista własnych rezerwacji, ochrona przed kolizjami, wykonane testy, aktualizacja README i dokumentacji oraz przesłanie zmian do repozytorium.
- Sprawdzono zapis rezerwacji, odrzucanie kolidujących terminów, terminy sąsiadujące oraz rezerwowanie różnych zasobów w tym samym czasie.
- Wykonano test dwóch równoczesnych zapisów. Po wykryciu zakleszczenia dodano ponawianie transakcji do skryptu testowego. Uzupełnienie tej obsługi w aplikacji pozostaje zadaniem do wykonania.

## Materiały projektowe

| Materiał | Plik | Dysk Google |
|---|---|---|
| Opis projektu, aktualny stan i wymagania | [Opis całego projektu](./00_UNIBOOK_KONTEKST_I_WYMAGANIA.txt) | Do uzupełnienia |
| Paula Brajczewska — aplikacja webowa i decyzje administratora | [Opis modułu i wymagania](./01_PAULA_WEB.txt) | Do uzupełnienia |
| Mateusz Perkowski — wydania, zwroty i historia operacji | [Opis modułu i wymagania](./02_MATEUSZ_PERKOWSKI_WYPOZYCZENIA.txt) | Do uzupełnienia |
| Mateusz Drewnowski — API, uwierzytelnianie i kontrola dostępu | [Opis modułu i wymagania](./03_MATEUSZ_DREWNOWSKI_API.txt) | Do uzupełnienia |
| Mikołaj Malinowski — aplikacja desktopowa PyQt | [Opis modułu i wymagania](./04_MIKOLAJ_DESKTOP.txt) | Do uzupełnienia |

[Repozytorium projektu](https://github.com/Mareq1251/AL_2026_27_st_zespol_7)

Materiały zawierają opis systemu, wymagania, dotychczasowy stan prac oraz szczegółowy zakres poszczególnych modułów. Diagramy są dostępne w konspekcie projektu.

Po umieszczeniu dokumentów na Dysku Google należy uzupełnić ostatnią kolumnę tabeli odnośnikami i udostępnić pliki członkom zespołu.

## Zasady realizacji

- Obecna aplikacja webowa działa na widokach i szablonach Django.
- API i aplikacja desktopowa stanowią rozbudowę istniejącego projektu.
- Reguły rezerwowania, wydawania i zwracania sprzętu powinny być wspólne dla wszystkich interfejsów.
- Każda osoba odpowiada za kod, testy i dokumentację własnego modułu.
- Zmiany wspólnych modeli i migracji należy uzgadniać przed rozpoczęciem równoległej edycji.
- Nie należy nadpisywać istniejącej migracji `0002` ani usuwać danych w celu uproszczenia integracji.
- Hasła, tokeny i zawartość `.env` nie mogą trafiać do repozytorium.
- Status `Gotowe` wymaga działającego kodu, testów, dokumentacji oraz sprawdzenia integracji.
- Ekran działający wyłącznie na danych przykładowych nie oznacza ukończenia integracji.

### Statusy zadań

- **Do zrobienia**
- **W trakcie**
- **Do sprawdzenia**
- **Gotowe**
- **Zablokowane**

## Zestawienie odpowiedzialności

| Osoba | Główny zakres | Najważniejsze zależności |
|---|---|---|
| Paula Brajczewska | Aplikacja webowa, decyzje administratora, edycja i anulowanie rezerwacji, poprawki zapisu | Role i API, historia oraz wypożyczenia |
| Mateusz Perkowski | Modele i logika wydań, zwrotów i historii | Model zasobów, decyzje i uprawnienia |
| Mateusz Drewnowski | Kontrakt API, uwierzytelnianie, role i endpointy | Wspólna logika webu i wypożyczeń |
| Mikołaj Malinowski | Aplikacja desktopowa PyQt | Kontrakt i działające API |

## Paula Brajczewska — aplikacja webowa i decyzje administratora

**Stan początkowy:** Do zrobienia.

**Proponowana gałąź:** `feature/web-decyzje`

### Pliki startowe

- `katalog/models.py`
- `katalog/forms.py`
- `katalog/views.py`
- `katalog/admin.py`
- `config/urls.py`
- `config/settings.py`
- `katalog/templates/`
- `katalog/migrations/`
- `requirements.txt`

### Zadania

- [ ] **PAU-01 — Przegląd obecnej aplikacji.** Uruchomić projekt i sprawdzić logowanie, katalog, formularz rezerwacji oraz własne zgłoszenia. Zachować działające funkcje i dotychczasowe adresy.

- [ ] **PAU-02 — Wygląd i nawigacja.** Przygotować wspólny szablon, czytelne formularze, komunikaty i menu. Zapewnić dostęp do katalogu, własnych rezerwacji, logowania i wylogowania. Funkcje administratora wyświetlać zgodnie z uprawnieniami. Poprawić błędne polskie znaki i sprawdzić obsługę klawiatury.

- [ ] **PAU-03 — Katalog i dostępność.** Dodać filtrowanie według typu, lokalizacji i parametrów dostępnych w modelu. Umożliwić sprawdzenie dostępności w podanym terminie. Zachować kontrolę kolizji podczas właściwego zapisu.

- [ ] **PAU-04 — Rejestracja i konta.** Uzupełnić brakującą rejestrację zwykłego użytkownika, walidację danych i wylogowanie. Uzgodnić wspólny mechanizm ról z Mateuszem Drewnowskim. Użytkownik nie może sam nadać sobie roli administratora, pracownika ani obsługi. Zarządzanie kontami i zasobami może wykorzystywać Django admin po sprawdzeniu wymaganych uprawnień.

- [ ] **PAU-05 — Decyzje administratora.** Przygotować listę oczekujących rezerwacji, szczegóły zgłoszenia oraz zatwierdzanie i odrzucanie. Odrzucenie wymaga uzasadnienia. Zapisywać osobę i datę decyzji po stronie serwera. Operacje zmieniające dane wykonywać przez POST z ochroną CSRF. Sprawdzać aktualny status w transakcji i obsłużyć ponowienie tej samej decyzji.

- [ ] **PAU-06 — Edycja i anulowanie.** Umożliwić właścicielowi edycję i anulowanie przyszłych rezerwacji w dozwolonych stanach. Zmiana terminu lub zasobu zatwierdzonej rezerwacji wymaga ponownego zatwierdzenia. Nieudana edycja musi pozostawić wcześniejsze dane bez zmian. Uzgodnić blokowanie zmian po wydaniu sprzętu.

- [ ] **PAU-07 — Własne rezerwacje i historia.** Rozszerzyć listę o szczegóły decyzji, uzasadnienia i dostępne akcje. Historię pobierać ze wspólnego modułu. Sprawdzać własność danych zarówno na listach, jak i w szczegółach.

- [ ] **PAU-08 — Obsługa błędów zapisu.** Zachować ograniczenie `rezerwacja_bez_kolizji`. Uzupełnić obsługę zakleszczenia `40P01` we współpracy z API. Ponowienia muszą być ograniczone i obejmować całą transakcję po jej wycofaniu. Nie traktować każdego błędu bazy jako kolizji i nie tworzyć podwójnych wpisów historii.

- [ ] **PAU-09 — Testy.** Sprawdzić poprawny zapis, błędne i przeszłe daty, nieaktywny zasób, kolizję, terminy sąsiadujące, cudzą rezerwację, decyzję wykonaną przez studenta, brak uzasadnienia, zwolnienie terminu po odrzuceniu oraz zachowanie danych po nieudanej edycji. Testy równoczesnych zapisów wykonać na PostgreSQL.

- [ ] **PAU-10 — Dokumentacja i przekazanie modułu.** Opisać ekrany, reguły, konfigurację kont i sposób uruchomienia testów. Przekazać wspólną logikę rezerwacji i decyzji do wykorzystania przez API.

### Kryteria odbioru

- Student korzysta wyłącznie z własnych rezerwacji.
- Administrator zatwierdza i odrzuca zgłoszenia.
- Odrzucenie wymaga uzasadnienia i zwalnia termin.
- Edycja nie omija blokady kolizji.
- Błędy zapisu są obsługiwane bez utraty wcześniejszych danych.
- Istnieją testy i opis modułu.

**Współpraca:** pola decyzji i role uzgodnić z Mateuszem Drewnowskim. Historię i blokowanie zmian po wydaniu uzgodnić z Mateuszem Perkowskim.

Materiały uzupełniające: [Opis modułu i wymagania](./01_PAULA_WEB.txt).

## Mateusz Perkowski — wydania, zwroty i historia operacji

**Stan początkowy:** Do zrobienia.

**Proponowana gałąź:** `feature/wypozyczenia-historia`

### Pliki startowe

- `katalog/models.py`
- `katalog/migrations/`
- `config/settings.py`
- aktualne widoki i logika rezerwacji
- konfiguracja użytkowników i uprawnień
- diagram bazy danych z konspektu

### Zadania

- [ ] **MP-01 — Analiza modelu i danych.** Uzgodnić powiązania zasobu z salą i egzemplarzem sprzętu. Zachować istniejące zasoby i rezerwacje. Rezerwacja sali nie może stanowić podstawy wydania sprzętu.

- [ ] **MP-02 — Modele i ograniczenia.** Przygotować uzgodnione modele szczegółów zasobów, wypożyczeń i historii. Zapisywać rzeczywiste daty wydania i zwrotu, osoby obsługi oraz uwagi. Zabezpieczyć unikalność numeru inwentarzowego, jedno wypożyczenie na rezerwację oraz najwyżej jedno otwarte wypożyczenie egzemplarza.

- [ ] **MP-03 — Wspólna logika operacji.** Przygotować funkcje wydania i zwrotu wykorzystywane przez API i pozostałe interfejsy. Reguły nie mogą istnieć wyłącznie w ekranie desktopu lub pojedynczym widoku.

- [ ] **MP-04 — Wydanie sprzętu.** W transakcji sprawdzić zatwierdzenie rezerwacji, właściwy egzemplarz, aktywność, dozwolony czas odbioru oraz brak otwartego wypożyczenia. Zapisać czas, osobę wydającą i uwagi. Dwie równoczesne próby nie mogą utworzyć dwóch wydań.

- [ ] **MP-05 — Zwrot sprzętu.** Zapisać rzeczywisty czas zwrotu, osobę przyjmującą i uwagi o stanie sprzętu. Ponowienie zwrotu nie może tworzyć drugiego zdarzenia ani nadpisywać pierwotnego czasu. Nie oznaczać sprzętu jako zwróconego wyłącznie na podstawie końca rezerwacji.

- [ ] **MP-06 — Sprzęt niezwrócony.** Udostępnić dane o otwartych i opóźnionych wypożyczeniach. Opóźniony zwrot blokuje kolejne fizyczne wydanie egzemplarza. Nie zmieniać automatycznie późniejszych rezerwacji bez uzgodnionej reguły.

- [ ] **MP-07 — Historia operacji.** Przygotować wspólny zapis zdarzeń rezerwacji, decyzji, wydań i zwrotów. Zdarzenie zawiera rodzaj, czas serwera, wykonawcę i powiązany obiekt. Zmiana danych i historia muszą zapisywać się w jednej transakcji. Nie rejestrować sukcesu po wycofaniu operacji.

- [ ] **MP-08 — Migracje i dane startowe.** Przygotować nowe migracje i uzgodnić ich kolejność. Zaplanować uzupełnienie szczegółowych danych istniejących zasobów. Nie usuwać rekordów dla uproszczenia zmiany schematu.

- [ ] **MP-09 — Testy.** Sprawdzić poprawne wydanie i zwrot, odmowę dla sali i niezatwierdzonej rezerwacji, błędny egzemplarz, brak uprawnienia, wydanie poza dozwolonym czasem, ponowne wydanie i zwrot, równoczesne wydania oraz wycofanie transakcji bez pozostawienia fałszywej historii.

- [ ] **MP-10 — Dokumentacja i przekazanie modułu.** Przekazać modele, migracje, funkcje operacji, testy oraz opis reguł i błędów. Udostępnić API dane potrzebne aplikacji desktopowej.

### Kryteria odbioru

- Można wydać wyłącznie właściwy sprzęt z zatwierdzonej rezerwacji.
- Egzemplarz nie ma dwóch otwartych wypożyczeń.
- Zwrot zapisuje rzeczywisty czas i osobę obsługi.
- Ponowienie operacji nie tworzy duplikatów.
- Historia odpowiada rzeczywiście zapisanym zmianom.
- Istnieją testy i opis modułu.

**Współpraca:** z Paulą uzgodnić zmiany rezerwacji po wydaniu i historię decyzji. Z Mateuszem Drewnowskim uzgodnić funkcje, błędy i uprawnienia. Dane dla desktopu udostępniać przez API.

Materiały uzupełniające: [Opis modułu i wymagania](./02_MATEUSZ_PERKOWSKI_WYPOZYCZENIA.txt).

## Mateusz Drewnowski — API, uwierzytelnianie i kontrola dostępu

**Stan początkowy:** Do zrobienia.

**Proponowana gałąź:** `feature/api`

### Pliki startowe

- `requirements.txt`
- `config/settings.py`
- `config/urls.py`
- `katalog/models.py`
- `katalog/forms.py`
- `katalog/views.py`
- `katalog/admin.py`
- migracje
- wspólna logika przygotowana przez Paulę i Mateusza Perkowskiego

### Zadania

- [ ] **MD-01 — Kontrakt API.** Uzgodnić adresy, metody, parametry, dane wejściowe, odpowiedzi i błędy przed integracją klientów. Prefiks `/api/v1/` jest propozycją do potwierdzenia. Kontrakt zapisać w repozytorium.

- [ ] **MD-02 — Uwierzytelnianie i role.** Wdrożyć mechanizm API korzystający z istniejących kont Django. Określić logowanie, wylogowanie lub unieważnianie poświadczeń oraz zachowanie nieaktywnego konta. Uzgodnić role studenta, pracownika, administratora i obsługi. Nie pozwalać na samodzielne podnoszenie uprawnień.

- [ ] **MD-03 — Konfiguracja Django REST Framework.** Dodać potrzebne zależności i konfigurację, jeżeli nie zostały jeszcze przygotowane. Zachować działający web i adresy. Nie tworzyć osobnego backendu ani drugiej bazy.

- [ ] **MD-04 — Katalog i rezerwacje.** Udostępnić zasoby, filtry, dostępność, tworzenie rezerwacji, własne listy i szczegóły, edycję i anulowanie. Korzystać ze wspólnej logiki webu. Właściciela ustala serwer. Chronić listy i szczegóły przed dostępem do cudzych danych. Uzgodnić paginację, sortowanie i daty ISO 8601 ze strefą czasową.

- [ ] **MD-05 — Decyzje administratora.** Udostępnić zatwierdzanie i odrzucanie rezerwacji z uzasadnieniem. Wykorzystać logikę przygotowaną z Paulą. Sprawdzać aktualny stan i uprawnienia po stronie serwera. Nie pozwalać na dowolną zmianę statusu przez ogólny zapis modelu.

- [ ] **MD-06 — Wydania, zwroty i historia.** Udostępnić zatwierdzone rezerwacje sprzętu, otwarte wypożyczenia, operacje wydania i zwrotu oraz historię. Korzystać z funkcji Mateusza Perkowskiego. Kontrolować widoczność danych zależnie od roli.

- [ ] **MD-07 — Błędy i współbieżność.** Uzgodnić format błędów obejmujący kod, komunikat i błędy pól. Rozróżniać brak logowania, brak uprawnień, brak obiektu, walidację i konflikt stanu. Obsłużyć kolizje oraz wyczerpanie ponowień zakleszczenia przez wspólną logikę. Nie ujawniać tracebacków, zapytań SQL i sekretów klientowi.

- [ ] **MD-08 — OpenAPI i przykłady.** Przygotować specyfikację zgodną z rzeczywistymi endpointami. Opisać uwierzytelnianie, role, pola, daty, filtry, paginację i błędy. Przekazać Mikołajowi przykłady poprawnych i błędnych odpowiedzi przed zakończeniem całego modułu.

- [ ] **MD-09 — Testy.** Sprawdzić brak logowania, konto nieaktywne, próbę podniesienia roli, cudze identyfikatory, niedozwolone decyzje i wydania, błędne daty, kolizje, edycję, ponowienie operacji oraz zgodność odpowiedzi z kontraktem. Sprawdzić również działanie dotychczasowego webu.

- [ ] **MD-10 — Dokumentacja i przekazanie modułu.** Przekazać endpointy, testy, specyfikację, przykłady wywołań oraz instrukcję przygotowania kont i ról. Podać konfigurację adresu serwera bez ujawniania prawdziwych tokenów i haseł.

### Kryteria odbioru

- API korzysta z istniejących kont i wspólnych reguł biznesowych.
- Uprawnienia są sprawdzane po stronie backendu.
- Klient nie może wskazać innego właściciela ani nadać sobie roli.
- Dostępne są operacje potrzebne webowi i desktopowi.
- Odpowiedzi i błędy odpowiadają dokumentacji.
- Pełny przebieg działa z rzeczywistymi klientami.
- Istnieją testy i specyfikacja API.

**Współpraca:** kontrakt uzgodnić z Mikołajem na początku prac. Role i sesje webu ustalić z Paulą, a operacje wypożyczeń i historii z Mateuszem Perkowskim.

Materiały uzupełniające: [Opis modułu i wymagania](./03_MATEUSZ_DREWNOWSKI_API.txt).

## Mikołaj Malinowski — aplikacja desktopowa PyQt

**Stan początkowy:** Do zrobienia.

**Proponowana gałąź:** `feature/desktop`

### Materiały startowe

- zatwierdzony kontrakt API
- przykłady odpowiedzi i błędów
- sposób uwierzytelniania i obsługi ról
- adres działającego backendu
- aktualna struktura repozytorium i zależności
- modele i konspekt jako opis procesu

### Zadania

- [ ] **MM-01 — Środowisko i struktura klienta.** Uzgodnić wersję PyQt, bibliotekę HTTP i strukturę osobnego katalogu desktopu w tym samym repozytorium. Desktop uruchamiać osobno od kontenerów backendu.

- [ ] **MM-02 — Logowanie.** Przygotować konfigurację adresu serwera, formularz logowania i wylogowanie. Obsłużyć błędne dane, konto nieaktywne oraz wygaśnięcie poświadczeń. Nie zapisywać jawnego hasła w pliku. Po wylogowaniu usuwać lokalny stan sesji i chronionych widoków.

- [ ] **MM-03 — Rezerwacje do obsługi.** Wyświetlać zatwierdzone rezerwacje sprzętu wraz z terminem i egzemplarzem. Dodać wyszukiwanie, uzgodnione filtry, odświeżanie i obsługę paginacji. Odróżnić pustą listę od błędu pobierania danych.

- [ ] **MM-04 — Wydanie sprzętu.** Przygotować ekran szczegółów, uwagi i potwierdzenie wydania. Wysyłać operację do API. Wyświetlać sukces dopiero po potwierdzeniu serwera. Blokować przycisk na czas żądania.

- [ ] **MM-05 — Zwrot sprzętu.** Wyświetlać otwarte wypożyczenia i umożliwić zapis zwrotu z uwagami. Pokazywać wynik i czas zwrócony przez serwer. Obsłużyć powtórny zwrot oraz stan zmieniony przez inną osobę.

- [ ] **MM-06 — Historia i sprzęt niezwrócony.** Udostępnić historię wydań i zwrotów oraz otwarte i opóźnione wypożyczenia. Rozróżniać termin rezerwacji od rzeczywistego zwrotu. Prezentować godziny w Europe/Warsaw.

- [ ] **MM-07 — Sieć i błędy.** Żądania nie mogą zamrażać okna. Zastosować timeouty i odpowiedni mechanizm pracy poza głównym wątkiem interfejsu. Obsłużyć brak sieci, niedostępny serwer, odmowę uprawnień, konflikt i niepoprawną odpowiedź. Po utracie odpowiedzi na zapis sprawdzić stan przed ponowieniem operacji.

- [ ] **MM-08 — Użyteczność.** Przygotować czytelne etykiety, polskie znaki, obsługę klawiatury i widoczny stan operacji. Adres API powinien być konfigurowalny. Nie umieszczać haseł i tokenów w kodzie ani zrzutach ekranu.

- [ ] **MM-09 — Testy.** Sprawdzić logowanie, brak sieci, niewłaściwą rolę, listy i paginację, wydanie i zwrot, dwukrotne kliknięcie, konflikt po zmianie przez innego klienta, wygaśnięcie sesji i timeout po zapisie. Odbiór integracji wykonać na rzeczywistym API.

- [ ] **MM-10 — Dokumentacja i przekazanie modułu.** Przekazać kod, zależności, instrukcję uruchomienia na Windows, konfigurację API oraz wyniki testów. Przygotować zrzuty rzeczywistego działania do dokumentacji.

### Kryteria odbioru

- Desktop korzysta z API, bez bezpośredniego połączenia z PostgreSQL.
- Obsługa może pobrać zatwierdzoną rezerwację, wydać sprzęt i zapisać zwrot.
- Historia i otwarte wypożyczenia odpowiadają danym backendu.
- Błędy sieci i uprawnień są czytelnie prezentowane.
- Operacje sieciowe nie blokują interfejsu.
- Program można uruchomić zgodnie z instrukcją na innym komputerze.

**Współpraca:** Mateusz Drewnowski dostarcza API, a Mateusz Perkowski definiuje reguły wydań i zwrotów. Dane przykładowe można wykorzystać do budowy interfejsu, ale końcowy odbiór wymaga prawdziwego backendu.

Materiały uzupełniające: [Opis modułu i wymagania](./04_MIKOLAJ_DESKTOP.txt).

## Ustalenia wspólne przed kodowaniem

| Ustalenie | Osoba prowadząca | Osoby potwierdzające |
|---|---|---|
| Role i uwierzytelnianie API | Mateusz Drewnowski | Paula i Mikołaj |
| Modele szczegółów zasobów, wypożyczeń i historii | Mateusz Perkowski | Paula i Mateusz Drewnowski |
| Przejścia statusów i blokada zmian po wydaniu | Paula | Mateusz Perkowski i Mateusz Drewnowski |
| Endpointy, daty, błędy i paginacja | Mateusz Drewnowski | Paula i Mikołaj |
| Dopuszczalny czas odbioru sprzętu | Mateusz Perkowski | Cały zespół |
| Wykorzystanie wspólnego API przez docelowy web | Paula i Mateusz Drewnowski | Cały zespół |
| Kolejność migracji i scalania zmian | Autorzy zmienianych modułów | Cały zespół |

Dokładne endpointy, mechanizm poświadczeń i szczegóły czasu odbioru wymagają wspólnego ustalenia. Propozycje opisane w materiałach nie oznaczają już wdrożonego rozwiązania.

## Kolejność i terminy

1. **25.11.2026:** pokaz obecnej obsługi rezerwacji.
2. **Po pokazie:** uzgodnienie kontraktu, ról i modeli oraz rozwój poszczególnych modułów.
3. **02.12.2026:** planowany etap integracji decyzji, wydań, zwrotów i klientów.
4. **09.12.2026:** planowany pokaz pełnego obiegu rezerwacji i sprzętu.
5. **16.12.2026:** dokończenie zakresu obowiązkowego i poprawki po integracji.
6. **13.01.2027:** dokumentacja, instrukcje i wyniki testów.
7. **20.01.2027:** sprawdzenie czystego uruchomienia, próba prezentacji i poprawki.
8. **27.01.2027:** oddanie projektu, prezentacja i obrona.

Szczegółowy zakres prac między pokazami stanowi plan zespołu.

## Wspólny scenariusz odbioru

- [ ] Student rezerwuje sprzęt w webie i widzi własne zgłoszenie.
- [ ] Próba zajęcia nakładającego terminu zostaje kontrolowanie odrzucona.
- [ ] Student nie ma dostępu do cudzych danych ani funkcji administratora.
- [ ] Administrator zatwierdza zgłoszenie, a system zapisuje osobę i czas decyzji.
- [ ] Odrzucenie wymaga uzasadnienia i zwalnia termin.
- [ ] Nieudana edycja pozostawia wcześniejsze dane bez zmian.
- [ ] Obsługa loguje się do desktopu i pobiera zatwierdzoną rezerwację przez API.
- [ ] Sprzęt zostaje wydany dokładnie raz.
- [ ] Zwrot zapisuje rzeczywisty czas, osobę i uwagi.
- [ ] Ponowienie wydania lub zwrotu nie tworzy drugiej operacji.
- [ ] Historia pokazuje właściwych wykonawców i czasy.
- [ ] Dane webu i desktopu pozostają spójne.
- [ ] Sprawdzono błędy sieci, wygaśnięcie logowania i równoczesne operacje.
- [ ] Przeprowadzono uruchomienie na nowym środowisku zgodnie z dokumentacją.

## Aktualizacja materiałów

Po zmianie kontraktu lub modeli należy zapisać datę, autora i opis ustalenia w repozytorium oraz uaktualnić odpowiednie materiały TXT.

Zadania oznaczać jako gotowe dopiero po sprawdzeniu działania i integracji. Nierozwiązane problemy i brakujące funkcje powinny być zapisane jawnie.
