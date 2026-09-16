soma = 1
denominador = 1
for i in range(2, 51):
    denominador += 2
    soma += i / denominador
    print(f"A soma das frações de {i} a {denominador} é {soma:.2f}")