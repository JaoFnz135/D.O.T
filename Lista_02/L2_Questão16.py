'''16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os
elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os
elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
Escrever as listas X e Y.'''

def modificacao(lx):
    ly = []
    for elemento in lx:
        if lx.index(elemento) % 2 == 0:
            elemento = lx[lx.index(elemento)] / 2
            ly.append(elemento)
        else: 
            elemento = lx[lx.index(elemento)] * 3
            ly.append(elemento)             
    return ly

def main():
    while True:
        try:
            listax = []
            for i in range(10):
                listax.append(int(input('Digite um número: ')))
            
            print(listax)
            print(modificacao(listax))
            
        except:
            print()    


if __name__ == '__main__':
    main()