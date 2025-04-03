km = float(input("Quantos km foram rodados? "))
dia = int(input("Por quantos dias o carro foi alugado? "))
diaria = dia * 60
quilometros = km * 0.15
s = diaria + quilometros
print("O carro foi alugado por {} dias, o valor da diaria ficou R${}" .format(dia, diaria))
print("Foi rodado {}km/h, o valor ficou R${:.2f}" .format(km, quilometros))
print("O valor total a ser pago será de R${:.2f}" .format(s))
