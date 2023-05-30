'''Lista1_q11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.'''

def divisores(n):
    quant = 0
    for i in range(1, n):
        d = n % (i+1)
        if d == 0:
            quant += 1
    return quant        

def main():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
            print(f'\nO número {n} têm {divisores(n)} divisores.')
            break
        except:
            print('Houve um erro. Tente novamente.')

if __name__ == '__main__':
    main()    