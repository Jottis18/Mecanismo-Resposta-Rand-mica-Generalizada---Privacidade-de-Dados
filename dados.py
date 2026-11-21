"""Trabalho 5 - Privacidade Diferencial: leitura e codificação do dados_censo.csv.

Dono: Pessoa B.
"""

import os

import numpy as np
import pandas as pd

PASTA_PROJETO = os.path.dirname(os.path.abspath(__file__))


# 1. LEITURA E CODIFICAÇÃO DA BASE
def carregar_dados(caminho=os.path.join(PASTA_PROJETO, "dados_censo.csv")):
    # -> (idades, salarios): idades int em 17..90; salarios 0 ("<=50K") ou 1 (">50K")
    raise NotImplementedError("Pessoa B")
