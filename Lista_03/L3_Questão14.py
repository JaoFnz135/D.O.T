'''14. Escreva uma função que recebes 3 valores reais X, Y e Z e que verifique se
esses valores podem ser os comprimentos dos lados de um triângulo e, neste
caso, retornar qual o tipo de triângulo formado. Para que X, Y e Z formem um
triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento
de cada lado de um triângulo é menor do que a soma do comprimento dos outros
dois lados. O procedimento deve identificar o tipo de triângulo formado
observando as seguintes definições:
o Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
o Triângulo Isósceles: os comprimentos de 2 lados são iguais.
o Triângulo Escaleno: os comprimentos dos 3 lados são diferentes.'''

def tp_tringulo(x, y, z):
    if type(x) != float or type(y) != float or type(z) != float:
        return Exception
    if (x > y + z) or (y > x + z) or (z > y + x) or (x <= 0.0 or y <= 0.0 or z <= 0):
        return Exception
    if x == y and x == z and z == y:
        return "Triângulo Equilátero"
    elif (x != y and y == z) or ( y != x  and x == z) or ( z != x and x == y):
        return "Triângulo Isóceles"
    elif x != y and x != z and z != y:
        return "Triângulo Escaleno"
    else:
        return Exception

assert tp_tringulo(1.0, 1.0, 1.0) == "Triângulo Equilátero"
assert tp_tringulo(1.1, 1.0, 1.0) == "Triângulo Isóceles"
assert tp_tringulo(1.0, 1.1, 1.0) == "Triângulo Isóceles"
assert tp_tringulo(1.0, 1.0, 1.1) == "Triângulo Isóceles"
assert tp_tringulo(1.0, 1.2, 1.4) == "Triângulo Escaleno"
assert tp_tringulo(-1.0, 1.2, 1.4) == Exception
assert tp_tringulo(1.0, -1.2, 1.4) == Exception
assert tp_tringulo(1.0, 1.2, -1.4) == Exception
assert tp_tringulo(10, 1.2, 1.4) == Exception
assert tp_tringulo(1.0, 12, 1.4) == Exception
assert tp_tringulo(1.0, 1.2, 14) == Exception
assert tp_tringulo(1.0, 1.2, 'a') == Exception
assert tp_tringulo(1.0, 'b', 4.2) == Exception
assert tp_tringulo('a', 1.4 , 4.2) == Exception
assert tp_tringulo(1.5, 1.4 , False) == Exception
assert tp_tringulo(1.5, True, 1.4) == Exception
assert tp_tringulo(False, 1.4 , 5.5) == Exception
assert tp_tringulo(0, 0, 0) == Exception
assert tp_tringulo(0.0, 0.0, 0.0) == Exception
print('Todos os teste ok!')