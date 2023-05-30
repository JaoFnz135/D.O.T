'''10. Faça uma função que recebe a média final de um aluno por parâmetro e
retorna o seu conceito, conforme a tabela abaixo:
Nota            Conceito
de 0,0 a 4,9     D
de 5,0 a 6,9     C
de 7,0 a 8,9     B
de 9,0 a 10,0    A'''

def conceito(med):
    if type(med) != float or med < 0:
        return Exception    
    if med >= 0.0 and med <= 4.9:
        return 'D'
    elif med >= 5.0 and med <= 6.9:
        return 'C'
    elif med >= 7.0 and med <= 8.9:
        return 'B'
    elif med >= 9.0 and med <= 10.0:
        return 'A'


assert conceito(7.5) == 'B'
assert conceito(4.9) == 'D'
assert conceito(9.0) == 'A'
assert conceito(6.9) == 'C'
assert conceito(6.9) == 'C'
assert conceito(9.5) == 'A'
assert conceito(0.0) == 'D'
assert conceito(0) == Exception
assert conceito(10) == Exception
assert conceito(-1) == Exception
assert conceito(True) == Exception
assert conceito('A') == Exception
print('Todos os teste ok!')