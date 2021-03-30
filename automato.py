from utils import print_table, subdividir_lista


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

    @property
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

    # função que devolve o Epsilon-fechamento de um conjunto de estados
    def e_fechamento(self, estados, delta):
        S = set(estados)
        nao_explorados = list(estados)
        while len(nao_explorados) > 0:
            q = nao_explorados.pop()
            if (q, 'epsilon') in delta:
                novos = delta[(q, 'epsilon')].difference(S)
                S.update(novos)
                nao_explorados.extend(novos)
        return S

    def afn(self, cadeia):
        QA = self.e_fechamento({self._q0}, self.delta)
        for s in cadeia:
            novos = set()
            for q in QA:
                if (q, s) in self.delta:
                    novos.update(self.e_fechamento(
                        self.delta[(q, s)], self.delta))
            QA = novos
        return len(QA.intersection(self._F)) != 0

    def testar(self, cadeia):
        self.cadeia_valida(cadeia)

        if self.tipo == 'AFD':
            return self.afd(cadeia)
        elif self.tipo == 'AFN':
            return self.afn(cadeia)

    def __str__(self):
        try:
            dados = subdividir_lista(
                list(self.delta.values()), len(self.Sigma))
            print_table(self.Q, self.Sigma, dados)
        except ValueError as error:
            print(f'Ops! Ocorreu um erro. {error}')

        return f'Tabela de transições do {self.tipo} \n'
