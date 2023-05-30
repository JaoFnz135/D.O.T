'''12. Faça uma função que recebe 2 valores inteiros por parâmetro e retorna-os
ordenados em ordem crescente.'''

def ordenar_vlr(n1, n2):
    if type(n1) != int or type(n2) != int:
        return Exception
    if n1 == 0 and n2 == 0:
        return Exception
    if n1 > n2:
        return (n2, n1)
    elif n2 > n1:
        return (n1, n2)
    else:
        return Exception

assert ordenar_vlr(3, 4) == (3, 4)
assert ordenar_vlr(4, 3) == (3, 4)
assert ordenar_vlr(100, 50) == (50,100)
assert ordenar_vlr(10, -10) == (-10, 10)
assert ordenar_vlr(10, 0) == (0, 10)
assert ordenar_vlr(0, 0) == Exception
assert ordenar_vlr('A', 1) == Exception
assert ordenar_vlr(1, 'A') == Exception
assert ordenar_vlr(1.0, 50) == Exception
assert ordenar_vlr(10, 5.0) == Exception
assert ordenar_vlr(1, True) == Exception
print('Todos os teste ok!')