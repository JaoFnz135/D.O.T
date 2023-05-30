'''Lista1_q2. Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área
do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo.
Área = PI * r2; Perímetro = PI * 2 * r;'''

def area(r):
    pi = 3.14
    a = pi * r **2
    return a


def perimetro(r):
    pi = 3.14
    p = 2 * pi * r
    return p

def main():
    raio = int(input('Digite o valor do raio: '))
    
    print(f'\nA área do circulo é: {area(raio)} \nO perimetro do circulo é: {perimetro(raio):.2f}')
    

if __name__=='__main__':
    main()