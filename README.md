# AL_2026_27_st_zespol_7 — UniBook

UniBook to system rezerwacji sal i sprzętu na uczelni. Docelowo studenci i pracownicy będą mogli sprawdzać dostępność i rezerwować zasoby, a administrator będzie zarządzał katalogiem i zatwierdzał zgłoszenia.

## Aktualny stan projektu

- Django i PostgreSQL uruchamiają się lokalnie przez Docker Compose.
- Migracje tworzą tabele użytkowników, sesji i katalogu zasobów.
- Administrator może dodawać i edytować zasoby w panelu Django.
- Użytkownik testowy `student_demo` może zalogować się i otworzyć katalog.
- Katalog wyświetla aktywne zasoby z PostgreSQL. Sprawdziliśmy go na dwóch rekordach: Sala 101 i Projektor P01.
- Przygotowaliśmy konspekt, diagram przypadków użycia, diagram komponentów oraz model logiczny bazy danych.

## Uruchomienie lokalne

Wymagania: działający Docker Desktop lub Docker Engine z Docker Compose. Polecenia wykonuj w folderze repozytorium.

### 1. Przygotuj konfigurację

Utwórz plik `.env` obok `compose.yaml`. Ustaw własne hasło do lokalnej bazy i własny klucz Django.

```dotenv
POSTGRES_DB=unibook
POSTGRES_USER=unibook
POSTGRES_PASSWORD=uzupelnij_lokalne_haslo
DJANGO_SECRET_KEY=uzupelnij_lokalny_klucz
```

Losowy klucz możesz wygenerować po zbudowaniu obrazu:

```powershell
docker compose build web
docker compose run --rm --no-deps web python -c "import secrets; print(secrets.token_hex(32))"
```

Wklej wynik jako wartość `DJANGO_SECRET_KEY` w `.env`. Plik `.env` jest wykluczony z Gita.

### 2. Uruchom aplikację i wykonaj migracje

```powershell
docker compose up -d --build
docker compose exec db pg_isready -U unibook -d unibook
```

Gdy baza zgłosi `accepting connections`, wykonaj:

```powershell
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

### 3. Dodaj dane demonstracyjne

Zaloguj się do panelu administratora pod adresem `http://localhost:8000/admin/` i dodaj dwa aktywne zasoby:

| Nazwa | Typ | Lokalizacja |
|---|---|---|
| Sala 101 | Sala | Budynek A |
| Projektor P01 | Sprzęt | Magazyn A |

W panelu utwórz też zwykłe konto `student_demo` i ustaw mu lokalne hasło.

### 4. Sprawdź katalog

Otwórz `http://localhost:8000/zasoby/` w oknie incognito. Po zalogowaniu jako `student_demo` powinny pojawić się oba zasoby.

## Następny etap

Na pokaz 25 listopada planujemy dodać formularz rezerwacji, zapis zgłoszenia w PostgreSQL oraz odrzucanie terminów kolidujących z istniejącą rezerwacją tego samego zasobu.