"""
E2 — GRR com a idade agrupada em bins.                     Dono: Pessoa A

Para medir só o erro causado pelos bins, troque o import pelo grr_stub.
"""
import numpy as np

from contrato import CONSULTAS, IDADE_MIN, IDADE_MAX, K_SAL
from grr import grr_perturba, grr_estima_contagens
# from grr_stub import grr_perturba, grr_estima_contagens   # sem ruído


def idade_para_bin(idades, largura):
    """Índice do bin de cada idade; o último bin é ajustado para incluir o 90."""
    raise NotImplementedError("Pessoa A")


def estrategia_e2(idades, salarios, eps, rng, largura):
    """Cliente: (bin, salário) -> GRR no domínio k_B * 2.

    Servidor: estima as células e responde as 10 consultas, com a política de
    bin atravessado documentada -> np.ndarray (10,), na ordem de CONSULTAS.
    """
    raise NotImplementedError("Pessoa A")
