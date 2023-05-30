'''3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
leitura.'''
def main():
    while True:
        try:
            l = []
            n = int(input('Digite um número: '))
            for i in range(1, n+1):
                l.append(i)
            l.reverse()
            print(l)
            break
        except:
            print('Houve um erro. Tente novamente.', end=" ")

if __name__ == '__main__':
    main()