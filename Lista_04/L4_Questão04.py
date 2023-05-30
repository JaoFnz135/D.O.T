"""4) Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma de qualquer seguimento da lista. Ex: Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9,
-6, 4, 1] = 34"""


def maior_soma(lista):
    if len(lista) <= 1:
        return Exception
    # Verifica o tipo
    for num in lista:
        if type(num) != int:
            return Exception
    soma = lista[0]
    soma_max = lista[0]
    # Cria uma repetição  do tamanho da lista
    for i in range(1, len(lista)):
        # Se a soma da variável 'soma' e do elemento 'i' da lista for maior que o elemento 'i' o valor é atribuido a var 'soma'
        if soma + lista[i] > lista[i]:
            soma = soma + lista[i]  # 'soma' recebe o valor
            # se 'soma' for maior que 'soma_max', a var 'soma_max' recebe o valor de soma
            if soma > soma_max:
                soma_max = soma
            else:
                continue
        # Lógica inversa do código de cima
        elif soma + lista[i] < lista[i]:
            soma = lista[i]
            if soma > soma_max:
                soma_max = soma
            else:
                continue
        else:
            continue
    return soma_max

assert maior_soma([0, 0, 0, 0]) == 0
assert maior_soma([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]) == 34
assert maior_soma([23, 34]) == 57
assert maior_soma([1, 2, 3, 4, 5]) == 15
assert maior_soma([-1, -2, -3, -4, -5]) == -1
assert maior_soma([-27, -55, -8, -92, -14]) == -8
assert maior_soma([]) == Exception
assert maior_soma([1, "rd", 212]) == Exception
assert maior_soma([1133]) == Exception
assert maior_soma([False, 21, 54]) == Exception
assert maior_soma([12.45, 32]) == Exception
print("Todos os teste OK")
