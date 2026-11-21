"""
GRR — Generalized Randomized Response.                    Dono: Pessoa A

Implementação própria (bibliotecas de LDP são proibidas).
  CLIENTE  -> grr_perturba: cada usuário perturba o próprio valor.
  SERVIDOR -> grr_estima_contagens: só enxerga os reports.
"""
import numpy as np


def grr_perturba(valores, k, eps, rng):
    """CLIENTE: inteiros em 0..k-1 -> um report em 0..k-1 por usuário."""
    raise NotImplementedError("Pessoa A")


def grr_estima_contagens(reports, k, eps):
    """SERVIDOR: só os reports -> vetor n_hat de tamanho k (estimador não viesado)."""
    raise NotImplementedError("Pessoa A")
