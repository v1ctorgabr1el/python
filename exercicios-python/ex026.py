frase = input("Digite algo: ").strip()

print(f"A sua frase tem {frase.lower().count('a')} letra a")
print(f"A primeira posição da letra a começa na posição {frase.lower().find('a')}")
print(f"A ultima posição da letra a está na posição {frase.lower().rfind('a')-1}")
print(len(frase))
