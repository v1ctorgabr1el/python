texto = input("Digite algo: ")
print(type(texto))
print('É um número?' , texto.isnumeric())
print('É uma string?', texto.isalpha())
print('É um alfanumerico?' , texto.isalnum())
print('Está tudo em maiusculas?' , texto.isupper())
print('Está tudo em minusculas?' , texto.islower())


