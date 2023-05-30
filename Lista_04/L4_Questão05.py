'''5) Escreva uma função que recebe uma lista com n números inteiros, e retorna uma
lista com a soma cumulativa dos elementos da lista original onde o i-ésimo
elemento é a soma dos primeiros i+1 elementos da lista original. Ex: [1,2,3] =
[1,3,6]'''

def soma_cumulativa(lista):
    if len(lista) == 0:
        return Exception
    soma = 0
    soma_cumulativa = []
    for num in lista:
        if type(num) != int:
            return Exception
        soma += num
        soma_cumulativa.append(soma)
    return soma_cumulativa

assert soma_cumulativa([1,2,3]) == [1, 3, 6]
assert soma_cumulativa([100, 200, 300, 400, 500]) == [100, 300, 600, 1000, 1500]
assert soma_cumulativa([5, 10, 15, 20]) == [5, 15, 30, 50]
assert soma_cumulativa([3, '2', 3]) == Exception
assert soma_cumulativa([]) == Exception
assert soma_cumulativa([2, True, 35, 4]) == Exception
assert soma_cumulativa([2.4 , 35, 4]) == Exception
print("Todos os teste OK")