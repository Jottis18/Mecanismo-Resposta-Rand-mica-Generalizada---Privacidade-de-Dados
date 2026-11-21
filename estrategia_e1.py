"""
E1 — GRR no domínio conjunto idade x salário (74 * 2 = 148 valores).   Dono: Pessoa B

Até o grr.py de A chegar, use o stub: com ele, as respostas têm de bater
exatamente com contrato.VERDADE_REFERENCIA.
"""
import numpy as np

from contrato import CONSULTAS, IDADE_MIN, K_IDADE, K_SAL
from grr_stub import grr_perturba, grr_estima_contagens   # trocar por: from grr import ...


def estrategia_e1(idades, salarios, eps, rng):
    """Cliente: par (idade, salário) -> índice 0..147 -> GRR.

    Servidor: estima as 148 células e soma as de cada consulta
    -> np.ndarray (10,), na ordem de CONSULTAS.
    """
    raise NotImplementedError("Pessoa B")
