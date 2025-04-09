distância = float(input("Digite a distância da viagem: "))

if distância <= 200:
    viagens_entre_200_km = distância * 0.50
    print(f"A sua viagem vai custar R${viagens_entre_200:.2f}")

else:
    viagens_maiores_que_200 = distância * 0.45
    print(f"A sua viagem vai custar R${viagens_maiores_que_200:.2f}")
