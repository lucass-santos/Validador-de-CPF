"""
Gerador de CPF
"""

from random import randint
teste = str(randint(100000000, 999999999))
print(teste)

cpf_verificado = teste

lista, soma = [], 0
for indice, numero in enumerate(range(10, 1, -1)):
    lista.append(int(cpf_verificado[indice]) * numero)
    soma += lista[indice]

digito1 = '0' if (11 - (soma % 11)) > 9 else str(11 - (soma % 11))
cpf_verificado += digito1

lista, soma = [], 0

for indice, numero in enumerate(range(11, 1, -1)):
    lista.append(int(cpf_verificado[indice]) * numero)
    soma += lista[indice]

digito2 = '0' if (11 - (soma % 11)) > 9 else str(11 - (soma % 11))
cpf_verificado += digito2

print(cpf_verificado)