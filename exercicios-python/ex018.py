#importa a biblioteca de matemática
import math

#pede para que o usuário digite
graus = int(input("Digite o angulo do triangulo retângulo: "))

#convert o radiante para graus
radiante = math.radians(graus)

#ira calcular o valor dos graus em seno, cosseno e tangente
seno = math.sin(radiante)
cosseno = math.cos(radiante)
tangente = math.tan(radiante)

print(f"O seno de {graus}° é de {seno:.2f}")
print(f"O cosseno de {graus}° é de {cosseno:.2f}")
print(f"O tangente de {graus}° é de {tangente:.2f}")

