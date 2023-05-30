'''4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra.'''
import random

def main():
    l = []
    for i in range(15):
        l.append(random.randint(1, 1000))
    print(f"{l}")    
    maior = max(l)
    print(f'\nO maior número da lista: {maior} \nPosição do número: {l.index(maior)}')
    menor = min(l)
    print(f'\nO maior número da lista: {menor} \nPosição do número: {l.index(menor)}')

if __name__ == '__main__':
    main()