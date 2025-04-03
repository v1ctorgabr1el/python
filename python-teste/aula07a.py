n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro número: '))
s = n1 - n2
a = n1 + n2
m = n1 * n2
d = n1 / n2
r = n1 % n2
print('A subtração é {}  a adição é {}  e a multiplicação é {}' .format(s, a, m), end=' >>> ')
print('A divisão é {:.2f} e o resto da divisão é {:.2f}' .format(d, r))