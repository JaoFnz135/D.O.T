'''5) Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os
elementos deste em uma outra lista de 20 elementos.'''
import random

def main():
    l1 = []
    l2 = []
    l3 = []
    for i in range(10):
        l1.append(random.randint(1, 100))
        l2.append(random.randint(1, 100))
    for i in range(10):
        l3.append(l1[i])
        l3.append(l2[i])
        
    print(f'\nLista 1: {l1}\nLista 2: {l2}\nLista 3: {l3}')
        
    
    
    pass

if __name__ == '__main__':
    main()