'''8. Faça uma função que recebe um valor inteiro e verifica se o valor é positivo
ou negativo. A função deve retornar um valor booleano.'''

def verificacao(n):
    if type(n) != int:
        return Exception
    if n >= 0:
        return True
    elif n < 0:
        return False
    else:
        return Exception

assert verificacao(1) == True
assert verificacao(199) == True
assert verificacao(40) == True
assert verificacao(-1) == False
assert verificacao(-199) == False
assert verificacao(-40) == False
assert verificacao(0) == True
assert verificacao(1.0) == Exception
assert verificacao(-1.0) == Exception
assert verificacao(0.0) == Exception
assert verificacao('A') == Exception
assert verificacao(True) == Exception
print('Todos os teste ok!')