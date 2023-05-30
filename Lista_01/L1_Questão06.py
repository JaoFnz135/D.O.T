'''Lista1_q6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
- Se o número de lados for igual a 5, escrever PENTÁGONO.
Observação: Considere que o usuário só informará os valores 3, 4 ou 5.'''

def lados():
    while True:
        try:
            l = int(input('Digite o número de lados: '))
            if l == 3 or l == 4 or l == 5: break
        except:
            print('Houve erro. Tente novamente.')      
    return l
  
def med_lado(l):
    
    while True:
        try:
            ml = float(input('Informe a medida dos lados em cm(centimetro): '))
            break
        except:
            print('Houve erro. Tente novamente.')
    return ml


def main():
    l = lados()
    ml = med_lado(l)
    if l == 3:
        per = l * ml 
        print(f'\nÉ um TRIÂNGULO com perimetro de {per} cm.')
    elif l == 4:
        a = ml ** 2
        print(f'\nÉ um QUADRADO de área de {a} cm².')
    elif l == 5:
        print(f'\nÉ um PENTÁGONO.')



if __name__ == '__main__':
    main()