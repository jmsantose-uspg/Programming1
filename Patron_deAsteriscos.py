n = int(input("Ingresa la altura: "))

# Triángulo
for i in range(1, n + 1):
    print("*" * i)

print()

# Triángulo invertido
for i in range(n, 0, -1):
    print("*" * i)

print()

# Pirámide centrada
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2*i - 1))

print()

# Diamante
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2*i - 1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2*i - 1))
    