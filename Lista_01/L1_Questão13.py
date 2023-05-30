'''Lista1_q13. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/N.'''

def valor(n):
    s = 1
    for i in range(1, n+1):
        s += (1/(i+1))
    return s
    

def main():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
            s = valor(n)
            print(f'O valor de S é: {s:.2f}')
            break            
        except:
            print('Houve um erro. Tente novamente.')
    
    
    
if __name__ == '__main__':
    main()