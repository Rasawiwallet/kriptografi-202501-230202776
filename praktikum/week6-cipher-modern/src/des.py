from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(8)                  # Kunci 8 byte
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"RAMZISELPORA"                  # 10 byte
padded = pad(plaintext, 8)                 # padding ke kelipatan 8 byte

ciphertext = cipher.encrypt(padded)
print("Ciphertext:", ciphertext)

# Dekripsi
decipher = DES.new(key, DES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), 8)
print("Decrypted:", decrypted)
