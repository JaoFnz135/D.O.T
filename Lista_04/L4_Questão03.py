'''3) Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6,
4, 1] = 25'''

def maior_soma(lista):
    if len(lista) == 0:
        return Exception
    vlr_anterior = 0
    max_soma = lista[0]
    for num in lista:
        if type(num) != int:
            return Exception
        elif vlr_anterior == 0:
            vlr_anterior = num
        else:
            soma = vlr_anterior + num
            vlr_anterior = num
            if soma > max_soma:
                max_soma = soma
    return max_soma

assert maior_soma([2, 3, 2, -1, 4, 5, 3, -2]) == 9
assert maior_soma([-1, -5, -5, -3, -2, -10, -1]) == -1
assert maior_soma([4, 6, -3, -1, 20, 1, 4, 5, 0]) == 21
assert maior_soma([-10, -1, -54, -53, -2, -5]) == -7
assert maior_soma([]) == Exception
assert maior_soma([10, '-3', 2, 4, '1']) == Exception
assert maior_soma([True, 2, 4, 5, 2]) == Exception
assert maior_soma([1.0, 3.0, 2, 3]) == Exception
print("Todos os testes OK!")