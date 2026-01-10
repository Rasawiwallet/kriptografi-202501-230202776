import random

# Parameter
secret = 1234      # Rahasia (a0)
k = 3              # Threshold (minimal shares)
n = 5              # Total shares
p = 2089           # Bilangan prima (> secret)

# Bangun koefisien polinomial (derajat k-1)
coeffs = [secret] + [random.randint(1, p-1) for _ in range(k-1)]

# Fungsi polinomial f(x)
def f(x):
    return sum(coeffs[i] * (x ** i) for i in range(len(coeffs))) % p

# Generate shares
shares = [(x, f(x)) for x in range(1, n+1)]
print("Shares:", shares)

# Rekonstruksi rahasia (Lagrange Interpolation)
def lagrange(points):
    result = 0
    for i, (xi, yi) in enumerate(points):
        term = yi
        for j, (xj, _) in enumerate(points):
            if i != j:
                term *= (xj * pow(xj - xi, -1, p)) % p
                term %= p
        result = (result + term) % p
    return result

# Ambil 3 shares untuk rekonstruksi
recovered = lagrange(shares[:3])
print("Recovered secret:", recovered)
