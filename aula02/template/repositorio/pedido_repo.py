from modelos.pedido import Pedido


class PedidoRepo:
    """Camada de persistência: guarda e busca pedidos (em memória)."""

    def __init__(self) -> None:
        self._pedidos: list[Pedido] = []

    def salvar(self, pedido: Pedido) -> None:
        if pedido not in self._pedidos:
            self._pedidos.append(pedido)

    def buscar(self, pedido_id: int):
        for pedido in self._pedidos:
            if pedido.id == pedido_id:
                return pedido
        return None

    def listar(self) -> list:
        return self._pedidos

    def proximo_id(self) -> int:
        return len(self._pedidos) + 1