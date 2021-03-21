def afd(Q, Sigma, delta, q0, F, cadeia):
    """ Função que simula um autômato finito determinístico

    Args:
        Q (list): connjunto de estados
        Sigma (list): alfabeto
        delta (dict): função de transição
        q0 (str): estado inicial
        F (list): Conjunto de estados finais
        cadeia (str):  cadeia/palavra/string

    Returns:
        (bool): A cadeia é reconhecida pelo automato
    """

    qA = q0
    for s in cadeia:
        qA = delta[(qA, s)]
    return qA in F


# função que devolve o Epsilon-fechamento de um conjunto de estados
def E(estados, delta):
    S = set(estados)
    nao_explorados = list(estados)
    while len(nao_explorados) > 0:
        q = nao_explorados.pop()
        if (q, 'epsilon') in delta:
            novos = delta[(q, 'epsilon')].difference(S)
            S.update(novos)
            nao_explorados.extend(novos)
    return S


def afn(Q, Sigma, delta, q0, F, cadeia):
    QA = E({q0}, delta)
    for s in cadeia:
        novos = set()
        for q in QA:
            if (q, s) in delta:
                novos.update(E(delta[(q, s)], delta))
        QA = novos
    return len(QA.intersection(F)) != 0
