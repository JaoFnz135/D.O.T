'''22. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
e retorna o valor de S.
S = 1 + 1/1! + 1/2! + 1/3! + 1 /N!'''

def valor_s(n):
    if type(n) != int or n <=0:
        return Exception
    else:
        denom = 1
        s = 1
        for i in range(1, n+1):
            denom *= i
            s += (1/denom)
    return s

assert valor_s(10) ==  2.7182818011463845
assert valor_s(1) == 2.0
assert valor_s(5) == 2.7166666666666663
assert valor_s(20) == 2.7182818284590455
assert valor_s(1.0) == Exception
assert valor_s(None) == Exception
assert valor_s(True) == Exception
assert valor_s(-10) == Exception
assert valor_s('A') == Exception
assert valor_s(0) == Exception
print('Todos os teste ok!')