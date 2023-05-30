'''Lista1_q5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e
que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
- para homens : (72.7 * h) – 58
- para mulheres : (62.1 * h) – 44.7
Observação: Altura = h (na fórmula acima).'''

def peso_ideal(h, s):
    if s == 1:
        return (62.1 * h) - 44.7
    else:
        return (72.7 * h) - 58

def altura():
    while True:
        try:
            h = float(input('Informe sua altura: '))
            break
        except:
            print('Houve um erro. Tente novamente.')
    return h

def sexo():
    s = 0
    while True:
        try:
            print('Informe qual é o seu sexo: 1 - Feminino ou 2 - Masculino')
            s = int(input('=> '))
            if s == 1 or s == 2: 
                break
        except:
            print('Houve um erro. Tente  novamente.')
        
    return s

def main():
    a = altura()
    s = sexo()
    p = peso_ideal(a, s)

    print(f'\nO seu peso ideal é {p:.2f} Kg.')



if __name__ == '__main__':
    main()