from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256


def szyfruj_i_odszyfruj(dane_jawne):
    haslo = "maciek1234"
    sol = get_random_bytes(16)
    iv = get_random_bytes(16) 

    klucz = PBKDF2(haslo.encode("utf-8"), sol, dkLen=32, count=200000, hmac_hash_module=SHA256,)
    szyfr = AES.new(klucz, AES.MODE_CBC, iv)

    dane_dopelnione = pad(dane_jawne, AES.block_size)  
    kryptogram = szyfr.encrypt(dane_dopelnione)

    klucz_do_odszyfrowania = PBKDF2(haslo.encode("utf-8"), sol, dkLen=32, count=200000, hmac_hash_module=SHA256,)
    szyfr_odszyfrowania = AES.new(klucz_do_odszyfrowania, AES.MODE_CBC, iv)
    odszyfrowane_dopelnione = szyfr_odszyfrowania.decrypt(kryptogram)
    odszyfrowane = unpad(odszyfrowane_dopelnione, AES.block_size)

    return kryptogram, odszyfrowane



with open("wiadomosc.txt", "wb") as f:
    f.write(b"test1234.")

with open("wiadomosc.txt", "rb") as f:
    bajty_pliku = f.read()


kryptogram1, odszyfrowane1 = szyfruj_i_odszyfruj(b"")
print(f"Dla pustych danych: {len(kryptogram1)} B, Zgodne: {b'' == odszyfrowane1}")


dane2 = b"0123456789ABCDEF"
kryptogram2, odszyfrowane2 = szyfruj_i_odszyfruj(dane2)
print(f"Dla 16 bajtów: {len(kryptogram2)} B, Zgodne: {dane2 == odszyfrowane2}")


kryptogram3, odszyfrowane3 = szyfruj_i_odszyfruj(bajty_pliku)
print(f"Dla pliku: {len(kryptogram3)} B, Zgodne: {bajty_pliku == odszyfrowane3}")


kryptogram1, _ = szyfruj_i_odszyfruj(b"0123456789ABCDEF")
kryptogram2, _ = szyfruj_i_odszyfruj(b"0123456789ABCDEF")
print("Czy dwa szyfrowania dają ten sam kryptogram?:", kryptogram1 == kryptogram2)