'''7) Escreva uma função que recebe uma lista com n números inteiros, e retorna True
caso algum elemento apareça mais de uma vez ou False caso nenhum elemento
apareça mais de uma vez. Ex [1, 2, 3, 1] = True. Ex. [3, 7, 2, 4] = False'''

def possui_rep(lista):
    if len(lista) == 0:
        return Exception
    for num in lista:
        if type(num) != int:
            return Exception
    for i in range(len(lista)):
        for j in range(len(lista)):
            # compara cada número com todos os outros numeros a cada repetição
            if lista[i] == lista[j] and i != j:
                return True
            else:
                continue
    return False

assert possui_rep([10, 3, 4, 9, -1]) == False
assert possui_rep([-2, -2, -5, -10, -3, -10, -5]) == True 
assert possui_rep([0, 10, 4]) ==  False
assert possui_rep([5, 10, 9, 4, 3, 4, 9, 7, 7]) == True
assert possui_rep([-1, 1, -1, -1, -1, 1, 2]) == True
assert possui_rep([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]) == True
assert possui_rep([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
assert possui_rep([]) == Exception
assert possui_rep([10, 4, "a", 3, -2]) == Exception
assert possui_rep([1.0, 5, -3]) == Exception
assert possui_rep([9, True, 9, 9]) == Exception
print("Todos os testes OK!")
