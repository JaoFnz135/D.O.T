'''1. Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o
seu volume (v = 4/3 * PI * R ** 3).'''

def volume(r):
    if type(r) == str or r <= 0:
        return Exception
    return round(4/3 * 3.14 * r ** 3, 2)

assert volume(1.0) == 4.19
assert volume(1) == 4.19 
assert volume(0) == Exception  
assert volume('s') == Exception  
assert volume(-3) == Exception
print("Todos os testes ok!")
