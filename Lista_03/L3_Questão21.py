'''21. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
e retorna o valor de S.
S = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/N.'''

def valor(n):
    s = 1
    if type(n) != int or n <= 0:
        return Exception
    for i in range(1, n):
        s += (1/(i+1))
    return round(s, 1)


assert valor(2) == 1.5
assert valor(3) == 1.8
assert valor(10) == 2.9
assert valor(150) == 5.6
assert valor(-15) == Exception
assert valor(1.5) == Exception
assert valor('a') == Exception
assert valor(True) == Exception
assert valor(0) == Exception
print('Todos os teste ok!')