# Divisão do trabalho

A Pessoa A fica com GRR, E2, avaliação e análise; a Pessoa B, com dados, E1, gráficos e a montagem
do notebook, do Readme, do relatório e dos slides. Nada do que A constrói depende de B; só a
comparação final E1 × E2 usa o E1 de B. B recebe o `grr.py` no sábado à tarde e os resultados no domingo.

## Quem mexe em cada arquivo

| Arquivo | Dono | Conteúdo |
| --- | --- | --- |
| `contrato.py` | os dois (só muda com acordo) | domínio, consultas, assinaturas, colunas de saída e respostas de referência |
| `grr_stub.py` | os dois (só muda com acordo) | GRR sem ruído, para testar sem esperar o `grr.py` |
| `grr.py` | Pessoa A | GRR: cliente (`grr_perturba`) e servidor (`grr_estima_contagens`) |
| `consultas.py` | Pessoa A | respostas verdadeiras das 10 consultas |
| `estrategia_e2.py` | Pessoa A | E2: bins e política de bin atravessado |
| `avaliacao.py` | Pessoa A | sementes, repetições, MAE e truncamento |
| `dados.py` | Pessoa B | leitura e codificação do `dados_censo.csv` |
| `estrategia_e1.py` | Pessoa B | E1: domínio conjunto de 148 valores |
| `graficos.py` | Pessoa B | gráficos e tabelas, salvos em `resultados/` |
| `trabalho_privacidade.ipynb` | Pessoa B (montagem) | notebook principal; as seções já estão criadas |
| `Readme.md` e `Readme.txt` | Pessoa B (montagem) | documentação no padrão do trabalho 3; A escreve as seções de E2 e de resultados |
| `estrategias.py` | os dois | só reúne E1 e E2 |

## Regras do repositório

- Cada um só edita os próprios arquivos; `contrato.py` e `grr_stub.py` só mudam com acordo.
- O `dados_censo.csv` fica na pasta do projeto e não vai para o Git (está no `.gitignore`).
- Enquanto o `grr.py` não estiver pronto, use `from grr_stub import ...`; depois, troque por `from grr import ...`.
- Com o stub, E1 e E2 com largura 1 têm de reproduzir exatamente `contrato.VERDADE_REFERENCIA`.
- Toda aleatoriedade vem do `rng` que a estratégia recebe (reprodutibilidade).
- Bibliotecas de LDP são proibidas; numpy, pandas, scipy e matplotlib são permitidos.
- `Readme.md` e `Readme.txt` têm o mesmo conteúdo: ao mudar um, copie para o outro.

## Pessoa A — GRR, E2, avaliação e análise

- [ ] `grr.py`: `grr_perturba` (cliente) e `grr_estima_contagens` (servidor), vetorizados com numpy.
- [ ] Testar o GRR: p/q = e^ε; com ε = 50 as estimativas batem com as contagens; a média de muitas execuções fica perto da verdade.
- [ ] Subir o `grr.py` testado até sábado à tarde.
- [ ] `consultas.py`: `respostas_verdadeiras`, conferida com `VERDADE_REFERENCIA`.
- [ ] Listar, para larguras candidatas (ex.: 2 a 20), quais consultas atravessam bins.
- [ ] Decidir onde a grade de bins começa (em 17 ou alinhada às dezenas) e justificar.
- [ ] `estrategia_e2.py`: `idade_para_bin` (último bin ajustado para incluir o 90), política de bin atravessado e `estrategia_e2`.
- [ ] Com o stub, medir o erro sem ruído por largura (isola o viés dos bins).
- [ ] `avaliacao.py`: `avaliar`, `resumo_mae` e `mae_por_consulta`, com as colunas do contrato.
- [ ] Comparar larguras com ruído e escolher a largura principal.
- [ ] Análise: menor MAE em cada ε, se a melhor estratégia muda com ε, melhor largura e efeito dos bins atravessados, consultas com maior e menor erro em cada estratégia.
- [ ] Relatório, slides e Readme: fundamentos do GRR, projeto do E2 e toda a análise (no Readme, as seções de E2 e de resultados).

## Pessoa B — dados, E1, gráficos e montagem

- [ ] `dados.py`: `carregar_dados`.
- [ ] `estrategia_e1.py`: par (idade, salário) → índice de 0 a 147, GRR e soma das células de cada consulta; com o stub, conferir com `VERDADE_REFERENCIA`.
- [ ] Trocar o stub pelo `grr.py` quando ele chegar (só muda o import).
- [ ] `graficos.py`: MAE × ε (indicando se o eixo é log), MAE por consulta num ε fixo e comparação de larguras do E2, salvando os .png em `resultados/`; testar com um DataFrame de mentira.
- [ ] `trabalho_privacidade.ipynb`: completar a montagem (as seções já estão criadas) e salvar as tabelas em `resultados/`.
- [ ] Demonstração para a apresentação, como o `--detalhar` do trabalho 3: um usuário, o report dele em cada ε e como o servidor estima.
- [ ] `Readme.md` e `Readme.txt` finais: seção do E1 e revisão geral (A escreve E2 e resultados).
- [ ] Relatório: esqueleto do PDF, seção de configuração experimental e encaixe das figuras.
- [ ] Slides: estrutura e visual da apresentação de 10 min, mais os slides do E1.
- [ ] Estudar o GRR e o E2 pelo código de A antes do ensaio de domingo.

## Juntos

- [ ] Domingo à tarde: rodar o notebook inteiro (E1 e E2 nas larguras testadas, 4 valores de ε, 10 repetições) e gerar as figuras finais.
- [ ] Juntar notebook, Readme, relatório em PDF e slides.
- [ ] Ensaio cruzado sem olhar o código (A explica GRR e E2; B explica dados, E1 e gráficos) e ensaio cronometrado de 10 min.
- [ ] Segunda até 10h: revisão final e submissão.

## Cronograma

| Quando | Pessoa A | Pessoa B |
| --- | --- | --- |
| Sáb, manhã e tarde | GRR e testes, `consultas.py`; **`grr.py` no repositório à tarde** | `dados.py`, E1 com o stub, `graficos.py`; troca o stub pelo `grr.py` |
| Sáb, noite | E2 (grade, bin atravessado, erro sem ruído) e `avaliacao.py` | notebook, esqueleto do relatório e dos slides |
| Dom, manhã | larguras com ruído, escolha da largura, seções de GRR, E2 e análise | estudar GRR e E2, demonstração, slides do E1, encaixe das figuras |
| Dom, tarde e noite | **juntos:** integração, análise final, montagem e ensaios | **juntos** |
| Seg, até 10h | **juntos:** revisão final e submissão | **juntos** |
