a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
delta = (b**2) - (4*a*c)
if delta < 0:
    print("Não existem raízes reais.")
elif delta == 0:
    raiz = -b // (2*a)
    print(f"Existe uma raiz real: x = {raiz:.2f}.")
else:
    raiz1 = (-b + delta**0.5) // (2*a)
    raiz2 = (-b - delta**0.5) // (2*a)
    print(f"Existem duas raízes reais: x1 = {raiz1:.2f} e x2 = {raiz2:.2f}.")