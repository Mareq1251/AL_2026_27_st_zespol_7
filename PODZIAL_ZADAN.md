# UniBook — podział zadań i pakiet kontekstu

Stan na 24 listopada 2026. Dokument rozdziela wykonane prace od dalszych obowiązków. Lista jest planem realizacji, a nie potwierdzeniem ukończenia nowych modułów.

## Wykonane prace

- **Cały zespół:** konspekt, wymagania i ogólna koncepcja systemu.
- **Marcin Pupek:** diagramy i model danych, Docker, PostgreSQL i Django, logowanie, katalog, rezerwacje, własne zgłoszenia, ochrona przed kolizjami, wykonane sprawdzenia, aktualizacja README i dokumentacji oraz repozytorium.
- Potwierdzono próbę dwóch równoczesnych zapisów. Podczas kolejnej próby wykryto zakleszczenie. Ponawianie dodano do skryptu testowego; obsługa w aplikacji pozostaje zadaniem Pauli we współpracy z API.

## Materiały dla zespołu i modeli językowych

| Materiał | Odnośnik do pliku w pakiecie | Dysk Google |
|---|---|---|
| Pełny kontekst, aktualny stan i wymagania | [Kontekst całego projektu](kontekst/00_UNIBOOK_KONTEKST_I_WYMAGANIA.txt) | Do uzupełnienia po przesłaniu |
| Paula Brajczewska — aplikacja webowa i decyzje administratora | [Samodzielny pakiet TXT](kontekst/01_PAULA_WEB.txt) | Do uzupełnienia po przesłaniu |
| Mateusz Perkowski — wydania, zwroty i historia operacji | [Samodzielny pakiet TXT](kontekst/02_MATEUSZ_PERKOWSKI_WYPOZYCZENIA.txt) | Do uzupełnienia po przesłaniu |
| Mateusz Drewnowski — api, uwierzytelnianie i kontrola dostępu | [Samodzielny pakiet TXT](kontekst/03_MATEUSZ_DREWNOWSKI_API.txt) | Do uzupełnienia po przesłaniu |
| Mikołaj Malinowski — aplikacja desktopowa pyqt | [Samodzielny pakiet TXT](kontekst/04_MIKOLAJ_DESKTOP.txt) | Do uzupełnienia po przesłaniu |

[Repozytorium projektu](https://github.com/Mareq1251/AL_2026_27_st_zespol_7)

Każdy indywidualny TXT zawiera zadania danej osoby, kontekst całego projektu i tekst pełnego konspektu. Wystarczy przekazać modelowi **swój TXT oraz aktualny kod potrzebnych plików**. Nie trzeba dołączać pozostałych czterech TXT. Diagramy należy dodatkowo załączyć w PDF, jeżeli praca wymaga oceny ich oznaczeń.

### Umieszczenie na Dysku Google

1. Przesłać pięć plików TXT z katalogu `kontekst` na Dysk Google.
2. Udostępnić je członkom zespołu i sprawdzić dostęp z ich kont.
3. Skopiować odnośnik do każdego pliku i w odpowiedniej komórce ostatniej kolumny zastąpić tekst przez `[Otwórz TXT](ADRES_SKOPIOWANY_Z_DYSKU)`.
4. Zachować działające odnośniki względne jako kopię do pobrania z repozytorium, jeżeli TXT będą również w GitHubie. Przy publikacji samego MD korzystać z uzupełnionej kolumny Google.
5. Modelowi najlepiej załączyć pobrany TXT. Sam link Google może wymagać logowania lub nie być odczytywalny przez model. Nie trzeba z tego powodu upubliczniać całego folderu.

Adresy Google nie zostały jeszcze podane i nie są wymyślone. Pliki to migawka z 24.11; późniejsze zmiany kodu i kontraktów trzeba aktualizować także w kontekście. Sekrety `.env`, hasła i tokeny nie należą do pakietu.

## Zasady realizacji

- Obecny web działa na widokach i szablonach Django. API i desktop są rozbudową istniejącego projektu.
- Reguły biznesowe mają być wspólne. API i web nie utrzymują osobnych kopii zasad rezerwowania i wydawania.
- Każda osoba odpowiada za kod, testy i dokumentację własnego modułu.
- Wspólne pliki i migracje uzgadniać przed równoległą edycją. Nie nadpisywać migracji 0002, danych demonstracyjnych ani historii.
- Statusy: `Do zrobienia`, `W trakcie`, `Do sprawdzenia`, `Gotowe`, `Zablokowane`.
- Status `Gotowe` wymaga działającego kodu, testów, dokumentacji i sprawdzenia integracji. Sam ekran z danymi przykładowymi nie oznacza gotowej integracji.

## Zestawienie odpowiedzialności

| Osoba | Główny zakres | Zależności |
|---|---|---|
| Paula Brajczewska | Web, decyzje, edycja/anulowanie, poprawki zapisu | Role i API, historia i wypożyczenia |
| Mateusz Perkowski | Modele i logika wydań/zwrotów, historia | Model zasobów, decyzje, uprawnienia API |
| Mateusz Drewnowski | Kontrakt API, uwierzytelnianie i role, endpointy | Wspólna logika webu i wypożyczeń |
| Mikołaj Malinowski | Desktop PyQt i integracja | Kontrakt i działające API |

## Paula Brajczewska — Aplikacja webowa i decyzje administratora

**Stan początkowy:** Do zrobienia. **Proponowana gałąź:** `feature/web-decyzje`.

**Pliki startowe:** katalog/models.py, katalog/forms.py, katalog/views.py, katalog/admin.py, config/urls.py, config/settings.py, katalog/templates/, migracje i requirements.txt. Do integracji: uzgodnione funkcje historii i kontrakt API.

**Współpraca:** Paula uzgadnia pola decyzji i wspólną logikę z Mateuszem Drewnowskim. Z Mateuszem Perkowskim uzgadnia zapis historii oraz odmowę edycji po wydaniu. Współdzielone modele i migracje mają jednego uzgodnionego edytora dla danej zmiany.

- [ ] **PAU-01 Przegląd istniejącego webu** — Odczytać modele, formularze, widoki, adresy i szablony. Uruchomić logowanie, katalog i zapis. Opisać punkt startowy bez tworzenia projektu od nowa. Zachować dotychczasowe adresy albo przygotować kompatybilne przekierowania.

- [ ] **PAU-02 Wspólny wygląd i nawigacja** — Przygotować wspólny szablon bazowy, czytelne formularze, komunikaty i menu: katalog, moje rezerwacje, logowanie/wylogowanie, funkcje administratora według uprawnień. Zachować obsługę klawiatury, etykiety pól i czytelność na mniejszym ekranie. Naprawić błędne polskie znaki. Wygląd nie zastępuje kontroli backendu.

- [ ] **PAU-03 Katalog i dostępność — F04, F05** — Dodać filtry typu i lokalizacji oraz parametrów dostępnych w uzgodnionym modelu. Umożliwić sprawdzenie wolnego przedziału bez traktowania wyniku jako gwarancji późniejszego zapisu. Czytelnie pokazywać nieaktywne lub niedostępne zasoby zgodnie z rolą.

- [ ] **PAU-04 Rejestracja i konta w webie — część F01–F03** — Dodać brakującą rejestrację zwykłego konta, walidację i wylogowanie. Z Mateuszem Drewnowskim ustalić uprawnienia i domyślną rolę. Nie dodawać drugiego modelu kont. Zarządzanie rolami, blokadami i zasobami może korzystać z Django admin, jeśli zostanie to świadomie przyjęte i sprawdzone. Nie nadawać użytkownikowi samodzielnego wyboru roli uprzywilejowanej.

- [ ] **PAU-05 Decyzje administratora — F09, F10** — Dodać listę oczekujących zgłoszeń i podgląd danych. Wspólnie uzgodnić pola decydenta i daty decyzji w modelu. Zatwierdzanie i odrzucanie wymagają backendowej kontroli uprawnienia. Odrzucenie wymaga uzasadnienia. Dane wykonawcy i czasu bierze serwer. Operacje zmieniające stan przez POST z ochroną CSRF, nie przez link GET. Sprawdzić aktualny status w transakcji i zdefiniować zachowanie po powtórzeniu decyzji. Zmiana statusu i zapis zdarzenia muszą być spójne.

- [ ] **PAU-06 Edycja i anulowanie — F08** — Pozwolić właścicielowi zmienić lub anulować przyszłe zgłoszenie w dozwolonych stanach. Obcy użytkownik nie może edytować po podmianie ID. Zmiana zasobu lub terminu zatwierdzonej rezerwacji kieruje ją ponownie do akceptacji. Nieudana zmiana zachowuje pierwotny termin i status. Uzgodnić z modułem wypożyczeń odmowę zmian po fizycznym wydaniu. Sprawdzić także przejścia z nieblokującego statusu do blokującego.

- [ ] **PAU-07 Własne rezerwacje i historia — F11** — Rozszerzyć listę o czytelne statusy, szczegóły decyzji i dostępne akcje. Historię pobierać ze wspólnego modułu Mateusza Perkowskiego. Sprawdzić własność na listach i szczegółach, nie tylko ukrywać przyciski.

- [ ] **PAU-08 Bezpieczny zapis i deadlock** — Zachować rezerwacja_bez_kolizji i rozpoznawanie konkretnego IntegrityError. Wspólnie z API przygotować ograniczone ponowienie całej transakcji dla 40P01 albo uzgodnioną kontrolowaną odmowę po wyczerpaniu prób. Nie ponawiać wewnątrz uszkodzonej transakcji. Nie dublować historii i decyzji. Zabezpieczenie zastosować również przy edycji i zmianie statusu.

- [ ] **PAU-09 Testy** — Zapis poprawny; daty odwrócone i przeszłe; nieaktywny zasób; termin nakładający, sąsiadujący i inny zasób; cudza rezerwacja; decyzja studenta; puste uzasadnienie; odrzucenie zwalnia termin; edycja z kolizją pozostawia dane; nieudane ponowienia nie duplikują skutków; CSRF i brak zmiany przez GET. Test współbieżności na PostgreSQL z kontrolą końcowej liczby rekordów.

- [ ] **PAU-10 Wynik do przekazania** — Działające ekrany i decyzje, zmiany modeli uzgodnione z zespołem, migracje, testy i krótki opis webu. Podać jak uruchomić testy i jakie konta/rzeczywiste role przygotować. Przekazać API wspólną logikę tworzenia, edycji i decyzji, zamiast kopiować ją do endpointów.

Pełny kontekst do załączenia modelowi: [TXT dla Paula Brajczewska](kontekst/01_PAULA_WEB.txt).

## Mateusz Perkowski — Wydania, zwroty i historia operacji

**Stan początkowy:** Do zrobienia. **Proponowana gałąź:** `feature/wypozyczenia-historia`.

**Pliki startowe:** katalog/models.py, istniejące migracje, config/settings.py, wymagania zależności, aktualne widoki rezerwacji oraz model użytkownika/role z repozytorium. Dołączyć diagram PDF do weryfikacji szczegółowych relacji.

**Współpraca:** Z Paulą uzgodnić zmiany rezerwacji po wydaniu i zdarzenia decyzji. Z Mateuszem Drewnowskim uzgodnić sygnatury funkcji, kody błędów i uprawnienia. Mikołaj potrzebuje kontraktu danych i scenariuszy, a nie bezpośredniego dostępu do bazy.

- [ ] **MP-01 Analiza modelu i danych** — Przejrzeć aktualne modele i migracje. Uzgodnić z zespołem powiązanie Zasob z Sala i EgzemplarzSprzetu. Projekt nie może dopuszczać wypożyczenia sali. Zachować istniejące rezerwacje i dane demonstracyjne. Nie tworzyć drugiego, niezależnego katalogu sprzętu.

- [ ] **MP-02 Rozszerzenia danych** — Przygotować uzgodnione modele szczegółów zasobów, wypożyczenia i zdarzenia historii. Wypożyczenie zawiera rezerwację, rzeczywisty czas wydania, opcjonalny zwrot, osoby obsługi i osobne uwagi wydania/zwrotu. Unikalny numer inwentarzowy, poprawność dat, najwyżej jedno wypożyczenie na rezerwację i jedno otwarte na egzemplarz wymagają zabezpieczeń w bazie i logice. Jeśli część relacji nie pozwala wyrazić reguły bezpośrednio ograniczeniem, opisać i wdrożyć transakcyjny mechanizm zamiast pozornej kontroli.

- [ ] **MP-03 Jedna logika operacji** — Przygotować funkcje biznesowe wydania i zwrotu wywoływane przez API, web lub panel. Przekazywać uprawnionego wykonawcę z backendu. Nie implementować reguł tylko w serializerze albo ekranie desktopu. Zaprojektować współpracę z kontrolą ról od Mateusza Drewnowskiego.

- [ ] **MP-04 Wydanie — F12** — W transakcji sprawdzić aktualne zatwierdzenie rezerwacji, typ sprzętu, właściwy egzemplarz, aktywność oraz dozwolony czas odbioru. Sprawdzić brak wcześniejszego wypożyczenia tej rezerwacji i brak otwartego wypożyczenia egzemplarza. Zastosować uzgodnione blokady i stałą kolejność ich pobierania. Zapisać rzeczywisty czas, osobę i uwagi. Jednoczesne kliknięcia nie mogą tworzyć dwóch wydań.

- [ ] **MP-05 Zwrot — F13** — Zidentyfikować otwarte wypożyczenie, sprawdzić uprawnienie, zapisać serwerowy czas przyjęcia, osobę i uwagi/stwierdzony stan. Powtórzenie zwrotu nie zmienia pierwotnego czasu i nie dopisuje kolejnego zdarzenia. Uzgodnić czy zwracany jest wcześniejszy wynik, czy kontrolowany konflikt. Nie oznaczać zwrotu automatycznie wraz z końcem rezerwacji.

- [ ] **MP-06 Sprzęt niezwrócony — F14** — Udostępnić dane o otwartych i opóźnionych wypożyczeniach. Opóźnienie oznacza przekroczenie terminu bez rzeczywistego zwrotu. Nie zmieniać samowolnie kolejnych rezerwacji, ale blokować kolejne wydanie tego egzemplarza. Zachować historię po dezaktywacji zasobu lub konta.

- [ ] **MP-07 Historia wspólna** — Przygotować funkcję rejestracji zdarzeń: utworzenie/edycja/anulowanie rezerwacji, decyzje, wydanie i zwrot. Dane: rodzaj, czas serwera, wykonawca, powiązany obiekt, opis. Co najmniej jeden przedmiot zmiany. Historia i zmiana biznesowa zapisują się w jednej transakcji. Nie rejestrować sukcesu przy rollbacku. Udostępnić osobom odpowiedzialnym za web i API jasny sposób dopisywania i filtrowania historii. Nie logować haseł i tokenów.

- [ ] **MP-08 Migracje i dane startowe** — Przygotować nowe migracje, uzgodnić ich kolejność i zależności. Jeśli potrzebne rozszerzenie typu btree_gist jest już aktywowane, wykorzystać istniejącą konfigurację. Zaplanować uzupełnienie danych szczegółowych dla Sala 101 i Projektor P01. Nie usuwać istniejących rekordów dla uproszczenia migracji.

- [ ] **MP-09 Testy** — Poprawne wydanie i zwrot; odmowa dla sali, rezerwacji oczekującej/odrzuconej/anulowanej, złego egzemplarza i niewłaściwej roli; wydanie poza regułą czasu; drugie wydanie i drugi zwrot; dwie równoczesne próby wydania; opóźnienie blokujące kolejny odbiór; rollback bez osieroconej historii; historia zgodna z wykonawcą i czasem. PostgreSQL oraz osobne połączenia dla testów równoczesnych.

- [ ] **MP-10 Wynik do przekazania** — Modele, migracje, wspólne funkcje operacji i historii, testy, dokumentacja reguł i lista wyjątków dla API. Interfejs graficzny desktopu nie należy do tego zakresu; przygotować dane potrzebne Mikołajowi przez Mateusza Drewnowskiego.

Pełny kontekst do załączenia modelowi: [TXT dla Mateusz Perkowski](kontekst/02_MATEUSZ_PERKOWSKI_WYPOZYCZENIA.txt).

## Mateusz Drewnowski — API, uwierzytelnianie i kontrola dostępu

**Stan początkowy:** Do zrobienia. **Proponowana gałąź:** `feature/api`.

**Pliki startowe:** requirements.txt, config/settings.py, config/urls.py, katalog/models.py, katalog/forms.py, katalog/views.py, katalog/admin.py, migracje oraz kod wspólnej logiki od Pauli i Mateusza Perkowskiego. Sprawdzić, czy pliki API już powstały, przed ich tworzeniem.

**Współpraca:** Uzgodnić kontrakt z Mikołajem na początku. Wspólnie z Paulą ustalić role i sesje webu, a z Mateuszem Perkowskim operacje wypożyczeń i historii. Wspólna logika pozostaje jedna; serializery nie są niezależną kopią zasad.

- [ ] **MD-01 Inwentaryzacja i kontrakt** — Sprawdzić wymagania, obecne modele, widoki i zależności. Uzgodnić REST API z Paulą, Mateuszem Perkowskim i Mikołajem przed integracją. Wersjonowany prefiks /api/v1/ może być propozycją; nie jest potwierdzonym istniejącym adresem. Zapisać metody, zasoby, parametry, przykłady JSON i błędy w repozytorium.

- [ ] **MD-02 Uwierzytelnianie i role — F01, F02** — Uzgodnić i wdrożyć mechanizm API zgodny z kontami Django. Opisać logowanie, wylogowanie lub unieważnienie i zachowanie nieaktywnego konta. Nie przyjmować niezaufanego user_id jako zalogowanego konta. Ustalić wspólne role student/pracownik/administrator/obsługa, najlepiej na istniejącym mechanizmie Django bez wymiany modelu użytkownika. Konfigurację ról oraz uprawnień panelu uzgodnić z Paulą. Nie utożsamiać uprawnień biznesowych ze wszystkimi flagami Django bez jawnej decyzji.

- [ ] **MD-03 Konfiguracja DRF** — Jeżeli nie jest jeszcze zainstalowany, dodać Django REST Framework do zależności i konfiguracji. Zachować działające adresy webowe, szablony i sesje. Ograniczyć zmiany do potrzeb integracji. Nie wprowadzać drugiego backendu ani nowej bazy. Sposób korzystania z API przez web ustalić z Paulą, odróżniając wspólną logikę od faktycznych wywołań HTTP.

- [ ] **MD-04 Katalog i rezerwacje — F03–F08, F11** — Udostępnić listę/szczegóły zasobów, filtry i dostępność, tworzenie, własne listy/szczegóły, edycję i anulowanie. Operacje korzystają ze wspólnej logiki webu. Właściciela przypisuje serwer. Listy muszą być filtrowane według uprawnień, a szczegóły chronione przed podmianą ID. Uzgodnić paginację, sortowanie, strefowe daty ISO 8601 oraz czytelny format błędów.

- [ ] **MD-05 Decyzje — F09, F10** — Udostępnić operacje akceptacji i odrzucenia dla administratora, z uzasadnieniem i czasem/osobą decyzji. Wywoływać logikę przygotowaną z Paulą. Stan ponownie sprawdzany po stronie serwera, niezależnie od aktualności ekranu klienta. Nie pozwalać przesłać dowolnego statusu przez ogólny zapis modelu.

- [ ] **MD-06 Wydania, zwroty i historia — F12–F14** — Udostępnić zatwierdzone rezerwacje sprzętu, otwarte wypożyczenia, wydanie, zwrot i historię. Korzystać z funkcji Mateusza Perkowskiego. API nie omija ograniczeń przy wywołaniu bez desktopu. Osobno kontrolować widoczność danych studenta, administratora i obsługi.

- [ ] **MD-07 Błędy i współbieżność** — Uzgodnić przewidywalny format błędu: kod maszynowy, komunikat i ewentualne błędy pól. Rozróżnić brak uwierzytelnienia, brak uprawnień, brak obiektu, walidację i konflikt stanu. Konkretne statusy HTTP są częścią kontraktu. Obsłużyć kolizję rezerwacji i wyczerpanie ponowień deadlocku przez wspólną logikę. Nie ujawniać tracebacków, SQL i sekretów w odpowiedzi klienta. Ograniczyć czas operacji i powtórzenia.

- [ ] **MD-08 OpenAPI i przykłady** — Przygotować specyfikację OpenAPI spójną z rzeczywistymi endpointami. Udokumentować uwierzytelnianie, wymagane pola, role, daty, filtry, paginację, odpowiedzi błędów oraz przebieg rezerwacja–decyzja–wydanie–zwrot. Mikołaj dostaje przykłady poprawnych i błędnych odpowiedzi przed zakończeniem całości. Mocki wyraźnie oznaczone, nie jako gotowy backend.

- [ ] **MD-09 Testy** — Brak logowania, nieaktywne konto, próba podniesienia własnej roli, cudze ID, niedozwolone decyzje i wydania, listy niewyciekające cudzych danych, błędne daty, kolizja, edycja i rollback, ponowne wywołania, pełny scenariusz obu klientów. Sprawdzić zgodność rzeczywistych odpowiedzi z kontraktem i zachowanie dotychczasowego webu.

- [ ] **MD-10 Wynik do przekazania** — Endpointy i konfiguracja, testy, specyfikacja API, przykłady wywołań i instrukcja przygotowania kont/rol. Nie umieszczać prawdziwych tokenów w dokumentacji. Przekazać Mikołajowi bazowy adres i zatwierdzony kontrakt, a nie wymóg znajomości tabel PostgreSQL.

Pełny kontekst do załączenia modelowi: [TXT dla Mateusz Drewnowski](kontekst/03_MATEUSZ_DREWNOWSKI_API.txt).

## Mikołaj Malinowski — Aplikacja desktopowa PyQt

**Stan początkowy:** Do zrobienia. **Proponowana gałąź:** `feature/desktop`.

**Pliki startowe:** Zatwierdzony kontrakt API, przykłady odpowiedzi, sposób uwierzytelniania i ról, adres uruchomionego serwera, aktualna struktura repozytorium i zależności. Do orientacji modele i konspekt. Nie są potrzebne hasła bazy ani .env backendu.

**Współpraca:** Mateusz Drewnowski dostarcza API, a Mateusz Perkowski definiuje reguły wydań i zwrotów. Do czasu dostępności API można przygotować UI na oznaczonych danych testowych. Odbiór modułu wymaga jednak rzeczywistego backendu, nie samych mocków.

- [ ] **MM-01 Kontrakt i środowisko** — Zapoznać się z modelem procesu. Z Mateuszem Drewnowskim uzgodnić API, uwierzytelnianie, przykłady odpowiedzi, daty i błędy. Wybrać i zapisać wersję PyQt oraz zależność HTTP. Przygotować czytelny osobny katalog klienta w tym samym repozytorium; jego nazwa jest do uzgodnienia. Desktop uruchamiany osobno od kontenerów backendu.

- [ ] **MM-02 Logowanie** — Przygotować okno adresu serwera i logowania, obsługę poprawnych i błędnych danych, konta nieaktywnego oraz wylogowania. Używać mechanizmu API, nie łączyć się z PostgreSQL. Nie zapisywać jawnego hasła w pliku. Po wylogowaniu usuwać lokalny stan sesji i chronionych widoków. Obsłużyć utratę ważności poświadczeń.

- [ ] **MM-03 Lista rezerwacji do obsługi** — Pokazać zatwierdzone rezerwacje sprzętu z terminem, egzemplarzem i danymi potrzebnymi do wydania. Dodać wyszukiwanie, filtry uzgodnione z API, odświeżanie i obsługę paginacji. Sale nie mogą występować jako sprzęt do wydania. Pustą listę odróżnić od awarii pobierania.

- [ ] **MM-04 Wydanie** — Ekran szczegółów pokazuje rezerwację i właściwy egzemplarz. Umożliwić wpisanie uwag i potwierdzenie operacji. Wysyłać żądanie do API, a wynik wyświetlać dopiero po odpowiedzi serwera. Zablokować przycisk na czas operacji, ale nie traktować tego jako zabezpieczenia przed powtórzeniem po stronie backendu.

- [ ] **MM-05 Zwrot** — Pokazać otwarte wypożyczenia, umożliwić identyfikację egzemplarza, wpisanie uwag/stanu i zapis zwrotu. Wyświetlić czas i wynik z serwera. Powtórny zwrot i stan zmieniony przez inną osobę muszą kończyć się czytelnym komunikatem i odświeżeniem danych.

- [ ] **MM-06 Historia i sprzęt niezwrócony** — Udostępnić historię wydań/zwrotów i listę otwartych/opóźnionych wypożyczeń według uprawnień. Rozróżniać termin rezerwacji od rzeczywistego czasu zwrotu. Prezentować godziny w Europe/Warsaw przy transmisji dat zgodnej z API.

- [ ] **MM-07 Responsywność i błędy** — Żądania sieciowe nie mogą zamrażać okna. Zastosować timeouty i odpowiedni mechanizm pracy poza głównym wątkiem UI. Obsłużyć niedostępny serwer, brak sieci, odmowę uprawnienia, konflikt, błędy walidacji oraz nieoczekiwaną odpowiedź. Po utracie odpowiedzi na zapis nie ponawiać automatycznie wydania w ciemno: najpierw sprawdzić stan przez API lub użyć uzgodnionej idempotencji. Nie pokazywać sukcesu bez potwierdzenia.

- [ ] **MM-08 Użyteczność** — Czytelne etykiety, polskie znaki, obsługa klawiatury, widoczny zalogowany użytkownik i stan operacji, potwierdzenie ważnej czynności. Adres API konfigurowalny. Nie zaszywać prawdziwych haseł i tokenów w kodzie ani zrzutach ekranu.

- [ ] **MM-09 Testy** — Logowanie poprawne i błędne; brak sieci; konto bez roli obsługi; lista i paginacja; zatwierdzony sprzęt; wydanie/zwrot; dwukrotne kliknięcie; konflikt po zmianie na innym kliencie; sesja wygasła; timeout po zapisie; wylogowanie i usunięcie danych z widoku. Testować także z prawdziwym API. Mock służy do UI, nie potwierdza działania integracji.

- [ ] **MM-10 Wynik do przekazania** — Kod desktopu, plik zależności lub uzgodniona sekcja zależności, instrukcja uruchomienia na Windows, konfiguracja API, testy i zrzuty rzeczywistego działania do dokumentacji. Umożliwić przejście zatwierdzona rezerwacja–wydanie–zwrot–historia. Nie tworzyć lokalnej kopii bazy jako źródła prawdy.

Pełny kontekst do załączenia modelowi: [TXT dla Mikołaj Malinowski](kontekst/04_MIKOLAJ_DESKTOP.txt).

## Ustalenia wspólne przed kodowaniem

| Ustalenie | Prowadzi | Kto potwierdza |
|---|---|---|
| Role i uwierzytelnianie API | Mateusz Drewnowski | Paula i Mikołaj |
| Modele szczegółów zasobów, wypożyczeń i historii | Mateusz Perkowski | Paula i Mateusz Drewnowski |
| Przejścia statusów i blokada zmian po wydaniu | Paula | Mateusz Perkowski i Mateusz Drewnowski |
| Endpointy, daty, błędy i paginacja | Mateusz Drewnowski | Paula i Mikołaj |
| Reguła dopuszczalnego czasu odbioru | Mateusz Perkowski | Cały zespół |
| Wykorzystanie wspólnego API przez docelowy web | Paula i Mateusz Drewnowski | Cały zespół |
| Kolejność migracji i scalania | Autorzy zmienianych modułów | Cały zespół |

Nie ustalono jeszcze dokładnych endpointów, mechanizmu poświadczeń API ani szczegółów czasu odbioru. Najpierw zapisać decyzje, potem podłączyć klientów. Propozycji z TXT nie przedstawiać jako istniejącego kontraktu.

## Kolejność i terminy

1. **25.11:** pokaz obecnych rezerwacji, bez deklarowania nowych modułów jako wykonanych.
2. **Po pokazie:** uzgodnienie kontraktu, ról i modeli; rozbudowa webu i logiki wypożyczeń. Desktop może równolegle powstawać na oznaczonych danych testowych.
3. **02.12:** plan roboczy — połączenie decyzji, wydań, zwrotów i klientów, spis pozostałych błędów.
4. **09.12:** planowany pokaz pełnego obiegu rezerwacji i sprzętu.
5. **16.12:** dokończenie zakresu obowiązkowego i poprawki po integracji.
6. **13.01 i 20.01:** dokumentacja, test czystego uruchomienia i próba prezentacji.
7. **27.01:** oddanie, prezentacja i obrona.

## Wspólny scenariusz odbioru

- [ ] Student rezerwuje sprzęt w webie; widzi własne zgłoszenie.
- [ ] Próba zajęcia nakładającego terminu jest kontrolowanie odrzucona.
- [ ] Student nie widzi cudzych danych i nie może sam zatwierdzić rezerwacji ani zmienić roli.
- [ ] Administrator zatwierdza zgłoszenie; osoba i czas decyzji są zapisane.
- [ ] Obsługa loguje się do desktopu i pobiera zatwierdzoną rezerwację przez API.
- [ ] Sprzęt jest wydany dokładnie raz; zwrot zapisuje rzeczywisty czas i uwagi.
- [ ] Ponowienie wydania lub zwrotu nie tworzy drugiej operacji.
- [ ] Historia pokazuje wykonawców i czasy, a dane webu i desktopu są spójne.
- [ ] Odrzucenie z uzasadnieniem zwalnia termin; nieudana edycja nie zmienia wcześniejszych danych.
- [ ] Sprawdzono błędy sieci, wygaśnięcie logowania i równoczesne operacje na PostgreSQL.
- [ ] Przeprowadzono czyste uruchomienie bez prywatnych plików i sekretów autora.

## Aktualizowanie pakietu

Po zmianie kontraktu lub modeli dopisać datę, autora i opis ustalenia do wspólnego rejestru w repozytorium, a następnie uaktualnić odpowiednie TXT. Statusy odhaczać dopiero po weryfikacji. Historia zmian Git pozostaje dowodem kodu; ta lista opisuje obowiązki.
