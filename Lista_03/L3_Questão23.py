'''23. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
e retorna o valor de S.
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(n2+1)/(n+3)'''

def valor_s(n):
    s = 0
    if type(n) != int or n <= 0:
        return Exception
    for i in range(1, n+1):
        s += (i**2+1)/(i+3)
    return round(s, 1)

assert valor_s(20) == 169.0
assert valor_s(2) == 1.5
assert valor_s(5) == 8.8
assert valor_s(1) == 0.5
assert valor_s(150) == 10912.8
assert valor_s(-15) == Exception
assert valor_s(15.0) == Exception
assert valor_s(-15.0) == Exception
assert valor_s('A') == Exception
assert valor_s(0) == Exception
assert valor_s(True) == Exception
print('Todos os teste ok!')