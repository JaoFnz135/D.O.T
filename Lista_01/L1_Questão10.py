'''Lista1_q10. Escreva um programa composto de uma função Max e o programa principal como segue:
a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer um
deles;
b) O programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a função
Max'''

def maior(a, b, c, d):
    maior = a
    if b > a and b > c and b > d:
        maior = b
    elif c > a and c > b and c > d:
        maior = c
    elif d > a and d > b and d > c:
        maior = d
    elif a == b and a == c and a == d:
        maior = a
    return maior

def main():
    while True:
        try:
            for i in range(4):
                n1 = int(input(f'\nInforme o primeiro número da lista({i+1}/4): '))
                n2 = int(input(f'Informe o segundo número da lista({i+1}/4): '))
                n3 = int(input(f'Informe o terceiro número da lista({i+1}/4): '))
                n4 = int(input(f'Informe o quarto número da lista({i+1}/4): '))
                print(f'\n{maior(n1, n2, n3, n4)}')
            break
        except:
            print('Houve um erro. Tente novamente.')

if __name__ == '__main__':
    main()    