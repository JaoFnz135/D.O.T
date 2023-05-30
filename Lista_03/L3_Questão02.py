'''2. Escreva uma função que recebe as 3 notas de um aluno por parâmetro e uma
letra. Se a letra for A o procedimento calcula a média aritmética das notas do
aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2). A função deve retornar
a média calculada.'''

def media(n1, n2, n3, letra):
    if (type(n1) != int and type(n1) != float) or (type(n2) != int and type(n2) != float) or (type(n3) != int and type(n3) != float):
        return Exception
    if (n1 < 0 or n1 > 10) or (n2 < 0 or n2 > 10) or (n3 < 0 or n3 > 10):
        return Exception
    if letra == 'A':
        return round((n1 + n2 + n3) / 3, 1)
    elif letra == 'P':
        return round((n1 * 5 + n2 * 3 + n3 * 2) /10, 1)
    else:
        return Exception
assert media('X', 6.8, 2.5, 'P') == Exception
assert media(5, True, 2.5, 'A') == Exception
assert media(5, -10, 2.5, 'A') == Exception
assert media(10, 8, 5, 1) == Exception
assert media(10, 8, 5, 'a') == Exception
assert media(11, 8, 5, 'A') == Exception
assert media(10, 80, 5, 'A') == Exception
assert media(11, 8, 51, 'A') == Exception
assert media(11, 8, 51, 'A') == Exception
assert media(10, 10, 10, 'A') == 10
assert media(1, 1, 1, 'A') == 1
assert media(10, 5, 6, 'A') == 7
assert media(4, 6, 7, 'A') == 5.7
assert media(5, 9.5, 10.0, 'A') == 8.2
assert media(10, 10, 10, 'P') == 10
assert media(10, 3, 5, 'P') == 6.9
assert media(0, 6.8, 2.5, 'P') == 2.5
print('Todos os teste ok!')