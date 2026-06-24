from modelos.item import Item
from modelos.pedido import Pedido


class PedidoService:
    """Camada de serviço: as regras de negócio. Recebe o repositório (injeção)."""

    def __init__(self, repo) -> None:
        self.repo = repo

    def criar_pedido(self, cliente: str) -> Pedido:
        pedido = Pedido(id=self.repo.proximo_id(), cliente=cliente)
        self.repo.salvar(pedido)
        return pedido

    def adicionar_item(self, pedido_id: int, nome: str, preco: float, qtd: int) -> None:
        pedido = self.repo.buscar(pedido_id)
        if pedido is None or pedido.fechado:
            raise ValueError("Pedido inválido ou já fechado")
        item = Item(nome=nome, preco=preco, qtd=qtd)
        pedido.adicionar(item)

    def fechar_pedido(self, pedido_id: int) -> float:
        pedido = self.repo.buscar(pedido_id)
        if pedido is None or pedido.fechado:
            raise ValueError("Pedido inválido ou já fechado")
        pedido.fechado = True
        return pedido.total()