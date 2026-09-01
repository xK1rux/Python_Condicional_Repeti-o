hInicio =int(input("Digite a hora de início do jogo (0 a 23): "))
mInicio = int(input("Digite o minuto de início do jogo (0 a 59): "))
hFim = int(input("Digite a hora de término do jogo (0 a 23): "))
mFim = int(input("Digite o minuto de término do jogo (0 a 59): "))
if hInicio == hFim and mInicio == mFim:
    print("O jogo não pode durar 24 horas.")
elif hFim < hInicio:
    duraçaoh = 24 - hInicio + hFim
    if mFim < mInicio:
        duraçaom = 60 - mInicio + mFim
        duraçaoh -= 1
    else:
        duraçaom = mFim - mInicio
elif hFim > hInicio:
    duraçaoh = hFim - hInicio
    if mFim < mInicio:
        duraçaom = 60 - mInicio + mFim
        duraçaoh -= 1
    else:
        duraçaom = mFim - mInicio
print(f"A duração do jogo foi de {duraçaoh} horas e {duraçaom} minutos.")