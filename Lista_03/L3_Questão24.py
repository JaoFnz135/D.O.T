'''24. Escreva uma função que recebe, por parâmetro, dois valores X e Z e calcula
e retorna X**z . (sem utilizar funções ou operadores de potência prontos)'''

def potencia(x, z):
    if (type(x) != int or x == 0) or (type(z) != int or z <= 0):
        return Exception
    else:
        pot = 1
        for i in range(1, z+1):
            pot *= x
        return pot

assert potencia(2, 3) ==  8
assert potencia(2, 5) ==  32
assert potencia(5, 2) == 25 
assert potencia(3, 3) ==  27 
assert potencia(-3, 3) ==  -27 
assert potencia(-3, 4) ==  81
assert potencia(0, 4) == Exception
assert potencia(2, 0) == Exception
assert potencia('a', 4) == Exception
assert potencia(10, -4) == Exception
assert potencia(10, 'a') == Exception
assert potencia(10, True) == Exception
assert potencia(True, 5) == Exception
assert potencia(True, 5.5) == Exception
assert potencia(5.2, 1) == Exception
print('Todos os teste ok!')