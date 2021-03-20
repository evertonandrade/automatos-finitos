from automato import afd

Q = set(input("Quais são os estados do autômato? ").split(' '))
Sigma = set(input("Qual o alfabeto do autômato? ").split(' '))

delta = dict()
data = []
for q in list(Q):
    linha = []
    for e in list(Sigma):
        valor = input(f'Estando em {q} e lendo {e} vai para? ')
        delta[(q, e)] = valor
        linha.append(valor)
    data.append(linha)


def print_table(linhas, colunas, dados):
    format_row = "{:>4}" * (len(colunas) + 1)
    print(format_row.format("    |", *colunas))
    print(format_row.format("----+", *['-----' for e in colunas]))
    for team, row in zip(linhas, dados):
        print(format_row.format(f' {team} |', *row))


print_table(Q, Sigma, data)

q0 = input('qual o estado inicial? ')
F = input("Quais são os estados finais? ").split(' ')
if set(F).issubset(Q):
    print('Ok')
else:
    print('Erro')


cadeia = input("Informe a Cadeia: ")

print("A cadeia foi aceita? ", end='')
print(afd(Q, Sigma, delta, 'q0', F, cadeia))
