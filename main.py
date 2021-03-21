from automato import afd, afn


def subdividir_lista(lista, n):
    lista_subdivida = []
    for i in range(0, len(lista), n):
        linha = [str(d) for d in lista[i:i + n]]
        lista_subdivida.append(linha)
    return lista_subdivida


Q = input("Quais são os estados do autômato? ").split(' ')
Sigma = input("Qual o alfabeto do autômato? ").split(' ')

delta = dict()
for q in list(Q):
    for e in list(Sigma):
        delta[(q, e)] = input(f'Estando em {q} e lendo {e} vai para? ')

# delta = {
#     ('q1', '0'): {'q1', 'q2'},
#     ('q1', '1'): {'q1'},
#     ('q2', '0'): {'q3'},
#     ('q2', '1'): {'q3'},
#     ('q3', '0'): {'q4'},
#     ('q3', '1'): {'q4'},
# }

dados = subdividir_lista(list(delta.values()), len(Sigma))

print(dados)


def print_table(linhas, colunas, dados):
    format_row = "{:>4}" * (len(colunas) + 1)
    print(format_row.format("    |", *colunas))
    print(format_row.format("----+", *['-----' for e in colunas]))
    for linha, dados_linha in zip(linhas, dados):
        print(format_row.format(f' {linha} |', *dados_linha))


print_table(Q, Sigma, dados)

q0 = input('qual o estado inicial? ')
F = input("Quais são os estados finais? ").split(' ')
if set(F).issubset(Q):
    print('Ok')
else:
    print('Erro')


cadeia = input("Informe a Cadeia: ")

print("A cadeia foi aceita? ", end='')
print(afd(Q, Sigma, delta, 'q0', F, cadeia))


'''

Q = ['q1', 'q2', 'q3', 'q4']
Sigma = ['0', '1']

delta = {
    ('q1', '0'): {'q1'},
    ('q1', '1'): {'q1', 'q2'},
    ('q2', '0'): {'q3'},
    ('q2', '1'): {'q3'},
    ('q3', '0'): {'q4'},
    ('q3', '1'): {'q4'},
}


def subdividir_lista(lista, n):
    lista_subdivida = []
    for i in range(0, len(lista), n):
        lista_subdivida.append(lista[i:i + n])
    return lista_subdivida


dados = subdividir_lista(list(delta.values()), len(Sigma))

print(dados)


print_table(Q, Sigma, dados)

F = {'q4'}
if F.issubset(Q):
    print('Ok')
else:
    print('Erro')

a = afn(Q, Sigma, delta, 'q1', F, '01010101011110111')
print(a)
'''
