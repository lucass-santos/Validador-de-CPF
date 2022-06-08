"""
Programa para verificar CPF
"""

cpf = input('Digite o cpf: ')

while not cpf.isnumeric() or len(cpf) != 11:
    print('Digite apenas números para informar o cpf e certifique-se de ter 11 dígitos')
    cpf = input('Pode digitar o cpf novamente: ')

cpf_sem_digito = cpf[:9]
lista, soma = [], 0
for indice, numero in enumerate(range(10, 1, -1)):
    lista.append(int(cpf_sem_digito[indice]) * numero)
    soma += lista[indice]

digito1 = '0' if (11 - (soma % 11)) > 9 else str(11 - (soma % 11))
cpf_sem_digito += digito1

for indice, numero in enumerate(range(11, 1, -1)):
    lista.append(int(cpf_sem_digito[indice]) * numero)
    soma += lista[indice]

digito2 = '0' if (11 - (soma % 11)) > 9 else str(11 - (soma % 11))
cpf_sem_digito += digito2

print("Cpf válido!") if cpf_sem_digito == cpf else print('Cpf inválido!!!')
