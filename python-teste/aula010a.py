n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

m = (n1 + n2) / 2

if m >= 6:
    print(f"você tirou uma boa nota, a sua média foi de {m}!")

else:
    print(f"Você tirou uma nota baixa estude mais, a sua média foi de {m}!")