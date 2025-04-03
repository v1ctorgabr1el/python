produto = float(input("Qual é o valor do produto R$"))
s = produto * (5 / 100)
d = produto - s 
print("O valor do produto original era de R${:.2f} e com 5% de desconto ficou com valor de R${:.2f}" .format(produto, d))