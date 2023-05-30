'''7. Faça uma função que recebe a idade de um nadador por parâmetro e retorna
a categoria desse nadador de acordo com a tabela abaixo:
Idade           Categoria
5 a 7 anos      Infantil A
8 a 10 anos     Infantil B
11-13 anos      Juvenil A
14-17 anos       Juvenil B
Maiores de 18 anos    Adulto
(inclusive)'''

def categoria(idd):
    if type(idd) != int:
        return Exception
    if idd < 5:
        return Exception    
    if idd >= 5 and idd <=7:
        return 'Infantil A'
    elif idd >= 8 and idd <=10:
        return 'Infantil B'
    elif idd >= 11 and idd <= 13:
        return 'Juvenil A'
    elif idd >= 14 and idd <= 17:
        return 'Juvenil B'
    elif idd >= 18:
        return 'Adulto'
    else:
        return Exception

assert categoria(5) == 'Infantil A'
assert categoria(10) == 'Infantil B'
assert categoria(12) == 'Juvenil A'
assert categoria(14) == 'Juvenil B'
assert categoria(18) == 'Adulto'
assert categoria(30) == 'Adulto'
assert categoria(17) == 'Juvenil B'
assert categoria(0) == Exception
assert categoria(4) == Exception
assert categoria(-1) == Exception
assert categoria('A') == Exception
assert categoria(False) == Exception
print('Todos os teste ok!')