num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 != num2:
    if num1 > num2:
        print(f"{num2}, {num1}")
    else:
        print(f"{num1}, {num2}")
else:
    print("Os números são iguais.")