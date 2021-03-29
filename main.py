from automato import Automato


meu_automato = Automato()
meu_automato.Q = input("Quais são os estados do autômato? ").split(' ')
meu_automato.Sigma = input("Qual o alfabeto do autômato? ").split(' ')

for q in meu_automato.Q:
    for e in meu_automato.Sigma:
        estado = input(f'Estando em {q} e lendo {e} vai para? ').split(' ')
        meu_automato.delta[(q, e)] = set(estado)

print(meu_automato)

meu_automato.q0 = input('qual o estado inicial? ')
meu_automato.F = set(input("Quais são os estados finais? ").split(' '))

cadeia = input("Informe a Cadeia: ")

aceita = meu_automato.testar(cadeia)
if aceita:
    print('A cadeia foi aceita :)')
else:
    print('A cadeia não foi aceita :(')
