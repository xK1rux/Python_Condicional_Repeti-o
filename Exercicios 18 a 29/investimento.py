tipoInv = int(input("Digite o tipo de investimento (1 - Poupança, 2 - Renda Fixa): "))
valorInv = int(input("Digite o valor do investimento: "))
if tipoInv == 1:
    rendimento = valorInv * 1.03
    print(f"O rendimento do investimento em Poupança é R$ {rendimento:.2f}.")
elif tipoInv == 2:
    rendimento = valorInv * 1.05
    print(f"O rendimento do investimento em Renda Fixa é R$ {rendimento:.2f}.")
else:
    print("Tipo de investimento inválido. Por favor, escolha 1 para Poupança ou 2 para Renda Fixa.")