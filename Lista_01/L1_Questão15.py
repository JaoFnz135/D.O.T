'''Lista1_q15. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)'''
    
def valor(n):
    s = 0
    for i in range(1, n+1):
        s += (i**2+1)/(i+3)
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