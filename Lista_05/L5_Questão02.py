'''2.Crie uma função chamada "verificar_anagrama" que receba duas strings como
parâmetros e retorne True se as duas strings forem anagramas (ou seja, possuírem as
mesmas letras em quantidade igual, mas em ordem diferente), e False caso contrário.'''

def verificar_anagrama(s1, s2):
    if type(s1) != str or type(s2) != str:
        return Exception
    anagrama = True
    if len(s1) == len(s2):
        for i in s1:
            if i in s2:
                continue
            else:
                anagrama = False
        return anagrama
    else:
        return False

assert verificar_anagrama('amor','roma') == True
assert verificar_anagrama('iracema','america') == True
assert verificar_anagrama('estudo','duetos') == True
assert verificar_anagrama('alegria','alergia') == True
assert verificar_anagrama('lobo','bolo') == True
assert verificar_anagrama('ouro', 'bola') == False
assert verificar_anagrama('morte','vidas') == False
assert verificar_anagrama('traste','triste') == False
assert verificar_anagrama('alegria','tristeza') == False
assert verificar_anagrama('morte', 2) == Exception
assert verificar_anagrama( 1.5 , 'bola') == Exception
assert verificar_anagrama('morte', True) == Exception
print("Todos os testes OK!")