#pede para o usuário digitar o valor inicial do produto.
produto = float(input("Digite o preço do produto: "))
#Pede para o usuário digitar o valor do desconto do produto.
desconto = int(input("Digite o valor do desconto: "))

#calcula o valor inicial do produto vezes os valor do desconto.
desconto_produto = (produto * desconto / 100) 
#faz a soma total do desconto.
total = produto - desconto_produto 

#mostra pra o usuário o valor total do produto.
print(f"O valor do desconto foi de {desconto}%")
print(f"O valor inical do produto era de R${produto:.2f}")
print(f"com desconto de {desconto}% você ira pagar R${total:.2f} pelo produto")