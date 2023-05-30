'''1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
a) Mostre a quantidade de números pares;
b) Grave uma lista somente com os números pares e mostre a lista;
c) Mostre a quantidade de números ímpares;
d) Grave uma lista somente com os números ímpares e mostre a lista.'''
import random

def par(l):
    lpar = []
    cont = 0
    for i in l:
        if i % 2 == 0:
            cont += 1
            lpar.append(i)
        else:
            pass
    return lpar, cont
        
def impar(l):
    list_impar = []
    cont = 0
    for i in l:
        if i % 2 != 0:
            cont += 1
            list_impar.append(i)
        else:
            pass
    return list_impar, cont        

def main():
    l = []
    for i in range(100):
        l.append(random.randint(1, 1000))
        
    listp, qtd_par = par(l)
    listimp, qtd_impar = impar(l)
        
    print(f'\nQuantidade de Números pares na lista: {qtd_par}\nLista de números pares: \n{listp}\n\nQuantidade de Números impares na lista: {qtd_impar}\nLista de números impares: \n{listimp}')
        
if __name__ == '__main__':
    main()