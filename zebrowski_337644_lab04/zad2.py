import hashlib
import hmac
import secrets


def wczytaj(nazwa="hasla.txt"):
    baza = {}
    with open(nazwa, "r", encoding="utf-8") as file:
        for linia in file.read().splitlines():
            if not linia.strip():
                continue
            login, iteracje, sol_hex, skrot_hex = linia.split(":")
            baza[login] = (int(iteracje), sol_hex, skrot_hex)
    return baza


baza = wczytaj()


def weryfikuj(login, haslo):
    if login not in baza:
        return False
    iteracje, sol_hex, skrot_hex = baza[login]
    wyliczony = hashlib.pbkdf2_hmac("sha256", haslo.encode("utf-8"), bytes.fromhex(sol_hex), iteracje, dklen=32)
    return hmac.compare_digest(wyliczony, bytes.fromhex(skrot_hex))


def dodaj(login, haslo):
    iteracje = 600000
    sol = secrets.token_bytes(16)
    skrot = hashlib.pbkdf2_hmac("sha256", haslo.encode("utf-8"), sol, iteracje, dklen=32)
    baza[login] = (iteracje, sol.hex(), skrot.hex())

print("anna, Kasztan-2026 ", weryfikuj("anna", "Kasztan-2026"))
print("anna, kasztan-2026 ", weryfikuj("anna", "kasztan-2026"))
print("piotr, Żółw na łące ", weryfikuj("piotr", "Żółw na łące"))
print("kasia, Kasztan-2026 ", weryfikuj("kasia", "Kasztan-2026"))
dodaj("test1", "TajneHaslo-123")
dodaj("test2", "TajneHaslo-123")

print("Sole takie same?   ", baza["test1"][1] == baza["test2"][1])
print("Skróty takie same? ", baza["test1"][2] == baza["test2"][2])
print("test1 weryfikacja: ", weryfikuj("test1", "Haslo337644"))
print("test2 weryfikacja: ", weryfikuj("test2", "Haslo337644"))