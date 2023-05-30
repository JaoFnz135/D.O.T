'''Lista1_q4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas
notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno
foi aprovado (considere 6.0 a média mínima para aprovação).'''

def media(n1, n2):
    m = (n1 + n2)/2
    return m

def main():
    while True:
        try:
            nota1 = int(input('Digite a primeira nota do aluno: '))
            nota2 = int(input('Digite a segunda nota do aluno: '))

            m = media(nota1, nota2)

            if m >= 6:
                print(f'\nPARABÉNS! você foi aprovado! Sua média é de {m}.')
            else:
                print(f'\nnSinto-lhe informar, mas você está de RECUPERAÇÃO. Sua média foi de {m}.')
            break
        except:
            print('Nota inválida. Tente novamente.')

if __name__ == '__main__':
    main()