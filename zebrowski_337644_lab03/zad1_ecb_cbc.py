
from Crypto.Cipher import DES,AES
from Crypto.Random import get_random_bytes
import PIL

def wypisz_bloki(nazwa, kryptogram):
    print(nazwa)
    bloki = [kryptogram[i:i + 16] for i in range(0, len(kryptogram), 16)]
    for numer, blok in enumerate(bloki, start=1):
        print(f"Blok {numer}: {blok.hex()}")

klucz = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
dane_jawne = ("0123456789ABCDEF" * 4).encode("ascii")
iv = get_random_bytes(16)
AES_ecb = AES.new(klucz, AES.MODE_ECB)
kryptogram_ecb = AES_ecb.encrypt(dane_jawne)
odzyskane_ecb = AES.new(klucz, AES.MODE_ECB).decrypt(kryptogram_ecb)


AES_cbc = AES.new(klucz, AES.MODE_CBC, iv)
kryptogram_cbc = AES_cbc.encrypt(dane_jawne)
odzyskane_cbc = AES.new(klucz, AES.MODE_CBC, iv).decrypt(kryptogram_cbc)

wypisz_bloki("ECB:", kryptogram_ecb)
wypisz_bloki("CBC:", kryptogram_cbc)

print("Odszyfrowanie ECB poprawne:", odzyskane_ecb == dane_jawne)
print("Odszyfrowanie CBC poprawne:", odzyskane_cbc == dane_jawne)
