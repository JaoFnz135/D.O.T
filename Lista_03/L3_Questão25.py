'''25. Escreva uma função que recebe, por parâmetro um valor inteiro e retorna o
seu fatorial.'''

def fatorial(n):
    fat = 1
    if type(n) != int or n <=0:
        return Exception
    for i in range(1, n + 1):
        fat *= i
    return fat


assert fatorial(3) == 6
assert fatorial(4) == 24 
assert fatorial(5) == 120
assert fatorial(6) == 720
assert fatorial(7) == 5040
assert fatorial(0) == Exception
assert fatorial(-10) == Exception
assert fatorial(1.0) == Exception
assert fatorial(-1.0) == Exception
assert fatorial('A') == Exception
assert fatorial(True) == Exception
print('Todos os teste ok!')