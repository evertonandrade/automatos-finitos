from automato import afd

Q = set(input("Quais são os estados do autômato? ").split(' '))
Sigma = set(input("Qual o alfabeto do autômato? ").split(' '))

delta = dict()
for q in list(Q):
    for e in list(Sigma):
        delta[(q, e)] = input(f'Estando em {q} e lendo {e} vai para? ')

print(delta)

q0 = input('qual o estado inicial? ')
F = input("Quais são os estados finais? ").split(' ')
if set(F).issubset(Q):
    print('Ok')
else:
    print('Erro')


cadeia = input("Informe a Cadeia: ")

print("A cadeia foi aceita? ", end='')
print(afd(Q, Sigma, delta, 'q0', F, cadeia))
