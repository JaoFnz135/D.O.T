'''12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A
prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
Para isso são dados:
o cartão gabarito;
o número de alunos da turma;
o cartão de respostas para cada aluno, contendo o seu número e suas respostas.'''

def cartao_aluno(gab):
    while True:
        try:
            qtd = int(input('Informe a quantidade de alunos: '))
            list_alunos = []
            #Candidatos
            for i in range(qtd):
                list_respostas = []
                print('Por favor, digitar como resposta: A, B, C, D ou E.')
                #Respostas
                for j in range(len(gab)):
                    while True:
                        try:
                            r = input(f'Aluno {i+1}-Questão {j+1}: ').upper()[0]
                            #r = 'B'
                            if r in 'ABCDE':
                                list_respostas.append(r)
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            print("Resposta inválida. Por favor, digitar A, B, C, D ou E como resposta.")
                list_alunos.append(list_respostas)
            return list_alunos   
        except:
            print('Erro, tente novamente.')    


def correcao(gab, cresp):
    string = f''
    for i in range(len(cresp)):
        acertos = 0
        for j in range(len(gab)):
            if gab[i] == cresp[i][j]:
                acertos += 1
            else:
                pass
        string += f'O aluno {i+1} acertou {acertos}/30 questões.\n'
    return string

def main():
    gabarito = []
    while True:
        try:
            for i in range(30):
                questr = input(f'Digite a resposta da {i+1}° questão do gabarito: ').upper()[0]
                #questr = 'A'
                if questr in 'ABCDE':
                    gabarito.append(questr)
                else:
                    ValueError
                    
            lista_alunos = cartao_aluno(gabarito)
            print(correcao(gabarito, lista_alunos))
            break     
        except ValueError:
            print('Por favor, digitar A, B, C, D ou E como resposta. Tente novamente.') 


if __name__ == '__main__':
    main()
    
    #gabarito = ["A", "E", "C", "A", "D", "E", "B", "E", "E", "E",
                #"A", "C", "B", "C", "A", "D", "B", "B", "A", "E",
                #"D", "C", "A", "D", "E", "A", "D", "B", "C", "C"]
    
    #cartao_resp = ["A", "E", "C", "A", "D", "E", "B", "E", "E", "E",
                #"A", "C", "B", "C", "A", "D", "B", "B", "A", "E",
                #"D", "C", "A", "D", "E", "A", "D", "B", "C", "C"]