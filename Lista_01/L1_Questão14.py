'''Lista1_q14. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 1 + 1/1! + ½! + 1/3! + 1 /N!'''

def fatorial(n):
    fat = n
    for i in range(1, n):
        fat *= (n-i)
    return fat

def valor(n):
    s = 1
    for i in range(1, n+1):
        s += (1/(fatorial(i)))
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