'''9) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
lista eliminando todas as ocorrências de valores repetidos. Ex: [5, 4, 5, 7, 3, 4] =
[7, 3]'''

def eliminar_repeticao(lista):
    nova_lista = []
    if len(lista) == 0:
        return Exception
    for i in range(len(lista)):
        if type(lista[i]) != int:
            return Exception
        for j in range(len(lista)):
            repetido = False
            if i != j and lista[i] == lista[j]:
                repetido = True
                break
        if not repetido:
            nova_lista.append(lista[i])
    return nova_lista


assert eliminar_repeticao([10, 4, 3, 4, 9, -1, 9]) == [10, 3, -1]
assert eliminar_repeticao([-2, -2, -5, -10, -3, -10, -5]) == [-3]
assert eliminar_repeticao([0, 10, 4, 0]) == [10, 4]
assert eliminar_repeticao([5, 10, 9, 4, 3, 4, 9, 7, 7]) == [5, 10, 3]
assert eliminar_repeticao([-1, 1, -1, -1, -1, 1, 2]) == [2]
assert eliminar_repeticao([]) == Exception
assert eliminar_repeticao([10, 4, "a", 3, -2]) == Exception
assert eliminar_repeticao([1.0, 5, -3]) == Exception
assert eliminar_repeticao([9, True, 9, 9]) == Exception
print("Todos os testes OK!")
