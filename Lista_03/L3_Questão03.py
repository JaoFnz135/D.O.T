'''3. Faça uma função que recebe por parâmetro um valor inteiro e positivo e
retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso
contrário.'''

def primo(n):
    mult = 0
    if type(n) != int or n <= 1:
        return Exception
    for i in range(2, n):
        if n % i == 0:
            mult += 1
    if mult == 0:
        return True
    else:
        return False

assert primo(2) == True
assert primo(3) == True
assert primo(19) == True 
assert primo(349) == True
assert primo(4) == False
assert primo(8) == False
assert primo(6) == False
assert primo(1) == Exception
assert primo(0) == Exception
assert primo(-1) == Exception
assert primo('E') == Exception
assert primo(True) == Exception
print('Todos os teste ok!')