nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

soma = (nota1 + nota2) / 2

if soma >= 7:
    print(f"você foi aprovado sua média foi de {soma}")

elif soma >= 5 and soma < 7:
    print(f"você ficou de recuperação sua média foi de {soma}")

else:
    print(f"você foi reprovado sua média foi de {soma}")

