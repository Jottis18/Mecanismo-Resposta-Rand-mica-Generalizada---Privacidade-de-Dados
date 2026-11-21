"""
Gráficos e tabelas do relatório.                           Dono: Pessoa B

Entradas nos formatos de contrato.py (COLUNAS_RESUMO, COLUNAS_POR_CONSULTA).
Até os resultados reais chegarem, teste com um DataFrame de mentira.
"""
import matplotlib.pyplot as plt


def grafico_mae_por_eps(resumo, log=True):
    """MAE médio ± desvio em função de eps, uma linha por estratégia (dizer se o eixo y é log)."""
    raise NotImplementedError("Pessoa B")


def tabela_mae_por_consulta(por_consulta):
    """MAE de cada consulta num eps fixo, por estratégia (tabela ou gráfico)."""
    raise NotImplementedError("Pessoa B")


def grafico_larguras_e2(resumo):
    """Comparação do MAE entre as larguras de bin testadas no E2."""
    raise NotImplementedError("Pessoa B")
