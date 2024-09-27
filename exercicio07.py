# Exercício 07
"""
Um investidor tem um capital de R$ 1000,00 para investir em renda fixa.
Atualmente, ele tem duas opções de investimento:
- Poupança: rende 0.5% ao mês
- LCA: rende 0.7% ao mês

Ao final de 10 anos de investimento, quanto o investidor terá ganho a mais se escolher o LCA ao invés da poupança?
"""

def calcula_lucro_investimento(capital, taxa, meses):
    return capital * (1 + taxa) ** meses

capital = 1000.00
taxa_poupanca = 0.005
taxa_lca = 0.007
anos = 10
meses = anos * 12

montante_poupanca = calcula_lucro_investimento(capital, taxa_poupanca, meses)
montante_lca = calcula_lucro_investimento(capital, taxa_lca, meses)

diferenca = montante_lca - montante_poupanca

print(f"A diferença no lucro será de: {diferenca}")
