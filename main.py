from automato import Automato
from colorama import Fore, Style


meu_automato = Automato()
meu_automato.Q = input(f'Quais são os estados do autômato? ').split(' ')
meu_automato.Sigma = input(f'\nQual o alfabeto do autômato? ').split(' ')
print()
for q in meu_automato.Q:
    for e in meu_automato.Sigma:
        estado = input(f'Estando em {q} e lendo {e} vai para? ').split(' ')
        meu_automato.delta[(q, e)] = set(estado)

print(meu_automato)

meu_automato.q0 = input(f'Qual o estado inicial? ')
meu_automato.F = set(input(f'\nQuais são os estados finais? ').split(' '))

while(True):
    cadeia = input(f'\nDigite a Cadeia (p/ sair pressione apenas ENTER): ')
    if cadeia == '':
        print('\nsaindo...')
        break
    aceita = meu_automato.testar(cadeia)
    if aceita:
        print(f'{Fore.GREEN}A cadeia foi aceita{Style.RESET_ALL}')
    else:
        print(f'{Fore.RED}A cadeia foi rejeitada{Style.RESET_ALL}')
