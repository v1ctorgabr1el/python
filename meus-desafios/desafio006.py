print("Digite seu peso e sua altura para saber o seu IMC, (índice de massa corporal)")

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

soma = peso / (altura ** 2)

if soma < 18.5:
    print("Abaixo do peso")

elif soma >=18.5 and soma < 25:
    print("Peso normal")

elif soma >= 25 and soma <= 29.9:
    print("Sobrepeso")

else:
    print("Acima do peso")