velocidade = float(input("Qual a velocidade do veiculo? "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você foi multado, você ultrapassou a velocidade da via que é de 80Km/h")
    print(f"Você foi multado em R${multa:.2f}")
    print(f"Sua velocidade {velocidade:.2f}KM/H")

else:
    print(f"{velocidade:.2f}KM/H")

