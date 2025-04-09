km = float(input("Digite a distância da viagem: "))

if km <= 200:
    viagem_200_km = km * 0.50
    print(f"A sua viagem vai custar R${viagem_200_km:.2f}")

else:
    viagem_maior_de_200 = km * 0.45
    print(f"A sua viagem vai custar R${viagem_maior_de_200:.2f}")