from projeto.models.enums.uf import Uf


class Pessoa:
    def __init__(self, nome:str, idade:int, uf:Uf):
        if idade <0:
            raise ValueError("Idade nao pode ser negativa.")
        self.nome = nome
        self.idade = idade
        self.uf=uf

    def __str__(self) -> str:
        return (f"\n Nome: {self.nome}"
                f"\n Idade: {self.idade}"
                f"\n UF: {self.uf.sigla}")
    