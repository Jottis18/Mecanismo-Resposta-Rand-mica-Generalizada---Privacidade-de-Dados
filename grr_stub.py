"""
Stub SEM ruído do GRR, com as mesmas assinaturas de grr.py.

Serve para:
  - B testar o E1 antes de o grr.py ficar pronto;
  - A medir no E2 só o erro causado pelos bins (sem o ruído do GRR).
Com ele, E1 e E2 com largura 1 reproduzem contrato.VERDADE_REFERENCIA.
"""
import numpy as np


def grr_perturba(valores, k, eps, rng):
    return np.asarray(valores).copy()


def grr_estima_contagens(reports, k, eps):
    return np.bincount(reports, minlength=k).astype(float)
