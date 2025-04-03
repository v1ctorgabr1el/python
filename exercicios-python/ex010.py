num = float(input('Quanto dinheiro você tem na carteira R$'))
dolar = num / 5.70
euro = num / 6.18
yen = num /   0.03764
print('Você tem R${:.2f} na sua carteira, você pode comprar ${:.2f}!' .format(num , dolar))
print("Você tem R${} na sua carteira, você pode comprar EUR{:.2f}!" .format(num, euro))
print("Você tem R${} na sua carteira, você pode comprar IENE{:.2f}!" .format(num, yen))

