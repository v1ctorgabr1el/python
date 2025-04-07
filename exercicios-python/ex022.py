#Pede para o usuário digitar seu nome.
nome = input("Digite seu nome: ")

#joga todo nome do usuário para maiusculas.
print(f"o seu nome todo em maiusculas é {nome.upper()}")

#joga todo nome do usuário para minusculas.
print(f"O seu nome todo em minusculas é {nome.lower()}")

#conta quantas letras o nome tem sem considerar os espaços.
print(f"O seu nome completo tem ao todo {len(''.join(nome.split()))} letras sem considerar espaços.")



#conta quantas letras tem o primeiro nome do usuário.
print(f"O seu primeiro nome tem {len(nome.split()[0])} letras.")