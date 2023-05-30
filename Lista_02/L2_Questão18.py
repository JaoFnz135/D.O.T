'''18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para
uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.'''

def lista_neg(lx):
    lr = []
    for i in lx:
        if i < 0:
            lr.append(i)
        else:
            pass
    return lr

def main():
    while True:
        listax = []
        try:
            for i in range(10):
                listax.append(int(input('Informe um número inteiro: ')))
            print(f'\nLista X: {listax}')
            print(f"Lista só com os números negativos da lista X: {lista_neg(listax)}")    
        except:
            print('Houve um erro, tente novamente. ')
if __name__ == '__main__':
    main()