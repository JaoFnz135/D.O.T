'''Lista1_q3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar
o valor correspondente em graus Celsius.
Fórmula: C = ((F-32)/9)*5'''

def celsius(f):
    return ((f - 32) / 9) * 5

def main():
    while True:
        try:
            f = int(input('Digite a temperatura em graus Fahrenheit: '))

            print(f'\nA temperatura de {f} °F convertida para celsius é igual a {celsius(f):.2f}')
            break
        except:
            print('Caractere inválido. Tente novamente.')



if __name__ == '__main__':
    main()