'''4. Faça uma função que recebe por parâmetro o tempo de duração de um
processo em uma fábrica expressa em segundos e retorna também por
parâmetro esse tempo em horas, minutos e segundos.'''

def tempo(seg):
    if type(seg) != int or seg <= 0:
        return Exception
    hora = seg // 3600
    min = (seg % 3600) // 60
    seg = (seg % 3600) % 60
    return (hora, min, seg)

# Retornar tuplas
assert tempo(3600) == (1,0,0)
assert tempo(1) == (0,0,1)
assert tempo(60) == (0,1,0)
assert tempo(723678) == (201,1,18)
assert tempo(0) == Exception
assert tempo('a') == Exception
assert tempo(-1) == Exception
assert tempo(3200.50) == Exception
print('Todos os teste ok!')