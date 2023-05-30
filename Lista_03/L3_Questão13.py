'''13. Faça uma função que recebe, por parâmetro, a hora de inicio e a hora de
término de um jogo, ambas subdivididas em 2 valores distintos: horas e minutos.
O procedimento deve retornar, também por parâmetro, a duração do jogo em
horas e minutos, considerando que o tempo máximo de duração de um jogo é
de 24 horas e que o jogo pode começar em um dia e terminar no outro.'''

def duracao(hi, mi, hf, mf):
    # Verificação de tipo
    if type(hi) != int or type(mi) != int or type(hf) != int or type(mf) != int:
        return Exception
    if (hi < 0 or mi < 0 or hf < 0 or mf < 0) or (hi == hf and hi == mi and hi == mf):
        return Exception
    if (mi > 59 or mf > 59) or (hi > 24 or hi < 0) or (hf > 24 or hf < 0):
        return Exception
    if hf < hi:
        hf += 24
    if mi > mf:
        mf += 60
    
    hd = hf - hi
    md = mf - mi 
    return (hd, md)


assert duracao(17, 30, 20, 40) == (3, 10)
assert duracao(23, 30, 1, 40) == (2, 10)
assert duracao(2, 30, 1, 40) == (23,10)
assert duracao(2, 40, 3, 35) == (1,55)
assert duracao(4,4,4,4) == Exception
assert duracao(4,4,4,'a') == Exception
assert duracao(4,4,'b',4) == Exception
assert duracao(4,'c',4,4) == Exception
assert duracao('d',4,4,4) == Exception
assert duracao(1.2,4,4,4) == Exception
assert duracao(1, 4, 2.5, 4) == Exception
assert duracao(1, 4, 4, 10.5) == Exception
assert duracao(3, 4, 4.3, 4) == Exception
assert duracao(3, 4, 43, 4) == Exception
assert duracao(30, 4, 4, 4) == Exception
assert duracao(3, 4, 4, 60) == Exception
assert duracao(3, 60, 4, 5) == Exception
print('Todos os teste ok!')