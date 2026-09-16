casa = 1
grao = 0
graoT = 0
while (casa <= 64):
    if casa == 1 or casa == 2:
        grao += 1
        graoT += 1
        print(f"na casa {casa} tem {grao} grãos contidos.")
        casa += 1
    else:
        grao += grao
        graoT += grao
        print(f"na casa {casa} tem {grao:,} grãos contidos.".replace(",", "."))
        casa += 1
print(f"Quantidade total de grãos é: {graoT:,}".replace(",", "."))