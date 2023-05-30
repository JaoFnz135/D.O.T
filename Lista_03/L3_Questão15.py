'''15. A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes,
coletando dados sobre o salário e número de filhos. Faça uma função que leia
esses dados para um número não determinado de pessoas e retorne a média de
salário da população, a média do número de filhos, o maior salário e o percentual
de pessoas com salário até R$ 350,00.'''

def pesquisa_estatisticas():
    slr_total = 0
    filhos_totais = 0
    max_salario = 0 
    slr_menor_350 = 0 
    num_pessoas = 0
    
    while True:
        salario = round(float(input('Informe o salário da pessoa [0-Encerrar]: ')), 2)
        if salario == 0:
            break
        filhos = int(input('Informe o número de filhos da pessoa: '))
        
        filhos_totais += filhos
        slr_total += salario
        num_pessoas += 1
        
        if salario > max_salario:
            max_salario = salario
        if salario <= 350.00:
            slr_menor_350 += 1
            
    med_salario = round(slr_total / num_pessoas, 2)
    med_filhos = round(filhos_totais / num_pessoas, 2)
    pct_ate_350 = round((slr_menor_350/num_pessoas) * 100, 1)
    
    print(f'\nmedia salarios: {med_salario}\nMedia filhos: {med_filhos}\nMax: {max_salario}\nmenor de 350: {pct_ate_350}')
    return (med_salario, med_filhos, max_salario, pct_ate_350)


assert pesquisa_estatisticas() == (1295.65, 0.8, 3500.00, 40)
print('Todos os teste ok!')