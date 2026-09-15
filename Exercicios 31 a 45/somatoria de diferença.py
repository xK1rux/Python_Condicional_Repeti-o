num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1
print(f"o maior número é {maior} e o menor número é {menor}")
somaImpares = 0
for i in range(menor, maior):
    if i % 2 == 1:
        somaImpares += i
        print(f"{somaImpares}")