salario = float(input("Digite o sálario do funcionario: "))
salario_porcento = salario + (salario * (15 / 100))
print("O valor inicial do salário era de R${:.2f} e com 15% de aumento ira ficar R${:.2f}" .format(salario, salario_porcento))
