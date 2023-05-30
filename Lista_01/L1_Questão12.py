'''Lista1_q12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.'''

def somatorio(n):
    soma = 0
    for i in range(1, n+1):
        soma += (i)
    return soma


def main():
    while True:
        try:
            n = int(input('Informe um número inteiro: '))
            s = somatorio(n)        
            print(f'O valor da somatória do número {n} é igual a{s}')
            break
        except:
            print('Houve um erro. Tente novamente.')
    
if __name__ == '__main__':
    main()