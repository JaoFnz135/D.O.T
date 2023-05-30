'''10) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra.'''

def main():
    while True:
        try:
            l = []
            for i in range(15):
                num = int(input('Digite um número: '))
                l.append(num)
            print(l)
            maior = max(l)
            print(f'\nO maior elemento da lista é: {maior} \nPosição na lista: {l.index(maior)}')
            menor = min(l)
            print(f'\nO menor elemento da lista é: {menor} \nPosição na lista: {l.index(menor)}')
            break
        except ValueError:
            print('Erro, tente novamente.', end=" ")


if __name__ == '__main__':
    main()
