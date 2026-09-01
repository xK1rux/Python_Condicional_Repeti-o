num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    conta1 = num1 - num2
    print(f"A diferença entre {num1} e {num2} é: {conta1:.2f}.")
else:
    conta2 = num2 - num1
    print(f"A diferença entre {num2} e {num1} é: {conta2:.2f}.")