"""8) Escreva uma função que recebe uma lista com n números inteiros, e retorna o valor
mais próximo da média de valores da lista. Ex [2.5, 7.5, 10.0, 4.0] = 7.5"""


def vlr_proximo_da_media(lista):
    if len(lista) == 0:
        return Exception
    soma = 0
    for num in lista:
        if type(num) != int and type(num) != float:
            return Exception
        else:
            soma += num
    media = soma / len(lista)
    vlr_mais_proximo = lista[0]
    diferenca_mproxima = abs(lista[0] - media)

    for num in lista:
        diferenca = abs(num - media)
        if diferenca < diferenca_mproxima:
            vlr_mais_proximo = num
            diferenca_mproxima = diferenca

    return vlr_mais_proximo


assert vlr_proximo_da_media([2, 4, 6, 8, 10]) == 6
assert vlr_proximo_da_media([3.5, 4.8, 2.2, 6.1, 5.9]) == 4.8
assert vlr_proximo_da_media([-5, -2, -8, -4, -10]) == -5
assert vlr_proximo_da_media([10]) == 10
assert vlr_proximo_da_media([]) == Exception
assert vlr_proximo_da_media([10, "2", 1]) == Exception
assert vlr_proximo_da_media([10, True]) == Exception
print("Todos os testes OK!")