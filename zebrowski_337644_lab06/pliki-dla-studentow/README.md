# Laboratorium 6 - Tablica ogłoszeń

## Uruchomienie lokalne

Wymagany jest Docker Desktop z obsługą kontenerów Linux i Docker Compose.

```powershell
docker compose up -d
```

Aplikacja jest dostępna pod `http://127.0.0.1:8080`. Po zmianach kodu aplikacji:

```powershell
docker compose restart web
```

Zatrzymanie środowiska:

```powershell
docker compose down
```

Konta testowe i szczegóły środowiska opisuje `START.md`. To celowo uproszczona
aplikacja edukacyjna; nie należy używać jej w środowisku produkcyjnym.
