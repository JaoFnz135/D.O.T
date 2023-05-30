'''5. Faça uma função que recebe a idade de uma pessoa em anos, meses e dias
e retorna essa idade expressa em dias.'''

def dias(a, m, d):
    if type(a) != int or type(m) != int or type(d) != int:
        return Exception
    if (m > 12 or d > 30) or (a <= 0 and m <= 0 and d <= 0):
        return Exception
    return (a * 365) + (m * 30) + d

assert dias(1, 1, 1) == 396
assert dias(0, 0, 1) == 1
assert dias(0, 1, 0) == 30
assert dias(1, 0, 0) == 365
assert dias(-1, -3, -3 ) == Exception
assert dias(1, 13, 0) == Exception
assert dias(0, 0, 0) == Exception
assert dias(1, 3, 40) == Exception
assert dias(1, 3, 'a') == Exception
assert dias(1, '11', 1) == Exception
assert dias('a', 3, 0) == Exception
print('Todos os teste ok!')