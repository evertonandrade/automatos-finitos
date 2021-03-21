from automato import afd


def subdividir_lista(lista, n):
    lista_subdivida = []
    for i in range(0, len(lista), n):
        lista_subdivida.append(lista[i:i + n])
    return lista_subdivida


Q = input("Quais são os estados do autômato? ").split(' ')
Sigma = input("Qual o alfabeto do autômato? ").split(' ')

delta = dict()
for q in list(Q):
    for e in list(Sigma):
        delta[(q, e)] = input(f'Estando em {q} e lendo {e} vai para? ')


dados = subdividir_lista(list(delta.values()), len(Sigma))

print(dados)


def print_table(linhas, colunas, dados):
    format_row = "{:>4}" * (len(colunas) + 1)
    print(format_row.format("    |", *colunas))
    print(format_row.format("----+", *['-----' for e in colunas]))
    for team, row in zip(linhas, dados):
        print(format_row.format(f' {team} |', *row))


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
