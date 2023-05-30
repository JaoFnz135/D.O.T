'''6. Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito
perfeito quando ele é igual à soma dos seus divisores excetuando ele próprio.
(Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar
um valor booleano.'''

def perfeito(n):
    soma = 0
    if type(n) != int or n <= 0:
        return Exception
    for i in range(1, n):
        if n % i == 0:
            soma += i
    if soma == n:
        return True
    else:
        return False


assert perfeito(6) == True
assert perfeito(28) == True
assert perfeito(496) == True
assert perfeito(495) == False
assert perfeito(2) == False
assert perfeito(4) == False
assert perfeito(100) == False
assert perfeito(-1) == Exception
assert perfeito(0) == Exception
assert perfeito('A') == Exception
assert perfeito(True) == Exception
print('Todos os teste ok!')