# Implementação de Automatos Finitos
Implementação de Autômatos

### Exemplo de execução do AFD
AFN sobre Σ = {a, b} que considere  
    L = { w | w possui **aa** ou **bb** como subpalavra }  
tal que = ({q0, q1, q2, qf }, Σ, δf, q0, {qf }).  

```
❯ python main.py

Quais são os estados do autômato? q0 q1 q2 qf

Qual o alfabeto do autômato? a b

Estando em q0 e lendo a vai para? q1
Estando em q0 e lendo b vai para? q2
Estando em q1 e lendo a vai para? qf
Estando em q1 e lendo b vai para? q2
Estando em q2 e lendo a vai para? q1
Estando em q2 e lendo b vai para? qf
Estando em qf e lendo a vai para? qf
Estando em qf e lendo b vai para? qf

    |   a   b
----+----------
 q0 |  q1  q2
 q1 |  qf  q2
 q2 |  q1  qf
 qf |  qf  qf
---------------
Tabela de transições do AFD 

Qual o estado inicial? q0

Quais são os estados finais? qf

Digite a Cadeia (p/ sair pressione apenas ENTER): ababab
A cadeia foi rejeitada

Digite a Cadeia (p/ sair pressione apenas ENTER): aababa
A cadeia foi aceita

Digite a Cadeia (p/ sair pressione apenas ENTER): bababa
A cadeia foi rejeitada

Digite a Cadeia (p/ sair pressione apenas ENTER): bababb
A cadeia foi aceita

Digite a Cadeia (p/ sair pressione apenas ENTER): abbaba
A cadeia foi aceita

Digite a Cadeia (p/ sair pressione apenas ENTER): babbbbbaaab
A cadeia foi aceita

Digite a Cadeia (p/ sair pressione apenas ENTER): 

saindo...
```

### Exemplo de execução do AFN
AFN sobre Σ = {a, b} que considere  
    L = { w | w possui **aaa** como sufixo }  
tal que = ({q0, q1, q2, qf }, Σ, δf, q0, {qf }).

``` 
❯ python main.py
Quais são os estados do autômato? q0 q1 q2 qf

Qual o alfabeto do autômato? a b

Estando em q0 e lendo a vai para? q0 q1
Estando em q0 e lendo b vai para? q0
Estando em q1 e lendo a vai para? q2
Estando em q1 e lendo b vai para? ø
Estando em q2 e lendo a vai para? qf
Estando em q2 e lendo b vai para? ø
Estando em qf e lendo a vai para? ø
Estando em qf e lendo b vai para? ø

    |   a   b
----+----------
 q0 |q1q0  q0
 q1 |  q2   ø
 q2 |  qf   ø
 qf |   ø   ø
---------------
Tabela de transições do AFN 

Qual o estado inicial? q0

Quais são os estados finais? qf

Digite a Cadeia (p/ sair pressione apenas ENTER): bbbbbba
A cadeia foi rejeitada

Digite a Cadeia (p/ sair pressione apenas ENTER): aaab
A cadeia foi rejeitada

Digite a Cadeia (p/ sair pressione apenas ENTER): baaa
A cadeia foi aceita

Digite a Cadeia (p/ sair pressione apenas ENTER): baba
A cadeia foi rejeitada

Digite a Cadeia (p/ sair pressione apenas ENTER): baaabb
A cadeia foi rejeitada

Digite a Cadeia (p/ sair pressione apenas ENTER): babbabaa
A cadeia foi rejeitada

Digite a Cadeia (p/ sair pressione apenas ENTER): babababaaa
A cadeia foi aceita

Digite a Cadeia (p/ sair pressione apenas ENTER): aaa
A cadeia foi aceita

Digite a Cadeia (p/ sair pressione apenas ENTER):     

saindo...
```