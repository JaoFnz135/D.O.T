'''10) Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma dos números que se repetem da lista. Ex: [5, -2, -2, 5, 3, 5, 10, -2, 3,
10, 3, 1] = 20'''

def maior_soma(lista):
    if len(lista) == 0:
        return Exception
    qtd_ocorrencias = {}
    rep = []
    for num in lista:
        if type(num) != int:
            return Exception
        if num not in qtd_ocorrencias:
            qtd_ocorrencias[num] = 1
        else:
            qtd_ocorrencias[num] += 1
            rep += [num]            
        max_soma = 0
        soma = 0
    for num in rep:
        soma = num * qtd_ocorrencias[num]
        if rep.index(num) == 0:
            max_soma = soma
        elif soma > max_soma:
            max_soma = soma
        else:
            continue
    return max_soma         

assert maior_soma([10, 10, 3, 3, 15, 1, 15]) == 30
assert maior_soma([-5, -10, -4, -10, -2, -5]) == -10
assert maior_soma([6, 8, 8, 10, 3, 2, 10, 3, 29, 10, 29]) == 58
assert maior_soma([]) == Exception
assert maior_soma([10, 5, 'a']) == Exception
assert maior_soma([True, 1, 4]) == Exception
assert maior_soma([2.5, ]) == Exception
print('Todos os testes OK!')