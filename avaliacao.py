"""
Motor de avaliação: sementes, repetições e MAE.            Dono: Pessoa A

Formatos de saída definidos em contrato.py (COLUNAS_*), que os gráficos de B usam.
"""
import numpy as np
import pandas as pd

from contrato import (CONSULTAS, EPSILONS, REPETICOES, COLUNAS_RESULTADO,
                      COLUNAS_RESUMO, COLUNAS_POR_CONSULTA)


def avaliar(estrategias, idades, salarios, epsilons=EPSILONS, repeticoes=REPETICOES):
    """estrategias: dict nome -> f(idades, salarios, eps, rng).

    Roda cada (estratégia, eps, repetição) com semente fixa e documentada
    -> DataFrame com COLUNAS_RESULTADO (uma linha por consulta).
    """
    raise NotImplementedError("Pessoa A")


def resumo_mae(df, truncado=False):
    """MAE por (estrategia, eps): média e desvio sobre as repetições -> COLUNAS_RESUMO."""
    raise NotImplementedError("Pessoa A")


def mae_por_consulta(df, eps, truncado=False):
    """MAE de cada consulta num eps fixo (média sobre as repetições) -> COLUNAS_POR_CONSULTA."""
    raise NotImplementedError("Pessoa A")
