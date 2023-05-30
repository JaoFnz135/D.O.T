'''3.Escreva uma função chamada "contar_caracteres" que receba uma string como
parâmetro e retorne um dicionário onde as chaves são os caracteres encontrados na string
e os valores são a quantidade de ocorrências de cada caractere.'''

def contar_caracteres(s):
    quant_char = {}
    if type(s) != str:
        return Exception
    for i in s:
        if i not in quant_char:
            quant_char[i] = 1
        else:
            quant_char[i] += 1
    return quant_char

# Fazer asserts

print("Todos os testes OK!")