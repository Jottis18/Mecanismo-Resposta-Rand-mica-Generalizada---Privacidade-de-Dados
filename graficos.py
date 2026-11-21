"""Trabalho 5 - Privacidade Diferencial: gráficos e tabelas do relatório.

Dono: Pessoa B. Entradas nos formatos de contrato.py (COLUNAS_RESUMO e
COLUNAS_POR_CONSULTA); até os resultados reais chegarem, teste com um DataFrame de mentira.
Como no trabalho 3, cada função salva a figura em `caminho` (um .png em resultados/).
"""

import matplotlib.pyplot as plt


# 1. MAE EM FUNÇÃO DE ε
def grafico_mae_por_eps(resumo, caminho=None, log=True):
    # MAE médio ± desvio por ε, uma linha por estratégia; indicar se o eixo y é log
    raise NotImplementedError("Pessoa B")


# 2. MAE POR CONSULTA NUM ε FIXO
def tabela_mae_por_consulta(por_consulta, caminho=None):
    # MAE de cada consulta, por estratégia (tabela ou gráfico)
    raise NotImplementedError("Pessoa B")


# 3. COMPARAÇÃO DAS LARGURAS DE BIN DO E2
def grafico_larguras_e2(resumo, caminho=None):
    # MAE de cada largura testada no E2, por ε
    raise NotImplementedError("Pessoa B")
