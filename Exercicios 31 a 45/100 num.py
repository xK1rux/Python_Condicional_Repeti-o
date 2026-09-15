quantNum = 0

while quantNum < 100:
    num = int(input("Digite um número: "))
    if num <= 0:
        print("Número inválido. Digite um número positivo.")
        continue
    else:
        quantNum += 1
        if quantNum == 1:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            elif num < menor:
                menor = num
print(f"O maior número digitado foi: {maior} e o menor número digitado foi: {menor}")
        