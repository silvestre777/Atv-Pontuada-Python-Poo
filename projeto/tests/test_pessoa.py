import pytest

from projeto.models.pessoa import Pessoa


# pytest.fixture torna como class modelo o def abaixo
@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa("Silvestre", 23)

    return pessoa

def test_pessoa_alterar_nome_valido(pessoa_valida):
    # Alterando o nome da pessoa de "Silvestre" para "Joao"
    pessoa_valida.nome = "Joao"
    assert pessoa_valida.nome == "Joao"

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Silvestre"


def test_pessoa_idade_valida(pessoa_valida):
    assert pessoa_valida.idade == 23


"""def test_pessoa_nome_com_valor_errado_retorna_mensagem_excecao(pessoa_valida):
    with pytest.raises(ValueError, match="Somente letras"):
        Pessoa("321321",23)"""

def test_pessoa_idade_negativa_retorna_mensagem_excecao(pessoa_valida):
    #Mensagem de erro
    with pytest.raises(ValueError, match="Idade nao pode ser negativa."):
        Pessoa("Silvestre",-1)
def test_pessoa_idade_tipo_invalido_retorna_mensagem_excecao(pessoa_valida):
    #Mensagem de erro
    with pytest.raises(TypeError, match="A idade deve contar apenas números."):
        Pessoa("Silvestre","23")