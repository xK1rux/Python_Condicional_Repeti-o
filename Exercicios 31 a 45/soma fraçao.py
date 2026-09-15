n = int(input("Digite um número: "))
soma = 1
for i in range(1, n + 1):
    soma += 1 / i
    print (f"A soma das frações de 1 a {n} é {soma:.2f}")