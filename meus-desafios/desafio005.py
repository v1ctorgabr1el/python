print("Digite três notas de 0 a 10")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

soma = (nota1 + nota2 + nota3) / 3

if soma > 7:
    print(f"Aprovado a sua nota foi {soma:.2f}")

elif soma >=5 and soma < 7:
    print(f"Recuperação a sua nota foi {soma:.2f}")

else:
    print(f"Reprovado a sua nota foi {soma:.2f}")