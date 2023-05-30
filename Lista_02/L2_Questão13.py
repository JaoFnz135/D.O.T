'''13) Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o
lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de
cada face.'''
from random import randint

def ocorrencia(lresult, l):
    f1 = f2 = f3 = f4 = f5 = f6 = 0
    qtd_face = f''
    for face in lresult:
        if face == 1:
            f1 += 1
        elif face == 2:
            f2 += 1
        elif face == 3:
            f3 += 1
        elif face == 4:
            f4 += 1
        elif face == 5:
            f5 += 1
        else:
            f6 += 1
    qtd_face = f'\nFace 1:{f1}/{l}\nFace 2:{f2}/{l}\nFace 3:{f3}/{l}\nFace 4:{f4}/{l}\nFace 5:{f5}/{l}\nFace 6:{f6}/{l}'
    return  qtd_face
         
    pass

def lancamento(n):
    resultado = []
    for i in range(n):
        face = randint(1, 6)
        resultado.append(face)
    ocorrencia_face = ocorrencia(resultado, n)
    return ocorrencia_face

def main():
    while True:
        try:
            n = int(input("Informe quantas vezes quer lançar o dado: "))
            if n != 0 and n > 0 and n != float:
                lresult = lancamento(n)
                print(lresult)
                break
            else:
                raise ValueError 
        except ValueError:
            print('Houve um erro. Tente novamente.')    
    

            pass


if __name__ == '__main__':
    main()
