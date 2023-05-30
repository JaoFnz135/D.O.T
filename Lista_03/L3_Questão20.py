'''20. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e
retorna o somatório desse valor.'''

def somatorio(n):
    soma = 0
    if type(n) != int or n <= 0:
        return Exception
    for i in range(1, n+1):
        soma += i
    return soma

assert somatorio(2) == 3
assert somatorio(10) == 55
assert somatorio(8) == 36
assert somatorio(9) == 45
assert somatorio(0) == Exception
assert somatorio(-1) == Exception
assert somatorio(True) == Exception
assert somatorio('A') == Exception
assert somatorio(1.0) == Exception
print('Todos os teste ok!')