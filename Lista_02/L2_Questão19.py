'''19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos
cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos
de S. Escrever a lista X.'''

def combinacao(lr, ls):
    return lr+ls

def main():
    while True:
        listaR = []
        listaS = []
        try:
            for i in range(5):
                listaR.append(int(input(f'Informe o {i+1}° número da lista-R: ')))
            for i in range(10):
                listaS.append(int(input(f'Informe o {i+1}° número da lista-S: ')))
            print(combinacao(listaR,listaS))               
            break 
        except:
            print('Houve um erro, tente novamente.')

if __name__ == '__main__':
    main()