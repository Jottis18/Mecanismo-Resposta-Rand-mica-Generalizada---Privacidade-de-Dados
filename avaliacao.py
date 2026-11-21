"""Trabalho 5 - Privacidade Diferencial: sementes, repetições e MAE.

Dono: Pessoa A. As colunas de saída estão em contrato.py (COLUNAS_*) e são usadas pelos
gráficos da Pessoa B.
"""

import numpy as np
import pandas as pd

from contrato import (
    CONSULTAS,
    EPSILONS,
    REPETICOES,
    COLUNAS_RESULTADO,
    COLUNAS_RESUMO,
    COLUNAS_POR_CONSULTA,
)


# 1. EXECUÇÃO DO EXPERIMENTO (ESTRATÉGIA x ε x REPETIÇÃO, COM SEMENTES FIXAS)
def avaliar(estrategias, idades, salarios, epsilons=EPSILONS, repeticoes=REPETICOES):
    # estrategias: dict nome -> f(idades, salarios, eps, rng)
    # -> DataFrame com COLUNAS_RESULTADO (uma linha por consulta)
    raise NotImplementedError("Pessoa A")


# 2. MÉTRICAS (MAE)
def resumo_mae(df, truncado=False):
    # MAE por (estrategia, epsilon): média e desvio sobre as repetições -> COLUNAS_RESUMO
    raise NotImplementedError("Pessoa A")


def mae_por_consulta(df, eps, truncado=False):
    # MAE de cada consulta num ε fixo (média sobre as repetições) -> COLUNAS_POR_CONSULTA
    raise NotImplementedError("Pessoa A")
