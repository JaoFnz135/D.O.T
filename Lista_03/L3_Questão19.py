'''19. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e
retorna o número de divisores desse valor.'''

def cont_divisores(vlr):
    if type(vlr) != int or vlr <= 0:
        return Exception
    else:
        qtd_div = 0
        for i in range(1, vlr + 1):
            if vlr % i == 0:
                qtd_div += 1
            else: continue
    return qtd_div

assert cont_divisores(4) == 3
assert cont_divisores(20) == 6
assert cont_divisores(10) == 4
assert cont_divisores(2) == 2
assert cont_divisores('3') == Exception
assert cont_divisores(2.5) == Exception
assert cont_divisores(True) == Exception
assert cont_divisores(None) == Exception
assert cont_divisores(0) == Exception
print('Todos os teste ok!')