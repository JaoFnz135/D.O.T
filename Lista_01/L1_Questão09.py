'''Lista1_q9. Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos
no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.'''

def soma(x, y):
    if x > y:
        sm = y
        for i in range(y, x+1):
            sm += i
    elif x < y:
        sm = x
        for i in range(x, y+1):
            sm += i
    else:
        sm = 0
    
    return sm
    

def main():
    while True:
        try:
            n1 = int(input('Digite o primeiro número: '))
            n2 = int(input('Digite o segundo número: '))
            s = soma(n1, n2)
            print(f'A soma dos números entre {n1} e {n2} é igual: {s}')
            break
            
        except:
            print('Houve um erro. Tente novamente.')
    


if __name__ == '__main__':
    main()    