#pede para o usuário digitar um número.
num = int(input("Digite um número: "))

#verifia se o número é par.
if num % 2 == 0:
    print(f"O número {num} é par!")

#vai ser mostrado se a condição de if não for verdadeira.
else:
    print(f"O número {num} é impar!")