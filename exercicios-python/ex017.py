from math import sqrt

ct1 = float(input("Digite o valor do cateto oposto: "))
ct2 = float(input("Digite o valor do cateto adjacente: "))

hipotenuza = sqrt(ct1 ** 2 + ct2 ** 2) 

print(f"O cateto oposte tem o  valor de {ct1} e o cateto adjcente tem o valor de {ct2}")
print(f"O valor da hipotenuza é {hipotenuza:.2f}")
