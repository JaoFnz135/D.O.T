'''7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
outro valor dado pertence ou não à lista.'''

def main():
    l = [range(10)]
    while True:
        try:
            for i in range(10):
                l.append(int(input('Informe um valor: ')))
            n = int(input('\nInforme um número para verificação: '))
            if n in l:
                print(f'\nO número {n} pertence a lista.')
                break
            else:
                print(f'\nO número {n} não pertence a lista.')
                break
        except:
            print('Erro, tente novamente.')


if __name__ == '__main__':
    main()
