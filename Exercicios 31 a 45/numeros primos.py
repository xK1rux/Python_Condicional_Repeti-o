num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1
for i in range(menor, maior + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)