# AL_2026_27_st_zespol_7 — UniBook

System rezerwacji sal i sprzętu na uczelni. W aplikacji webowej działają logowanie, katalog zasobów, formularz rezerwacji i lista własnych zgłoszeń. Rezerwacje są zapisywane w PostgreSQL, gdzie ograniczenie bazodanowe blokuje nakładające się terminy tego samego zasobu.

Stan realizacji na 22 listopada 2026 roku.

## Zrealizowane funkcje

- Uruchamianie Django i PostgreSQL przez Docker Compose.
- Migracje kont, sesji, zasobów i rezerwacji.
- Dodawanie i edycja zasobów w panelu administratora.
- Logowanie zwykłego użytkownika i dostęp do aktywnych zasobów.
- Rezerwacja wybranego zasobu z początkiem, końcem i celem wykorzystania.
- Przypisanie zalogowanego użytkownika oraz statusu Oczekująca przy zapisie.
- Lista własnych rezerwacji.
- Walidacja kolejności dat, początku nowej rezerwacji i aktywności zasobu.
- Sprawdzanie kolizji w formularzu oraz ochrona w PostgreSQL przez ExclusionConstraint.
- Dopuszczenie sąsiadujących terminów i równoczesnych rezerwacji różnych zasobów.

Przygotowano również konspekt, diagram przypadków użycia, diagram komponentów i model logiczny bazy.

## Technologie

- Python 3.12 i Django 5.2.
- PostgreSQL 16 i sterownik psycopg.
- Szablony Django i HTML.
- Docker Compose.
- PostgreSQL btree_gist do ograniczenia rezerwacji.

Obecna wersja webowa korzysta z widoków, formularzy i sesji Django. Wspólne REST API dla klienta desktopowego oraz OpenAPI przewidziano w dalszym etapie.

## Uruchomienie lokalne

Wymagany jest działający Docker Desktop lub Docker Engine z Docker Compose. Polecenia należy wykonywać w folderze repozytorium.

### Konfiguracja

Obok compose.yaml należy utworzyć plik .env z własnymi wartościami.

```dotenv
POSTGRES_DB=unibook
POSTGRES_USER=unibook
POSTGRES_PASSWORD=uzupelnij_lokalne_haslo
DJANGO_SECRET_KEY=uzupelnij_lokalny_klucz
```

Obraz aplikacji można zbudować, a losowy klucz wygenerować następująco.

```powershell
docker compose build web
docker compose run --rm --no-deps web python -c "import secrets; print(secrets.token_hex(32))"
```

Wygenerowany klucz należy wpisać do .env. Plik .env jest ignorowany przez Git.

### Start i migracje

```powershell
docker compose up -d --build
docker compose exec db pg_isready -U unibook -d unibook
```

Po komunikacie accepting connections należy wykonać migracje.

```powershell
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Migracja katalog.0002_alter_zasob_options_rezerwacja włącza btree_gist przed utworzeniem rezerwacji i ograniczenia kolizji. Użytkownik bazy musi mieć uprawnienia do utworzenia tego rozszerzenia. Lokalna konfiguracja obrazu PostgreSQL wykorzystuje użytkownika inicjalizującego bazę.

### Dane demonstracyjne

Pod adresem http://localhost:8000/admin/ należy dodać aktywne zasoby i utworzyć zwykłe konto student_demo z lokalnym hasłem.

| Nazwa | Typ | Lokalizacja |
|---|---|---|
| Sala 101 | Sala | Budynek A |
| Projektor P01 | Sprzęt | Magazyn A |

Konta i rekordy demonstracyjne są tworzone na danej instalacji. Dane bazy są utrwalane w wolumenie pgdata.

## Obsługa aplikacji

1. Otworzyć http://localhost:8000/zasoby/ i zalogować się.
2. Przy wybranym zasobie kliknąć Rezerwuj.
3. Podać przyszły początek, koniec oraz cel wykorzystania.
4. Zapisać formularz. Po powodzeniu otworzy się strona Moje rezerwacje.
5. Sprawdzić status Oczekująca i daty w strefie Europe/Warsaw.

Adres formularza ma postać /zasoby/ID/rezerwuj/, gdzie ID jest identyfikatorem zasobu. Lista zgłoszeń użytkownika jest dostępna pod /moje-rezerwacje/.

## Ochrona przed kolizjami

Termin blokują rezerwacje oczekujące i zatwierdzone. Ograniczenie rezerwacja_bez_kolizji porównuje identyfikator zasobu i przedział czasu z granicami [początek, koniec). Pozwala to zapisać rezerwację rozpoczynającą się dokładnie w chwili zakończenia poprzedniej.

Formularz sprawdza zajętość przed zapisem. W razie konfliktu powstałego między walidacją a zapisem PostgreSQL odrzuca operację, a widok obsługuje IntegrityError w transakcji i wyświetla komunikat o zajętym terminie.

## Wykonana weryfikacja

| Sprawdzenie | Wynik |
|---|---|
| Uruchomienie, migracje i logowanie | Poprawne |
| Zapis rezerwacji i lista własnych zgłoszeń | Poprawne |
| Nakładające się terminy tego samego zasobu | Konflikt odrzucony z komunikatem |
| Sąsiadujące przedziały czasu | Obie rezerwacje zapisane |
| Dwa różne zasoby w tym samym terminie | Obie rezerwacje zapisane |
| Dwie równoczesne transakcje dla tego samego zasobu i terminu | Jedna zapisana, druga odrzucona przez rezerwacja_bez_kolizji |

W teście współbieżności użyto dwóch wątków, oddzielnych połączeń i transakcji oraz wspólnej bariery startowej. Zapis wykonywano bezpośrednio przez ORM. W bazie pozostała jedna rezerwacja, a drugi zapis zgłosił konflikt. Skrypt zgłosił TEST OK i usunął dane techniczne. Test wykonano lokalnie w Django shell.

## Następny etap

Na 2 grudnia zaplanowano pracę nad decyzjami administratora, wydaniami, zwrotami i historią. Pokaz 9 grudnia ma obejmować rezerwację w webie, zatwierdzenie oraz wydanie i zwrot sprzętu w kliencie desktopowym PyQt korzystającym ze wspólnego API.
