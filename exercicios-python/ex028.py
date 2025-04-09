#Importa a biblioteca random de números aleatórios.
import random

#Mostra na tela do usuário está mensagem.
print("Jogo de adivinhação, tente adivinhar o mesmo número que o computador.")
#Pede para que usuário digite um número de 0 a 5.
número_usuário = int(input("Digite um número de 0 a 5: "))

#O computador irá chutar um número de 0 a 5.
número_computador = random.randint(0 , 5)

#Se o número do usuário for iqual do computador, o usuário irá vencer do computador.
if número_usuário == número_computador:
    print(f"você venceu do computador, seu número foi: {número_usuário}\nnúmero do computador: {número_computador}")

#Caso contrário o computador irá vencer do usuário.
elif número_usuário != número_computador:
    print(f"O computador venceu, número do computadot: {número_computador}\nseu número: {número_usuário}")


   




