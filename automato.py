def afd(Q, Sigma, delta, q0, F, cadeia):
    qA = q0
    for s in cadeia:
        qA = delta[(qA, s)]
    return qA in F

