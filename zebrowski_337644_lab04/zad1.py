
import hashlib
import os

def sha256_file(path):
    with open(path, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()


with open("SHA256SUMS.txt", "r", encoding="ascii") as file:
    for line in file:
        expected_hash, relative_path = line.split()
        file_path = os.path.join(os.path.dirname("SHA256SUMS.txt"), relative_path)

        try:
            hash = sha256_file(file_path)
            if hash == expected_hash:
                status = "OK"
            else:
                status = "BŁĄD"
        except FileNotFoundError:
            status = "BRAK"

        print(f"{relative_path} status: {status}")

text_a = hashlib.sha256("Ala ma kota.".encode("ascii")).digest()
text_b = hashlib.sha256("Ola ma kota.".encode("ascii")).digest()
xor_hashes = bytes(a ^ b for a, b in zip(text_a, text_b))

print(f"SHA-256 Ala ma kota.: {text_a.hex()}")
print(f"SHA-256 Ola ma kota.: {text_b.hex()}")
print(f"XOR skrótów: {xor_hashes.hex()}")
print(f"Różniące się bity: {sum(byte.bit_count() for byte in xor_hashes)}")