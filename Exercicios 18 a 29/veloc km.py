numVoltas = int(input("Digite o número de voltas: "))
distancia = int(input("Digite a extensão do circuito (em m): "))
tempo = int(input("Digite o tempo gasto (em min): "))
velocidade = ((numVoltas * distancia) / (tempo)) * 0.06
print(f"A velocidade média foi de {velocidade:.2f} km/h.")