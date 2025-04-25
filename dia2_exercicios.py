# DIA 2 - ESTUDOS DE PYTHON
# Tipos primitivos, entradas de dados, operações, conversões e testes de tipos

# ======================
# Entrada simples e testes de string
n = input('Digite algo: ')
print('É um número?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('Só tem espaços?', n.isspace())
print('É alfanumérico?', n.isalnum())
print('Está em maiúsculas?', n.isupper())
print('Está em minúsculas?', n.islower())
print('Está capitalizada?', n.istitle())
print('O tipo primitivo é', type(n))

print('---' * 10)

# ======================
# Trabalhando com tipos primitivos

# Conversão para int
numero_inteiro = int(input('Digite um número inteiro: '))
print('Você digitou o número inteiro:', numero_inteiro)
print('Tipo:', type(numero_inteiro))

# Conversão para float
numero_decimal = float(input('Digite um número decimal: '))
print('Você digitou o número decimal:', numero_decimal)
print('Tipo:', type(numero_decimal))

# Conversão para str
texto = str(numero_inteiro)
print('Convertendo o número inteiro para texto:', texto)
print('Tipo:', type(texto))

# Conversão para bool
valor_booleano = bool(numero_inteiro)
print('Convertendo o número inteiro para booleano:', valor_booleano)
print('Tipo:', type(valor_booleano))

print('---' * 10)

# ======================
# Operação matemática simples com entrada de dados
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
