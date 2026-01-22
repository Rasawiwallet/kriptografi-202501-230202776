import hashlib
import itertools
import string

# Hash MD5 target (contoh: hash dari password "selpora")
target_hash = "761eb6c87274b8cc2599cbc5918d86d3"

# Karakter yang akan dicoba
characters = string.ascii_lowercase  # a-z
max_length = 7  # panjang password maksimal

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

found = False

for length in range(1, max_length + 1):
    for guess in itertools.product(characters, repeat=length):
        password = ''.join(guess)
        if md5_hash(password) == target_hash:
            print("Password ditemukan:", password)
            found = True
            break
    if found:
        break

if not found:
    print("Password tidak ditemukan")
