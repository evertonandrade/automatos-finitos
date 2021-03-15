from automato import afd


# transições
delta = {
    ('q0', '0'): 'q0', ('q0', '1'): 'q1',
    ('q1', '0'): 'q2', ('q1', '1'): 'q1',
    ('q2', '0'): 'q1', ('q2', '1'): 'q1'
}

# conjunto de estados
Q = ['q0', 'q1', 'q2']

# conjunto de estados finais
F = ['q1']

# alfabeto
Sigma = ['0', '1']

cadeia = input("Informe a Cadeia: ")

print("A cadeia foi aceita? ", end='')
print(afd(Q, Sigma, delta, 'q0', F, cadeia))
