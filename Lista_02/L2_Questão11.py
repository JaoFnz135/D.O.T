'''11) Faça um programa que alimente uma lista com um número de posições definidas pelo
usuário.
Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
==== =MENU========
1)Cadastar nome
2)Pesquisar nome
3)Listar todos os nome
0) Sair do programa
——————–
Digite sua escolha:_'''
#Corrigir erros.
def menu():
    print("=======MENU========")
    print("1)Cadastar nome")
    print("2)Pesquisar nome")
    print("3)Listar todos os nome")
    print("0) Sair do programa")
    print("_____________________")
    while True:
        try:    
            r = int(input('\nEscolha a opção: '))
            if r >= 0 and r < 4:
                return r                
            else:
                raise ValueError
        except ValueError:
            print('Opção inválida. Por favor, digitar uma opção disponível no menu.', end=" ")
            
def cadastrar(ln, qtd):
    while True:
        try:
            for i in range(qtd):
                nome = str(input(f'Informe o {i+1}° nome a ser cadastrado: '))
                ln.append(nome)
            return ln
        except:
            print('Houve um erro, tente novamente.')        
            
def pesquisar(ln):
    while True:
        try:
            nome = input('Informe o nome que deseja pesquisar: ')
            for n in ln:
                if nome == n:
                    return nome
                else:
                    return 'Nome não encontrado.'
        except:
            print('Houve um erro, tente novamente.')
    
def main():
    lista_nomes = []
    while True:
        try:
            if menu() == 1:
                qtd = int(input('Informe quantos nomes quer cadastrar: '))
                lista_nomes = cadastrar(lista_nomes, qtd)
            elif menu() == 2:
                nome = pesquisar(lista_nomes)
                print(nome)
            elif menu() == 3:
                for i in lista_nomes:
                    print(i)
            elif menu() == 0:
                break
            else:
                raise ValueError
        except ValueError:
            print('Houve um erro, tente novamente.') 
   
if __name__ == '__main__':
    main()