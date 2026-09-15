n = int(input("Digite um número: "))
soma = 1
fatorial = 1
for i in range(1, n + 1):    
    fatorial *= i
    soma += 1 / fatorial
    print(f"A soma das frações de 1 a {n} é {soma:.2f}")