'''17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o
valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V
aparece.
Caso o valor V não ocorra nenhuma vez na lista W, escrever uma mensagem informando isto.'''

def verificacao(lw):
    while True:
        try:
            posicoes = []
            cont = 0
            vlr = float(input('\nDigite o  valor que quer verificar na lista: '))
            for i in range(len(lw)):
                if lw[i] == vlr:
                    cont += 1
                    posicoes.append(i+1)
                else:
                    pass
            return f'\nO valor {vlr} apareceu na lista-w {cont} vezes, nas seguintes posições: {posicoes}' if cont > 0 else f'O valor {vlr} não apareceu na lista-w.'       
        except:
            print('Houve um erro, tente novamente.')
            
def main():
    while True:
        try:
            listaw = []
            for i in range(10):
                elemento = float(input(f'Informe o {i+1}º elemento da lista-W: '))
                listaw.append(elemento)
            print(verificacao(listaw))
            break
        except:
            print('Por favor, digitar um valor númerico.')
            
if __name__ == '__main__':
    main()
