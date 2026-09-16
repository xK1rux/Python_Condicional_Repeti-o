soma = 1
numerador = 1
while numerador < 15:
    numerador += 1
    denominador = numerador ** 2
    if numerador % 2 == 0:
        soma -= numerador / denominador
    else:
        soma += numerador / denominador
    print(f"A soma das frações de {numerador} a {denominador} é {soma:.2f}")