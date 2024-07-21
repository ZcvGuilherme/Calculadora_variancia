import os
from time import sleep
#x = media dos elementos
#variancia =    a^2 = ((x1 - x)^2 + (x2 - x)^2 + ... + (xn - x)^2) / n

#desvio padrao = variancia ** (1/2)
def limpa_tela():
    os.system('cls') or None
def create_variable(var_dict, var_name, value):
    var_dict[var_name] = value

lista = []
# Dicionário para armazenar as variáveis
variables = {}
variable2 = {}
#solicitar valores
entrada = input("Digite os valores separados por vírgula: ")
valores = [int(valor.strip()) for valor in entrada.split(',')]
# Criando variáveis
for i, valor in enumerate(valores, start=1):
    var_name = f'var_{i}'
    create_variable(variables, var_name, valor)
# Acessando as variáveis
#for chave, valor in variables.items():
#    print(chave, valor)
#fazendo a media
for chave, valor in variables.items():
    lista.append(valor)
quantidade = len(lista)
soma = sum(lista)
media = soma/quantidade

for chave, valor in variables.items():
    n = valor - media
    n **= 2
    create_variable(variable2, chave, n)

soma_dos_valores = sum(variable2.values())
variancia = soma_dos_valores/quantidade

desvio_padrao = variancia**1/2

limpa_tela()
print(f'média dos valores: {media:.2f}\nvariância: {variancia:.2f}\ndesvio padrão: {desvio_padrao:.2f}')
sleep(3)

