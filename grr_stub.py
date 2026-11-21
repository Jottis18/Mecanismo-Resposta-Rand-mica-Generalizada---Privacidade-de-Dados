"""Trabalho 5 - Privacidade Diferencial: GRR sem ruído, com as mesmas assinaturas do grr.py.

Serve para a Pessoa B testar o E1 antes de o grr.py ficar pronto e para a Pessoa A medir,
no E2, só o erro causado pelos bins. Com ele, E1 e E2 com largura 1 reproduzem
contrato.VERDADE_REFERENCIA.
"""

import numpy as np


def grr_perturba(valores, k, eps, rng):
    # Devolve os próprios valores: nenhum usuário troca de valor
    return np.asarray(valores).copy()


def grr_estima_contagens(reports, k, eps):
    # Contagem exata de cada valor do domínio
    return np.bincount(reports, minlength=k).astype(float)
