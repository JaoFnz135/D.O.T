'''8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
ocorreu a letra ‘A’.
OBS: Fazer crítica na entrada do caractere para aceitar somente letras.'''

def letraA(l):
    cont = 0
    for i in l:
        if i == 'A':
            cont += 1
        else:
            pass
    return cont

def main():
    l = []
    while True:
        try:
            for i in range(10):
                letra = input(f'Informe um caractere alfabético para a lista: ').upper()[0]
                if letra.isalpha():
                    l.append(letra)
                else:
                    raise ValueError   
            
            print(f'\nA letra "A" aparece {letraA(l)} vezes na lista criada.')
            break
        except:
            print('Erro, tente novamente.')

if __name__ == '__main__':
    main()