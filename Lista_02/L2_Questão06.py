'''6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
e quantos faturamentos estão abaixo da média.'''
import random

def faturamento(q, p):
    fat = 0
    lfat = []
    total = 0
    print("Faturamento dos produtos:")
    for i in range(20):
        fat = q[i] * p[i]
        lfat.append(fat)
        print(f'Produto {i+1}: R$ {fat:.2f}')
        total += fat
    print(f"\nFaturamento total: {total}")
    media = total / 20
    print(f"\nMédia do faturamento: R$ {media:.2f}\n")
    print('Faturamento abaixo da média: ')
    for i in range(20):
        if lfat[i] < media:
            print(f"Produto {i}: R$ {lfat[i]:.2f}")


def main():
    quant = [2, 7, 10, 6, 3, 14, 20, 9, 11, 4, 18, 14, 14, 6, 8, 2, 7, 18, 10, 25]
    preco = [5.00, 7.00, 2.00, 10.00, 4.00, 12.00, 5.50, 9.00, 1.50, 2.80, 15.00, 7.60, 20.00, 6.00, 18.90, 14.00, 2.00, 8.00, 5.50, 1.20]
    #quant = []
    #preco = []
    while True:
        try:
            #for i in range(20):
             #   qtd = int(input('Informe a quantidade do produto:'))
              #  prc = float(input('Informe o preço do produto: '))
               # quant.append(qtd)
                #preco.append(prc)

            faturamento(quant, preco)
            break
        except:
            print('Erro, tente novamente.')

if __name__ == '__main__':
    main()
