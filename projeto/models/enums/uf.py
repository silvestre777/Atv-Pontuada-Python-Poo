from enum import Enum

class Uf(Enum):
    BAHIA = ("Bahia","BA")
    SAO_PAULO = ("São Paulo", "SP")


    def __init__(self, estado : str, sigla: str) -> None:
        self.estado = estado
        self.sigla = sigla