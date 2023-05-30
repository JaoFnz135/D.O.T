'''Lista1_q1. Faça uma função que recebe um número inteiro pôr parâmetro e retorna verdadeiro se ele for par e falso se for impar.'''

def par_impar(n):
    return n % 2 == 0


def main():
    while True:
        try:
            num = int(input('Digite um número: '))
            if par_impar(num) == True:
                print(f'O número {num} é par.')
            else:
                print(f'O número {num} é impar.')
            break
        except:           
            print('Caractere inválido. Tente novamente.')

if __name__=='__main__':
    main()