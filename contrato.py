"""Trabalho 5 - Privacidade Diferencial: contrato entre a Pessoa A e a Pessoa B.

Tudo o que os dois lados precisam combinar está aqui: domínio, codificação, consultas,
assinaturas e colunas dos arquivos de saída. Não mude sem avisar o outro.
"""

# 1. DOMÍNIO (FIXO PELO ENUNCIADO; NÃO DERIVAR DOS DADOS)
IDADE_MIN, IDADE_MAX = 17, 90
K_IDADE = IDADE_MAX - IDADE_MIN + 1      # 74
SALARIOS = ["<=50K", ">50K"]             # códigos 0 e 1
K_SAL = len(SALARIOS)                    # 2

# 2. PROTOCOLO EXPERIMENTAL
EPSILONS = [0.5, 1.0, 2.0, 4.0]
REPETICOES = 10

# 3. CODIFICAÇÃO USADA POR TODAS AS ESTRATÉGIAS
#   idades   -> np.ndarray de int em 17..90
#   salarios -> np.ndarray de int em {0, 1}   (0 = "<=50K", 1 = ">50K")
#   rng      -> np.random.Generator (toda aleatoriedade vem dele)

# 4. CONSULTAS: retângulos FECHADOS (nome, idade_min, idade_max, códigos de salário)
CONSULTAS = [
    ("Q1",  30, 50, (1,)),
    ("Q2",  17, 19, (0,)),     # Idade < 20
    ("Q3",  60, 90, (1,)),     # Idade >= 60
    ("Q4",  20, 30, (1,)),
    ("Q5",  40, 60, (1,)),
    ("Q6",  17, 30, (0,)),     # Idade <= 30
    ("Q7",  40, 90, (0,)),     # Idade >= 40
    ("Q8",  30, 40, (0,)),
    ("Q9",  50, 90, (0, 1)),   # marginal de idade
    ("Q10", 17, 90, (1,)),     # marginal de salário
]
NOMES_CONSULTAS = [nome for nome, *_ in CONSULTAS]

# Respostas verdadeiras no dados_censo.csv (48.842 registros), para conferir o código.
# Com o grr_stub, E1 e E2 com largura 1 têm de reproduzir exatamente estes valores.
VERDADE_REFERENCIA = {
    "Q1": 7820, "Q2": 2507, "Q3": 985, "Q4": 990, "Q5": 6629,
    "Q6": 14800, "Q7": 13918, "Q8": 10261, "Q9": 10674, "Q10": 11687,
}

# 5. ASSINATURAS (implementadas nos arquivos de cada um)
#   grr.grr_perturba(valores, k, eps, rng) -> reports               [A] CLIENTE
#   grr.grr_estima_contagens(reports, k, eps) -> n_hat, shape (k,)  [A] SERVIDOR
#   estrategia_e1(idades, salarios, eps, rng) -> np.ndarray (10,)            [B]
#   estrategia_e2(idades, salarios, eps, rng, largura) -> np.ndarray (10,)   [A]
#     (no motor de avaliação: functools.partial(estrategia_e2, largura=w))

# 6. COLUNAS DOS ARQUIVOS DE SAÍDA (salvos em resultados/)
# avaliacao.avaliar (A): uma linha por (estrategia, epsilon, rep, consulta)
COLUNAS_RESULTADO = [
    "estrategia",        # str, ex.: "E1", "E2-w10"
    "epsilon",           # float
    "rep",               # int, 0..REPETICOES-1
    "semente",           # int usada na repetição
    "consulta",          # str, "Q1".."Q10"
    "verdade",           # int
    "estimativa",        # float, sem truncamento
    "estimativa_trunc",  # float, truncada em [0, n]
]
# avaliacao.resumo_mae(df, truncado) -> entrada dos gráficos de B
COLUNAS_RESUMO = ["estrategia", "epsilon", "mae_media", "mae_desvio"]
# avaliacao.mae_por_consulta(df, eps, truncado) -> entrada dos gráficos de B
COLUNAS_POR_CONSULTA = ["estrategia", "consulta", "mae"]
