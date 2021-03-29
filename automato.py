from utils import *


class Automato:
    def __init__(self):
        self.Q = list()
        self.Sigma = list()
        self.delta = dict()
        self._q0 = ''
        self._F = set()

    @property
    def q0(self):
        return self.q0

    @q0.setter
    def q0(self, value):
        if value in self.Q:
            self._q0 = value
        else:
            raise ValueError(
                'O estado inical deve estar contido nos estados do autômato'
            )

    @property
    def F(self):
        return self._F

    @F.setter
    def F(self, value):
        if value.issubset(self.Q):
            self._F = value
        else:
            raise ValueError(
                'O conjunto de estados finais deve ser subconjunto dos estados do autômato'
            )

    def tipo(self):
        estados = self.delta.values()
        for e in estados:
            if len(e) > 1:
                return 'AFN'
        return 'AFD'

    def cadeia_valida(self, cadeia):
        for s in cadeia:
            if s not in self.Sigma:
                raise Exception(
                    'A cadeia contem simbolos que não pertencem ao alfabeto do autômato'
                )

    def afd(self, cadeia):
        qA = self._q0
        for s in cadeia:
            proximo_estado = self.delta[(qA, s)]
            qA = ''.join(proximo_estado)
        return qA in self._F

    def testar(self, cadeia):

        self.cadeia_valida(cadeia)
        if self.tipo() == 'AFD':
            return self.afd(cadeia)
        elif self.tipo == 'AFN':
            ...

    def __str__(self):
        dados = subdividir_lista(list(self.delta.values()), len(self.Sigma))
        print()
        print_table(self.Q, self.Sigma, dados)
        return f'Tabela de transições do {self.tipo()} \n'
