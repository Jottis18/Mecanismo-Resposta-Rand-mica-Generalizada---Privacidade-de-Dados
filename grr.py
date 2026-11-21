"""Trabalho 5 - Privacidade Diferencial: mecanismo GRR (Generalized Randomized Response).

Dono: Pessoa A. Implementação própria (bibliotecas de LDP são proibidas).
"""

import numpy as np


# 1. CLIENTE: CADA USUÁRIO PERTURBA O PRÓPRIO VALOR
def grr_perturba(valores, k, eps, rng):
    # Inteiros em 0..k-1 -> um report em 0..k-1 por usuário
    raise NotImplementedError("Pessoa A")


# 2. SERVIDOR: ESTIMA AS CONTAGENS SÓ A PARTIR DOS REPORTS
def grr_estima_contagens(reports, k, eps):
    # Reports -> vetor n_hat de tamanho k (estimador não viesado)
    raise NotImplementedError("Pessoa A")
