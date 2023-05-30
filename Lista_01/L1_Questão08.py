'''Lista1_q8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o
caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um
programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os
números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.'''

def pergunta():
    while True:
        try:
            r = input('Quer continuar(S/N): ').upper()[0]
            if r == 'S' or r == 'N':
                break          
        except:
            print('Caractere inválido. Tente novamente.', end=' ')
            
    return r
def main():
    while True:
        try:
            n = int(input('Informe um número para saber seu cubo: '))
            cubo = n **3
            print(f'O cubo de {n} é: {cubo}')
            resp = pergunta()
            if resp == 'N': break
        except:
            print('Houve um erro. Tente novamente.')
            



if __name__ == '__main__':
    main()
    