'''9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.'''

def main():
    lx = []
    while True:
        try:
            for i in range(5):
                lx.append(int(input('Digite um número: ')))
            lx.reverse()
            ly = lx
            print(ly)

        except:
            print('Erro, tente novamente.', end=" ")

if __name__ == '__main__':
    main()
