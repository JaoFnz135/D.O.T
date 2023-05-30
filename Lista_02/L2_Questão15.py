'''15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
por diante. Escrever todo a lista D e todo a lista E.'''
def inverter(ld):
    le = ld[::-1]
    return le

def main():
    ld = []
    while True:
        try:
            for i in range(10):
               ld.append(int(input('Digite um número: ')))
            
            print(f'\n{ld}')
            print(f"{inverter(ld)}")
            break
        except:
            print('Erro, tente novamente.', end=" ")

if __name__ == '__main__':
    main()
