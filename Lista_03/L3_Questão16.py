'''16. Faça uma função que leia um número não determinado de valores positivos
e retorna a média aritmética dos mesmos.'''

def media(valores):
    soma = 0
    qtd_valores = len(valores)
    for valor in valores:
        if type(valor) != int or valor <= 0:
            return Exception
        else:
            soma += valor
    return soma / qtd_valores


assert media([2, 4, 6, 8, 10]) == 6.0
assert media([5]) == 5.0
assert media([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 3.0
assert media([10, 10, 10, 10]) == 10
assert media([10, 10, 10, 'a']) == Exception
assert media([10, 10, 'a', 10]) == Exception
assert media([10, 'a', 10, 10]) == Exception
assert media(['a', 10, 10, 10]) == Exception
assert media([10, 1.5]) == Exception
assert media([10, 10, 1.5]) == Exception
assert media([1.0, 10, 10, 10]) == Exception
assert media([True]) == Exception
assert media([4, -1]) == Exception
assert media([-10]) == Exception
assert media([0]) == Exception
print('Todos os teste ok!')


'''
Como não sei como os dados seriam inseridos pro teste, vou deixar esse código utilizado while aqui
e o usando o for a cima.

def media(n):
    soma = 0
    qtd_valores = 0
    while True:
        num = int(input('Informe um valor [0 - Encerrar]: '))
        if num == 0:
            break
        else:
            soma += num
            qtd_valores += 1
    return soma / qtd_valores'''