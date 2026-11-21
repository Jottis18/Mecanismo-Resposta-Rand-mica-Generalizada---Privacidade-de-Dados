# Trabalho 5 — Privacidade Diferencial Local com GRR

Implementação própria do **Generalized Randomized Response (GRR)** e comparação de duas
estratégias para responder 10 consultas de contagem sobre idade e salário (`dados/dados_censo.csv`):

- **E1:** GRR no domínio conjunto idade × salário (74 × 2 = 148 valores);
- **E2:** GRR com a idade agrupada em bins (k_B × 2 valores).

Protocolo: ε ∈ {0,5; 1; 2; 4}, 10 repetições por (estratégia, ε) com sementes fixas,
MAE médio ± desvio e MAE por consulta, com e sem truncamento em [0, n].

**Entrega: segunda, 23/11/2026, até 10h** (notebook + relatório em PDF).
Apresentação de 10 min + 5 min de arguição, em que qualquer um pode ser perguntado sobre qualquer parte.

## Quem faz o quê

| Arquivo | Dono | Conteúdo |
| --- | --- | --- |
| `contrato.py` | os dois (só muda com acordo) | domínio, consultas, assinaturas, formatos e respostas de referência |
| `grr_stub.py` | os dois (só muda com acordo) | GRR sem ruído, para testar sem esperar o `grr.py` |
| `grr.py` | Pessoa A | GRR: cliente (`grr_perturba`) e servidor (`grr_estima_contagens`) |
| `consultas.py` | Pessoa A | respostas verdadeiras das 10 consultas |
| `estrategia_e2.py` | Pessoa A | E2: bins e política de bin atravessado |
| `avaliacao.py` | Pessoa A | sementes, repetições, MAE e truncamento |
| `dados.py` | Pessoa B | leitura e codificação do CSV |
| `estrategia_e1.py` | Pessoa B | E1: domínio conjunto de 148 valores |
| `graficos.py` | Pessoa B | gráficos e tabelas do relatório |
| `estrategias.py` | os dois | só reúne E1 e E2 |

Tarefas detalhadas e cronograma: [TAREFAS.md](TAREFAS.md).

## Regras do repositório

- Cada um só edita os próprios arquivos; `contrato.py` e `grr_stub.py` só mudam com acordo.
- Enquanto o `grr.py` não estiver pronto, use `from grr_stub import ...`; depois, troque por `from grr import ...`.
- Com o stub, E1 e E2 com largura 1 têm de reproduzir exatamente `contrato.VERDADE_REFERENCIA`.
- Toda aleatoriedade vem do `rng` que a estratégia recebe (reprodutibilidade).
- Bibliotecas de LDP são proibidas; numpy, pandas, scipy e matplotlib são permitidos.

## Como rodar

```bash
pip install -r requirements.txt
```

O notebook final (montado no domingo) importa estes módulos e gera todas as tabelas e figuras.
