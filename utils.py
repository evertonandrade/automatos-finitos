def subdividir_lista(lista, n):
    lista_subdivida = []

    if len(lista) == 0 or n == 0:
        return lista_subdivida

    for i in range(0, len(lista), n):
        linha = [''.join(d) for d in lista[i:i + n]]
        lista_subdivida.append(linha)
    return lista_subdivida


def print_table(linhas, colunas, dados):
    if not linhas or not colunas or not dados:
        print()

    format_row = "{:>4}" * (len(colunas) + 1)
    print(format_row.format("    |", *colunas))
    print(format_row.format("----+", *['-----' for e in colunas]))
    for linha, dados_linha in zip(linhas, dados):
        print(format_row.format(f' {linha} |', *dados_linha))
    print(format_row.format("-----", *['-----' for e in colunas]))

