# Implementação de Automatos Finitos
 Essa é uma implementação de autômato finito determinístico, de autômato finito não-determinístico e não-determinístico com transição vazia.

## Como rodar?
É preciso ter o [python 3](https://www.python.org/downloads/) instalado na sua máquina. (sugiro ter uma versão atualizada).  

### Para executar o programa

Primeiramente, clone o repositório e acesse o diretório:
```bash
$ git clone https://github.com/evertonandrade/automatos-finitos.git
$ cd automatos-finitos
```

Instale as dependências
```bash
$ pip install -r requirements.txt
```

Execute com:
```bash
$ python main.py
```

### Instruções do programa
- Digite os estados separando-os por 1 espaço.
- O alfabeto da mesma forma separando os simbolos por 1 espaço.
- Para usar a transição vazia especifique `epsilon` como caractere do alfabeto
- Qualquer outro erro gerará uma exceção.
- A partir do preenchimento da tabela de transição o programa irá verificar automáticamente se é um AFD ou AFN.
- Após definir todos os 5 componentes do autômato, basta informa uma cadeia para o reconhecimento.  

### Exemplo de execução do AFD
> AFN sobre Σ = {a, b} que considere  
> L = { w | w possui **aa** ou **bb** como subpalavra }  
> tal que = ({q0, q1, q2, qf }, Σ, δf, q0, {qf }).  

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
> AFN sobre Σ = {a, b} que considere  
> L = { w | w possui **aaa** como sufixo }  
> tal que = ({q0, q1, q2, qf }, Σ, δf, q0, {qf }).

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


### Exemplo de execução do AFN com transição vazia
> AFN com transição vazia que aceita palavras na forma a* b*  

```
❯ python main.py
Quais são os estados do autômato? q0 qf

Qual o alfabeto do autômato? a b epsilon

Estando em q0 e lendo a vai para? q0
Estando em q0 e lendo b vai para? ø
Estando em q0 e lendo epsilon vai para? qf
Estando em qf e lendo a vai para? ø
Estando em qf e lendo b vai para? qf
Estando em qf e lendo epsilon vai para? ø

    |   a   b epsilon
----+---------------
 q0 |  q0   ø  qf
 qf |   ø  qf   ø
--------------------
Tabela de transições do AFN 

Qual o estado inicial? q0

Quais são os estados finais? qf

Digite a Cadeia (p/ sair pressione apenas ENTER): abab
A cadeia foi rejeitada

Digite a Cadeia (p/ sair pressione apenas ENTER): ab
A cadeia foi aceita

Digite a Cadeia (p/ sair pressione apenas ENTER): ba
A cadeia foi rejeitada

Digite a Cadeia (p/ sair pressione apenas ENTER): aaabbb
A cadeia foi aceita

Digite a Cadeia (p/ sair pressione apenas ENTER): aaaaabbbb
A cadeia foi aceita

Digite a Cadeia (p/ sair pressione apenas ENTER): ab
A cadeia foi aceita

Digite a Cadeia (p/ sair pressione apenas ENTER): a
A cadeia foi aceita

Digite a Cadeia (p/ sair pressione apenas ENTER): b
A cadeia foi aceita

Digite a Cadeia (p/ sair pressione apenas ENTER): 

saindo...

```
---

<p align="center">
Made with ♥ by <a href="http://everton.github.io">Everton</a>
</p>
