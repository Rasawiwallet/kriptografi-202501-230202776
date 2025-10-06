# contoh potongan kode
def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():  # hanya huruf yang dienkripsi
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)

# contoh penggunaan
pesan = "Halo Dunia 123"
kunci = 3

encrypted = encrypt(pesan, kunci)
decrypted = decrypt(encrypted, kunci)

print("Pesan Asli :", pesan)
print("Terenkripsi:", encrypted)
print("Terdekripsi:", decrypted)
