'''9. Faça uma função que recebe um valor inteiro e verifica se o valor é par ou
ímpar. A função deve retornar um valor booleano.'''

def par_ou_impar(n):
    if type(n) != int:
        return Exception
    if n % 2 == 0:
        return True
    elif n % 2 != 0:
        return False

assert par_ou_impar(2) == True
assert par_ou_impar(100) == True
assert par_ou_impar(22) == True
assert par_ou_impar(1) == False
assert par_ou_impar(101) == False
assert par_ou_impar(23) == False
assert par_ou_impar(-23) == False
assert par_ou_impar(-199) == False
assert par_ou_impar(-2) == True
assert par_ou_impar(-100) == True
assert par_ou_impar(0) == True
assert par_ou_impar('A') == Exception
assert par_ou_impar(1.5) == Exception
assert par_ou_impar(True) == Exception
print('Todos os teste ok!')