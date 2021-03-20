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

    