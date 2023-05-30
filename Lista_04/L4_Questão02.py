'''2) Escreva uma função que recebe uma lista com n números inteiros, conta e imprime
o número de vezes que cada número ocorre na sequência.'''

def contar_num(lista):
    if len(lista) == 0:
        return Exception
    registro_ocorrencia = {}
    for num in lista:
        if type(num) != int:
            return Exception
        elif num not in registro_ocorrencia:
            registro_ocorrencia[num] = 1
        else:
            registro_ocorrencia[num] += 1
    return registro_ocorrencia

assert contar_num([4, 4, 5, 3, 4 , 5, 5, 5, 5, 3, 1 ]) == {4: 3, 5: 5, 3: 2, 1: 1}
assert contar_num([4, 3, 5, 4, 3, 3, 4, 3, 3, 3, -3, -3, 0, 0, -1]) == {4:3, 3:6, 5:1, -3:2, 0:2, -1:1}
assert contar_num([2, 2, 2, 0, 1, 4]) == {2:3, 0:1, 1:1, 4:1}
assert contar_num([]) == Exception
assert contar_num([2, '1', 1]) == Exception
assert contar_num([True, 0, 1]) == Exception
assert contar_num([1.0, 2.0, 3]) == Exception
print("Todos os testes OK!")