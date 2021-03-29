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
