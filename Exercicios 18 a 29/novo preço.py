precoAtual = float(input("Digite o preço atual do produto: "))
mediaMensal = float(input("Digite a média mensal de vendas do produto: "))
if precoAtual < 30 and mediaMensal < 500:
    novoPreco = precoAtual * 1.10
    print(f"O novo preço do produto é R$ {novoPreco:.2f}.")
elif 30 <= precoAtual < 80 and 500 < mediaMensal < 1000:
    novoPreco = precoAtual * 1.15
    print(f"O novo preço do produto é R$ {novoPreco:.2f}.")
elif precoAtual >= 80 and mediaMensal >= 1000:
    novoPreco = precoAtual * 0.95
    print(f"O novo preço do produto é R$ {novoPreco:.2f}.")
else:
    novoPreco = precoAtual
    print(f"O preço do produto permanece o mesmo: R$ {novoPreco:.2f}.")