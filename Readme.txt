# Trabalho 5: Privacidade Diferencial – Mecanismo de Resposta Randômica Generalizada (GRR)

- Disciplina: Privacidade de Dados
- Professor: Javam Machado
- Linguagem: Python

---

## Descrição do Projeto

Este projeto consiste na implementação do mecanismo **Generalized Randomized Response (GRR)** do zero (sem bibliotecas prontas de privacidade diferencial local), no modelo **local** de privacidade diferencial (LDP), e na comparação de duas estratégias para responder a 10 consultas de contagem sobre os atributos Idade e Salário da base `dados_censo.csv`:

- **E1:** GRR sobre o domínio conjunto idade × salário (74 × 2 = 148 valores);
- **E2:** GRR com a idade agrupada em faixas (bins) antes da perturbação (k_B × 2 valores).

O objetivo é avaliar o erro (MAE) das respostas privadas em diferentes orçamentos de privacidade (ε = 0,5, 1, 2 e 4) e entender como o tamanho do domínio e a largura das faixas afetam a precisão.

---

## Como Executar

Requisitos: Python 3 e as bibliotecas listadas em `requirements.txt` (numpy, pandas, matplotlib e notebook).

1. Coloque o arquivo `dados_censo.csv`, fornecido com o enunciado, na pasta do projeto.

2. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

3. Abra o notebook `trabalho_privacidade.ipynb` (no Jupyter ou no VS Code) e execute todas as células.

O notebook salva todas as tabelas e gráficos na pasta `resultados/`. Como as sementes são fixas, os resultados são os mesmos a cada execução.

---

## Dados e Consultas

A base `dados_censo.csv` tem 48.842 registros, um por indivíduo, sem valores faltantes:

- **Idade:** inteiro de 17 a 90 (k = 74 valores);
- **Salário:** `<=50K` ou `>50K` (k = 2), codificado como 0 e 1; 23,93% dos registros têm `>50K`.

O domínio conjunto tem 74 × 2 = 148 valores. As 10 consultas do enunciado usam intervalos fechados de idade:

| Consulta | Predicado                       | Resposta verdadeira |
|----------|---------------------------------|---------------------|
| Q1       | 30 ≤ Idade ≤ 50 e Sal = >50K    | 7.820               |
| Q2       | Idade < 20 e Sal = <=50K        | 2.507               |
| Q3       | Idade ≥ 60 e Sal = >50K         | 985                 |
| Q4       | 20 ≤ Idade ≤ 30 e Sal = >50K    | 990                 |
| Q5       | 40 ≤ Idade ≤ 60 e Sal = >50K    | 6.629               |
| Q6       | Idade ≤ 30 e Sal = <=50K        | 14.800              |
| Q7       | Idade ≥ 40 e Sal = <=50K        | 13.918              |
| Q8       | 30 ≤ Idade ≤ 40 e Sal = <=50K   | 10.261              |
| Q9       | Idade ≥ 50                      | 10.674              |
| Q10      | Sal = >50K                      | 11.687              |

---

## Estratégia E1: GRR sobre o Domínio Conjunto

_A preencher (Pessoa B): codificação do par (idade, salário) em um índice de 0 a 147, perturbação pelo GRR e soma das células de cada consulta._

---

## Estratégia E2: GRR com Idade em Faixas

_A preencher (Pessoa A): largura escolhida e justificativa, onde a grade de faixas começa, ajuste do último bin para incluir a idade 90 e tratamento das consultas cujos limites atravessam um bin._

---

## Fundamentação Teórica da Privacidade Diferencial

* **Privacidade diferencial local (ε-LDP):** cada usuário perturba o próprio valor antes de enviá-lo, e o agregador só vê os valores perturbados. Um mecanismo M satisfaz ε-LDP se Pr[M(v) = y] ≤ e^ε · Pr[M(v') = y] para quaisquer valores de entrada v, v' e qualquer saída y.
* **GRR:** num domínio de tamanho k, o usuário reporta o valor verdadeiro com probabilidade p = e^ε / (e^ε + k − 1) e cada um dos outros k − 1 valores com probabilidade q = 1 / (e^ε + k − 1). Como p / q = e^ε, o mecanismo satisfaz ε-LDP. Para o mesmo ε, quanto maior o domínio k, menor é p e maior é o ruído.
* **Estimador não viesado:** com n usuários e c_y reports iguais a y, a estimativa do número de usuários com valor y é n̂_y = (c_y − n·q) / (p − q). Para uma consulta que cobre um conjunto S de valores, a resposta estimada é a soma das estimativas de S, (c_S − n·|S|·q) / (p − q), e o erro cresce com |S| e com k.
* **Pós-processamento:** truncar as estimativas em [0, n] não afeta a garantia de privacidade. Os resultados são reportados com e sem truncamento.

---

## Resultados

_A preencher após os experimentos (ε = 0,5, 1, 2 e 4; 10 repetições por estratégia e ε): MAE médio ± desvio padrão por ε, MAE de cada consulta para um ε fixo e comparação das larguras de bin do E2._

---

## Estrutura do Repositório

```text
.
├── trabalho_privacidade.ipynb   # Notebook principal: roda tudo e mostra tabelas e figuras
├── contrato.py                  # Domínio, consultas, ε, colunas de saída e respostas de referência
├── grr.py                       # GRR: perturbação (cliente) e estimação (servidor)
├── grr_stub.py                  # GRR sem ruído, usado nos testes
├── dados.py                     # Leitura e codificação do dados_censo.csv
├── consultas.py                 # Respostas verdadeiras das 10 consultas
├── estrategia_e1.py             # E1: GRR sobre o domínio conjunto (148 valores)
├── estrategia_e2.py             # E2: GRR com idade em faixas
├── estrategias.py               # Reúne E1 e E2
├── avaliacao.py                 # Sementes, repetições e MAE
├── graficos.py                  # Gráficos e tabelas
├── requirements.txt             # Dependências do projeto
├── dados_censo.csv              # Base de dados do enunciado (ignorada pelo Git)
├── resultados/                  # Tabelas (.csv) e gráficos (.png) gerados pelo notebook
├── TAREFAS.md                   # Divisão do trabalho entre a dupla
├── Readme.txt                   # Documentação do projeto
├── Readme.md                    # Documentação do projeto (mesmo conteúdo, em Markdown)
└── .gitignore                   # Arquivo de exclusão do Git
```

---

## Referências

- Wang, T.; Blocki, J.; Li, N.; Jha, S. Locally Differentially Private Protocols for Frequency Estimation. *USENIX Security*, 2017.
- Dwork, C.; Roth, A. The Algorithmic Foundations of Differential Privacy. *Foundations and Trends in Theoretical Computer Science*, 2014.
- Warner, S. L. Randomized Response: A Survey Technique for Eliminating Evasive Answer Bias. *Journal of the American Statistical Association*, 1965.
