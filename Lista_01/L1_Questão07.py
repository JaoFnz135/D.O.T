'''Lista1_q7. Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por
sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize
uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste
número, também do tipo inteiro.'''

def fatorial(n):
    fat = n
    for i in range(1, n):
        fat *= (n-i)
    return fat

def main():
    while True:
        try:
            num = int(input('Digite um número para saber seu fatorial: '))
            print(f'O fatorial de {num} é {fatorial(num)}.')
            break
        except:
            print('Houve um erro. Tente novamente.')


if __name__ == '__main__':
    main()