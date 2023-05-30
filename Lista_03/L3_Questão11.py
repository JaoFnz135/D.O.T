'''11. Faça uma função que recebe, por parâmetro, a altura e o sexo de uma
pessoa e retorna o seu peso ideal. Para homens, calcular o peso ideal usando a
fórmula peso ideal = 72.7 * altura - 58 e, para mulheres, peso ideal = 62.1 * altura
- 44.7.'''

def peso_ideal(alt, sx):
    if type(alt) != float or type(sx) != str or alt <= 0:
        return Exception
    if sx == 'M':
        return round(72.7 * alt - 58, 1)
    elif sx == 'F':
        return round(62.1 * alt - 44.7, 1)
    else:
        return Exception

assert peso_ideal(1.79, 'M') == 72.1
assert peso_ideal(1.79, 'F') ==  66.5
assert peso_ideal(1.50, 'F') ==  48.5
assert peso_ideal(1.50, 'M') ==  51.1
assert peso_ideal(1.82, 'M') ==  74.3
assert peso_ideal(1.75, 'F') ==  64.0
assert peso_ideal(1.75, 'J') ==  Exception
assert peso_ideal(175, 'F') ==  Exception
assert peso_ideal(1.75, 10) ==  Exception
assert peso_ideal(1.75, True) ==  Exception
assert peso_ideal(False, 'F') ==  Exception
assert peso_ideal(0, 'F') ==  Exception
assert peso_ideal(0.0, 'M') ==  Exception
assert peso_ideal(-1.5, 'X') ==  Exception
assert peso_ideal(1.5, -10) ==  Exception
print('Todos os teste ok!')
#type(alt) != float or 