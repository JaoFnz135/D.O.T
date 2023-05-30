'''2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
de números negativos e a soma dos números positivos dessa lista.'''

def negativos(l):
    cont = 0
    for i in l:
        if i < 0:
            cont += 1
    return cont
def soma(l):
    soma = 0 
    for i in l:
        if i >= 0:
            soma += i
    return soma

def main(): 
    l = []
    while True:
        try:
            for i in range(10):
                n = float(input(f'Digite um número real[{i+1}/10]: '))
                l.append(n)
            neg = negativos(l)
            s = soma(l)
            print(f'\nQuantidade de números negativos: {neg} \nSoma dos números positivos: {s}')   
            break
        except:
            print('Houve um erro. Tente novamente.', end=" ")     

if __name__ == '__main__':
    main()