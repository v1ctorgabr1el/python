num = int(input("Digite um número de 0 a 9999: "))

milhar = num // 1000
centena  = (num % 1000) // 100
dezena =  (num % 100) // 10
unidade = num % 10

print(f"milhar {milhar}")
print(f"centena {centena}")
print(f"dezena {dezena}")
print(f"Unidade {unidade}")