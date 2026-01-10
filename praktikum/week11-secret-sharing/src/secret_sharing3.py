import random

# Secret dalam bentuk string
secret_str = "KriptografiUPB2025"

# Konversi string → integer
secret = int.from_bytes(secret_str.encode(), "big")

# Parameter Shamir
k = 3
n = 5
p = 2**521 - 1   # bilangan prima besar (aman untuk string)

# Bangun polinomial
coeffs = [secret] + [random.randint(1, p-1) for _ in range(k-1)]

def f(x):
    return sum(coeffs[i] * (x ** i) for i in range(len(coeffs))) % p

# Bagi rahasia menjadi shares
shares = [(x, f(x)) for x in range(1, n+1)]
print("Shares:", shares)

# Rekonstruksi rahasia (Lagrange Interpolation)
def recover_secret(points):
    result = 0
    for i, (xi, yi) in enumerate(points):
        term = yi
        for j, (xj, _) in enumerate(points):
            if i != j:
                term *= (xj * pow(xj - xi, -1, p)) % p
                term %= p
        result = (result + term) % p
    return result

recovered_int = recover_secret(shares[:k])

# Konversi kembali integer → string
recovered_bytes = recovered_int.to_bytes(
    (recovered_int.bit_length() + 7) // 8, "big"
)
recovered_str = recovered_bytes.decode()

print("Recovered secret:", recovered_str)
