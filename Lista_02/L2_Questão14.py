'''14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0.
Escrever a lista C modificada.'''
from random import randint

def troca_valores(lc):
    lc_modificada = []
    for i in lc:
        if i < 0:
            lc_modificada.append(0)
        else:
            lc_modificada.append(i)
    return lc_modificada

def main():
    lista_c = []
    for i in range(10):
        lista_c.append(randint(-100, 100))    
    
    print(f"\n{lista_c}")
    print(troca_valores(lista_c))
    
if __name__ == '__main__':
    main()