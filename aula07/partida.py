# partida.py — um servico com EFEITO COLATERAL (narrar), mas testavel.
#
# A Partida RECEBE o narrador pelo construtor (injecao de dependencia — o DIP da Aula 5).
# Por isso, no teste, da pra passar um narrador "de mentira" que so anota.
class Narrador:
    def gol(self, time):
        print(f"GOOOL do {time}!")        # efeito real (ao vivo, narraria de verdade)


class Partida:
    def __init__(self, narrador):          # recebe o narrador de FORA
        self.narrador = narrador
        self.gols = {"casa": 0, "fora": 0}

    def marcar_gol(self, lado, time):
        self.gols[lado] += 1
        self.narrador.gol(time)            # avisa o narrador


if __name__ == "__main__":
    partida = Partida(Narrador())          # no programa real, entra o Narrador de verdade
    partida.marcar_gol("casa", "Brasil")   # imprime: GOOOL do Brasil!
    print(partida.gols)                    # {'casa': 1, 'fora': 0}
