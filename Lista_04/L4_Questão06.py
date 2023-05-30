'''6) Escreva uma função que recebe uma lista com n números inteiros, e retorna True
caso a lista esteja ordenada em ordem ascendente ou False caso não esteja
ordenada. Ex [1, 2, 3] = True. Ex. [3, 7, 2] = False'''

def lista_ordenada(lista):
    if len(lista) == 0:
        return Exception
    for num in lista:
        if type(num) != int:
            return Exception
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            continue
        else:
            return False
       

assert lista_ordenada([1, 2, 3, 4, 8]) == True
assert lista_ordenada([1, 5, 4, 4, 8]) == False
assert lista_ordenada([-1, 0, 1, 2, 3]) == True
assert lista_ordenada([1, 2, 3, 4, -1]) == False
assert lista_ordenada([0, 0, 3, 4]) == True
assert lista_ordenada(['2', 0, 3, 4]) == Exception
assert lista_ordenada([0, 1.5 , 3, 4]) == Exception
assert lista_ordenada([0, 1, True, 4]) == Exception
assert lista_ordenada([]) == Exception
print("Todos os teste OK")