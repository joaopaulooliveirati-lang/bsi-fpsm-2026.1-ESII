# placar.py — resultado de uma partida (sempre do ponto de vista do time da casa)
#
# Funcao "pura": dado o mesmo placar, devolve sempre o mesmo resultado.
# Por isso e facil de testar — e o alvo da Parte B.
def resultado(gols_casa, gols_fora):
    if gols_casa > gols_fora:
        return "vitória"
    elif gols_casa < gols_fora:
        return "derrota"
    return "empate"
