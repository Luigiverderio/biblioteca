import ast
from inspect import getsource, signature
from copy import deepcopy
import pytest
from pprint import pformat

try:
    import funcoes_biblioteca as funcoes
except Exception:
    funcoes = None

try:
    if funcoes:
        from funcoes_biblioteca import livros_disponiveis
except Exception:
    pass

try:
    if funcoes:
        from funcoes_biblioteca import emprestimos_em_atraso
except Exception:
    pass

try:
    if funcoes:
        from funcoes_biblioteca import contagem_por_genero
except Exception:
    pass

try:
    if funcoes:
        from funcoes_biblioteca import autor_mais_emprestado
except Exception:
    pass

try:
    if funcoes:
        from funcoes_biblioteca import relatorio_usuario
except Exception:
    pass

try:
    if funcoes:
        from funcoes_biblioteca import livro_mais_antigo_disponivel
except Exception:
    pass


# ---------------------------------------------------------------------------
# DADOS DE TESTE
# ---------------------------------------------------------------------------

ACERVO_BASE = [
    {"id": 1, "titulo": "Dom Casmurro",        "autor": "Machado de Assis", "ano": 1899, "genero": "romance"},
    {"id": 2, "titulo": "O Cortiço",            "autor": "Aluísio Azevedo",  "ano": 1890, "genero": "romance"},
    {"id": 3, "titulo": "Capitães da Areia",    "autor": "Jorge Amado",      "ano": 1937, "genero": "romance"},
    {"id": 4, "titulo": "Memórias Póstumas",    "autor": "Machado de Assis", "ano": 1881, "genero": "romance"},
    {"id": 5, "titulo": "Vidas Secas",          "autor": "Graciliano Ramos", "ano": 1938, "genero": "romance"},
    {"id": 6, "titulo": "Iracema",              "autor": "José de Alencar",  "ano": 1865, "genero": "romance"},
    {"id": 7, "titulo": "O Alienista",          "autor": "Machado de Assis", "ano": 1882, "genero": "conto"},
    {"id": 8, "titulo": "Sagarana",             "autor": "Guimarães Rosa",   "ano": 1946, "genero": "conto"},
]

EMPRESTIMOS_BASE = [
    {"id_livro": 1, "usuario": "Ana",    "dias_restantes": 3},
    {"id_livro": 3, "usuario": "Bruno",  "dias_restantes": 0},
    {"id_livro": 7, "usuario": "Carla",  "dias_restantes": -2},
    {"id_livro": 5, "usuario": "Ana",    "dias_restantes": 10},
]


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def assert_nao_usa_funcoes_proibidas():
    assert funcoes is not None, (
        "Não foi possível importar funcoes_biblioteca. "
        "Verifique se há erro de sintaxe ou uso de input()."
    )
    source = getsource(funcoes)
    tree = ast.parse(source)
    proibidas = ["min", "max", "sum", "filter", "map", "sorted", "count"]
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if hasattr(node, "func") and hasattr(node.func, "id"):
                assert node.func.id not in proibidas, (
                    f"Utilizou a função proibida: {node.func.id}"
                )


def verifica_lista_de_dicts(esperado, obtido, msg):
    marcador = "\n" + "*" * 50 + "\n"
    assert isinstance(obtido, list), f"{marcador}Era esperado uma lista, mas obteve {type(obtido)}.\n{msg}"
    assert len(esperado) == len(obtido), (
        f"{marcador}Tamanho errado: esperado {len(esperado)}, obtido {len(obtido)}.\n{msg}"
    )
    for e in esperado:
        assert e in obtido, f"{marcador}O elemento\n{e}\ndeveria estar na lista.\n{msg}"


def verifica_dicionario(esperado, obtido, msg):
    marcador = "\n" + "*" * 50 + "\n"
    assert isinstance(obtido, dict), f"{marcador}Era esperado um dicionário.\n{msg}"
    for k, v in esperado.items():
        assert k in obtido, f"{marcador}Chave '{k}' não encontrada no dicionário retornado.\n{msg}"
        if isinstance(v, list):
            assert sorted(v) == sorted(obtido[k]), (
                f"{marcador}Valor da chave '{k}' incorreto.\nEsperado: {v}\nObtido: {obtido[k]}\n{msg}"
            )
        else:
            assert v == obtido[k], (
                f"{marcador}Valor da chave '{k}' incorreto.\nEsperado: {v}\nObtido: {obtido[k]}\n{msg}"
            )
    for k in obtido:
        assert k in esperado, f"{marcador}Chave inesperada '{k}' no dicionário retornado.\n{msg}"


# ---------------------------------------------------------------------------
# VERIFICAÇÃO GERAL
# ---------------------------------------------------------------------------

@pytest.mark.timeout(3)
def test_funcoes_nao_possui_prints_nem_inputs():
    assert funcoes is not None, "Não foi possível importar funcoes_biblioteca."
    source = getsource(funcoes)
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            try:
                assert node.func.id != "print", "O arquivo não deve conter print()."
                assert node.func.id != "input", "O arquivo não deve conter input()."
            except AttributeError:
                pass


# ---------------------------------------------------------------------------
# NÍVEL 1 — livros_disponiveis
# ---------------------------------------------------------------------------

def assert_livros_disponiveis(acervo, emprestimos, esperado, exemplo=""):
    assert_nao_usa_funcoes_proibidas()
    assert funcoes and livros_disponiveis, "A função livros_disponiveis não foi definida."
    sig = signature(funcoes.livros_disponiveis)
    assert len(sig.parameters) == 2, (
        f"livros_disponiveis deve receber 2 argumentos, recebeu {len(sig.parameters)}."
    )
    marcador = "\n" + "*" * 50 + "\n"
    msg = (
        f"{marcador}Erro{exemplo}!\n"
        f"Acervo:\n{pformat(acervo)}\n"
        f"Empréstimos:\n{pformat(emprestimos)}\n"
        f"Esperado:\n{pformat(esperado)}\n"
    )
    try:
        obtido = funcoes.livros_disponiveis(deepcopy(acervo), deepcopy(emprestimos))
    except Exception as e:
        pytest.fail(f"{msg}Erro na execução: {type(e).__name__}: {e}")

    msg += f"Obtido:\n{pformat(obtido)}\n"
    verifica_lista_de_dicts(esperado, obtido, msg)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("acervo,emprestimos,esperado", [
    pytest.param(acervo, emp, esp, id=f"livros_disponiveis caso {i}")
    for i, (acervo, emp, esp) in enumerate([
        # Caso base do enunciado
        (
            ACERVO_BASE,
            EMPRESTIMOS_BASE,
            [
                {"id": 2, "titulo": "O Cortiço",         "autor": "Aluísio Azevedo",  "ano": 1890, "genero": "romance"},
                {"id": 4, "titulo": "Memórias Póstumas", "autor": "Machado de Assis", "ano": 1881, "genero": "romance"},
                {"id": 6, "titulo": "Iracema",           "autor": "José de Alencar",  "ano": 1865, "genero": "romance"},
                {"id": 8, "titulo": "Sagarana",          "autor": "Guimarães Rosa",   "ano": 1946, "genero": "conto"},
            ],
        ),
        # Nenhum livro emprestado — todos disponíveis
        (
            ACERVO_BASE,
            [],
            ACERVO_BASE,
        ),
        # Todos os livros emprestados — nenhum disponível
        (
            ACERVO_BASE,
            [
                {"id_livro": 1, "usuario": "X", "dias_restantes": 1},
                {"id_livro": 2, "usuario": "X", "dias_restantes": 1},
                {"id_livro": 3, "usuario": "X", "dias_restantes": 1},
                {"id_livro": 4, "usuario": "X", "dias_restantes": 1},
                {"id_livro": 5, "usuario": "X", "dias_restantes": 1},
                {"id_livro": 6, "usuario": "X", "dias_restantes": 1},
                {"id_livro": 7, "usuario": "X", "dias_restantes": 1},
                {"id_livro": 8, "usuario": "X", "dias_restantes": 1},
            ],
            [],
        ),
        # Apenas um livro emprestado
        (
            ACERVO_BASE,
            [{"id_livro": 8, "usuario": "Bruno", "dias_restantes": 5}],
            [
                {"id": 1, "titulo": "Dom Casmurro",     "autor": "Machado de Assis", "ano": 1899, "genero": "romance"},
                {"id": 2, "titulo": "O Cortiço",         "autor": "Aluísio Azevedo",  "ano": 1890, "genero": "romance"},
                {"id": 3, "titulo": "Capitães da Areia", "autor": "Jorge Amado",      "ano": 1937, "genero": "romance"},
                {"id": 4, "titulo": "Memórias Póstumas", "autor": "Machado de Assis", "ano": 1881, "genero": "romance"},
                {"id": 5, "titulo": "Vidas Secas",       "autor": "Graciliano Ramos", "ano": 1938, "genero": "romance"},
                {"id": 6, "titulo": "Iracema",           "autor": "José de Alencar",  "ano": 1865, "genero": "romance"},
                {"id": 7, "titulo": "O Alienista",       "autor": "Machado de Assis", "ano": 1882, "genero": "conto"},
            ],
        ),
        # Acervo com um único livro, não emprestado
        (
            [{"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "genero": "romance"}],
            [],
            [{"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "genero": "romance"}],
        ),
        # Acervo com um único livro, emprestado
        (
            [{"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "genero": "romance"}],
            [{"id_livro": 1, "usuario": "Ana", "dias_restantes": 2}],
            [],
        ),
    ])
])
def test_nivel1_livros_disponiveis(acervo, emprestimos, esperado):
    assert_livros_disponiveis(acervo, emprestimos, esperado)


# ---------------------------------------------------------------------------
# NÍVEL 1 — emprestimos_em_atraso
# ---------------------------------------------------------------------------

def assert_emprestimos_em_atraso(acervo, emprestimos, esperado, exemplo=""):
    assert_nao_usa_funcoes_proibidas()
    assert funcoes and emprestimos_em_atraso, "A função emprestimos_em_atraso não foi definida."
    sig = signature(funcoes.emprestimos_em_atraso)
    assert len(sig.parameters) == 2, (
        f"emprestimos_em_atraso deve receber 2 argumentos, recebeu {len(sig.parameters)}."
    )
    marcador = "\n" + "*" * 50 + "\n"
    msg = (
        f"{marcador}Erro{exemplo}!\n"
        f"Acervo:\n{pformat(acervo)}\n"
        f"Empréstimos:\n{pformat(emprestimos)}\n"
        f"Esperado:\n{pformat(esperado)}\n"
    )
    try:
        obtido = funcoes.emprestimos_em_atraso(deepcopy(acervo), deepcopy(emprestimos))
    except Exception as e:
        pytest.fail(f"{msg}Erro na execução: {type(e).__name__}: {e}")

    msg += f"Obtido:\n{pformat(obtido)}\n"
    verifica_lista_de_dicts(esperado, obtido, msg)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("acervo,emprestimos,esperado", [
    pytest.param(acervo, emp, esp, id=f"emprestimos_em_atraso caso {i}")
    for i, (acervo, emp, esp) in enumerate([
        # Caso base do enunciado
        (
            ACERVO_BASE,
            EMPRESTIMOS_BASE,
            [
                {"titulo": "Capitães da Areia", "usuario": "Bruno", "dias_restantes": 0},
                {"titulo": "O Alienista",        "usuario": "Carla", "dias_restantes": -2},
            ],
        ),
        # Nenhum atraso
        (
            ACERVO_BASE,
            [
                {"id_livro": 1, "usuario": "Ana",   "dias_restantes": 5},
                {"id_livro": 2, "usuario": "Bruno", "dias_restantes": 1},
            ],
            [],
        ),
        # Todos em atraso
        (
            ACERVO_BASE,
            [
                {"id_livro": 1, "usuario": "Ana",   "dias_restantes": -1},
                {"id_livro": 2, "usuario": "Bruno", "dias_restantes": -5},
                {"id_livro": 3, "usuario": "Carla", "dias_restantes": 0},
            ],
            [
                {"titulo": "Dom Casmurro", "usuario": "Ana",   "dias_restantes": -1},
                {"titulo": "O Cortiço",    "usuario": "Bruno",  "dias_restantes": -5},
                {"titulo": "Capitães da Areia", "usuario": "Carla", "dias_restantes": 0},
            ],
        ),
        # Atraso exatamente zero (limite da condição)
        (
            ACERVO_BASE,
            [{"id_livro": 4, "usuario": "Diego", "dias_restantes": 0}],
            [{"titulo": "Memórias Póstumas", "usuario": "Diego", "dias_restantes": 0}],
        ),
        # Sem empréstimos — sem atrasos
        (
            ACERVO_BASE,
            [],
            [],
        ),
    ])
])
def test_nivel1_emprestimos_em_atraso(acervo, emprestimos, esperado):
    assert_emprestimos_em_atraso(acervo, emprestimos, esperado)


# ---------------------------------------------------------------------------
# NÍVEL 2 — contagem_por_genero
# ---------------------------------------------------------------------------

def assert_contagem_por_genero(acervo, esperado, exemplo=""):
    assert_nao_usa_funcoes_proibidas()
    assert funcoes and contagem_por_genero, "A função contagem_por_genero não foi definida."
    sig = signature(funcoes.contagem_por_genero)
    assert len(sig.parameters) == 1, (
        f"contagem_por_genero deve receber 1 argumento, recebeu {len(sig.parameters)}."
    )
    marcador = "\n" + "*" * 50 + "\n"
    msg = (
        f"{marcador}Erro{exemplo}!\n"
        f"Acervo:\n{pformat(acervo)}\n"
        f"Esperado:\n{pformat(esperado)}\n"
    )
    try:
        obtido = funcoes.contagem_por_genero(deepcopy(acervo))
    except Exception as e:
        pytest.fail(f"{msg}Erro na execução: {type(e).__name__}: {e}")

    msg += f"Obtido:\n{pformat(obtido)}\n"
    verifica_dicionario(esperado, obtido, msg)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("acervo,esperado", [
    pytest.param(acervo, esp, id=f"contagem_por_genero caso {i}")
    for i, (acervo, esp) in enumerate([
        # Caso base do enunciado
        (ACERVO_BASE, {"romance": 6, "conto": 2}),
        # Acervo com um único gênero
        (
            [
                {"id": 1, "titulo": "A", "autor": "X", "ano": 2000, "genero": "romance"},
                {"id": 2, "titulo": "B", "autor": "Y", "ano": 2001, "genero": "romance"},
            ],
            {"romance": 2},
        ),
        # Cada livro tem um gênero diferente
        (
            [
                {"id": 1, "titulo": "A", "autor": "X", "ano": 2000, "genero": "romance"},
                {"id": 2, "titulo": "B", "autor": "Y", "ano": 2001, "genero": "conto"},
                {"id": 3, "titulo": "C", "autor": "Z", "ano": 2002, "genero": "poesia"},
            ],
            {"romance": 1, "conto": 1, "poesia": 1},
        ),
        # Três gêneros com contagens distintas
        (
            [
                {"id": 1, "titulo": "A", "autor": "X", "ano": 1900, "genero": "romance"},
                {"id": 2, "titulo": "B", "autor": "Y", "ano": 1901, "genero": "romance"},
                {"id": 3, "titulo": "C", "autor": "Z", "ano": 1902, "genero": "romance"},
                {"id": 4, "titulo": "D", "autor": "W", "ano": 1903, "genero": "conto"},
                {"id": 5, "titulo": "E", "autor": "V", "ano": 1904, "genero": "poesia"},
                {"id": 6, "titulo": "F", "autor": "U", "ano": 1905, "genero": "poesia"},
            ],
            {"romance": 3, "conto": 1, "poesia": 2},
        ),
        # Um único livro
        (
            [{"id": 1, "titulo": "Solo", "autor": "X", "ano": 2000, "genero": "crônica"}],
            {"crônica": 1},
        ),
    ])
])
def test_nivel2_contagem_por_genero(acervo, esperado):
    assert_contagem_por_genero(acervo, esperado)


# ---------------------------------------------------------------------------
# NÍVEL 2 — autor_mais_emprestado
# ---------------------------------------------------------------------------

def assert_autor_mais_emprestado(acervo, emprestimos, esperado, exemplo=""):
    assert_nao_usa_funcoes_proibidas()
    assert funcoes and autor_mais_emprestado, "A função autor_mais_emprestado não foi definida."
    sig = signature(funcoes.autor_mais_emprestado)
    assert len(sig.parameters) == 2, (
        f"autor_mais_emprestado deve receber 2 argumentos, recebeu {len(sig.parameters)}."
    )
    marcador = "\n" + "*" * 50 + "\n"
    msg = (
        f"{marcador}Erro{exemplo}!\n"
        f"Acervo:\n{pformat(acervo)}\n"
        f"Empréstimos:\n{pformat(emprestimos)}\n"
        f"Esperado: {esperado}\n"
    )
    try:
        obtido = funcoes.autor_mais_emprestado(deepcopy(acervo), deepcopy(emprestimos))
    except Exception as e:
        pytest.fail(f"{msg}Erro na execução: {type(e).__name__}: {e}")

    msg += f"Obtido: {obtido}\n"
    assert isinstance(obtido, str), f"{marcador}Era esperada uma string, obteve {type(obtido)}.\n{msg}"
    assert obtido == esperado, msg


@pytest.mark.timeout(3)
@pytest.mark.parametrize("acervo,emprestimos,esperado", [
    pytest.param(acervo, emp, esp, id=f"autor_mais_emprestado caso {i}")
    for i, (acervo, emp, esp) in enumerate([
        # Caso base do enunciado: Machado tem ids 1 e 7 emprestados (2 livros)
        (
            ACERVO_BASE,
            EMPRESTIMOS_BASE,
            "Machado de Assis",
        ),
        # Apenas um empréstimo
        (
            ACERVO_BASE,
            [{"id_livro": 3, "usuario": "Ana", "dias_restantes": 5}],
            "Jorge Amado",
        ),
        # Dois autores empatados — qualquer um dos dois é aceito
        # (testamos apenas o caso sem empate para garantir determinismo)
        (
            ACERVO_BASE,
            [
                {"id_livro": 2, "usuario": "Ana",   "dias_restantes": 3},
                {"id_livro": 5, "usuario": "Bruno", "dias_restantes": 1},
            ],
            # Aluísio (id 2) e Graciliano (id 5) têm 1 empréstimo cada
            # Sem desempate definido — testamos caso com vencedor claro
            "Aluísio Azevedo",  # só 1 empréstimo, mas é o único com >= 1
        ),
        # Machado com 3 livros emprestados (ids 1, 4, 7)
        (
            ACERVO_BASE,
            [
                {"id_livro": 1, "usuario": "Ana",   "dias_restantes": 2},
                {"id_livro": 4, "usuario": "Bruno", "dias_restantes": 7},
                {"id_livro": 7, "usuario": "Carla", "dias_restantes": -1},
                {"id_livro": 2, "usuario": "Diego", "dias_restantes": 4},
            ],
            "Machado de Assis",
        ),
        # Graciliano é o único com livro emprestado
        (
            ACERVO_BASE,
            [{"id_livro": 5, "usuario": "Eva", "dias_restantes": 0}],
            "Graciliano Ramos",
        ),
    ])
])
def test_nivel2_autor_mais_emprestado(acervo, emprestimos, esperado):
    assert_autor_mais_emprestado(acervo, emprestimos, esperado)


# ---------------------------------------------------------------------------
# NÍVEL 3 — relatorio_usuario
# ---------------------------------------------------------------------------

def assert_relatorio_usuario(acervo, emprestimos, usuario, esperado, exemplo=""):
    assert_nao_usa_funcoes_proibidas()
    assert funcoes and relatorio_usuario, "A função relatorio_usuario não foi definida."
    sig = signature(funcoes.relatorio_usuario)
    assert len(sig.parameters) == 3, (
        f"relatorio_usuario deve receber 3 argumentos, recebeu {len(sig.parameters)}."
    )
    marcador = "\n" + "*" * 50 + "\n"
    msg = (
        f"{marcador}Erro{exemplo}!\n"
        f"Usuário: {usuario}\n"
        f"Acervo:\n{pformat(acervo)}\n"
        f"Empréstimos:\n{pformat(emprestimos)}\n"
        f"Esperado:\n{pformat(esperado)}\n"
    )
    try:
        obtido = funcoes.relatorio_usuario(deepcopy(acervo), deepcopy(emprestimos), usuario)
    except Exception as e:
        pytest.fail(f"{msg}Erro na execução: {type(e).__name__}: {e}")

    msg += f"Obtido:\n{pformat(obtido)}\n"
    verifica_dicionario(esperado, obtido, msg)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("acervo,emprestimos,usuario,esperado", [
    pytest.param(acervo, emp, usr, esp, id=f"relatorio_usuario caso {i}")
    for i, (acervo, emp, usr, esp) in enumerate([
        # Caso base do enunciado — Ana tem 2 livros no prazo, nenhum atrasado
        (
            ACERVO_BASE,
            EMPRESTIMOS_BASE,
            "Ana",
            {
                "usuario": "Ana",
                "livros_com_prazo": ["Dom Casmurro", "Vidas Secas"],
                "livros_atrasados": [],
                "total_emprestimos": 2,
            },
        ),
        # Bruno tem 1 livro com dias_restantes == 0 (atrasado)
        (
            ACERVO_BASE,
            EMPRESTIMOS_BASE,
            "Bruno",
            {
                "usuario": "Bruno",
                "livros_com_prazo": [],
                "livros_atrasados": ["Capitães da Areia"],
                "total_emprestimos": 1,
            },
        ),
        # Carla tem 1 livro com dias_restantes negativo (atrasado)
        (
            ACERVO_BASE,
            EMPRESTIMOS_BASE,
            "Carla",
            {
                "usuario": "Carla",
                "livros_com_prazo": [],
                "livros_atrasados": ["O Alienista"],
                "total_emprestimos": 1,
            },
        ),
        # Usuário sem nenhum empréstimo
        (
            ACERVO_BASE,
            EMPRESTIMOS_BASE,
            "Diego",
            {
                "usuario": "Diego",
                "livros_com_prazo": [],
                "livros_atrasados": [],
                "total_emprestimos": 0,
            },
        ),
        # Usuário com livros nos dois estados (prazo e atraso)
        (
            ACERVO_BASE,
            [
                {"id_livro": 1, "usuario": "Eva", "dias_restantes": 5},
                {"id_livro": 2, "usuario": "Eva", "dias_restantes": -3},
                {"id_livro": 3, "usuario": "Eva", "dias_restantes": 0},
                {"id_livro": 4, "usuario": "Eva", "dias_restantes": 1},
            ],
            "Eva",
            {
                "usuario": "Eva",
                "livros_com_prazo": ["Dom Casmurro", "Memórias Póstumas"],
                "livros_atrasados": ["O Cortiço", "Capitães da Areia"],
                "total_emprestimos": 4,
            },
        ),
    ])
])
def test_nivel3_relatorio_usuario(acervo, emprestimos, usuario, esperado):
    assert_relatorio_usuario(acervo, emprestimos, usuario, esperado)


# ---------------------------------------------------------------------------
# NÍVEL 3 — livro_mais_antigo_disponivel
# ---------------------------------------------------------------------------

def assert_livro_mais_antigo_disponivel(acervo, emprestimos, esperado, exemplo=""):
    assert_nao_usa_funcoes_proibidas()
    assert funcoes and livro_mais_antigo_disponivel, "A função livro_mais_antigo_disponivel não foi definida."
    sig = signature(funcoes.livro_mais_antigo_disponivel)
    assert len(sig.parameters) == 2, (
        f"livro_mais_antigo_disponivel deve receber 2 argumentos, recebeu {len(sig.parameters)}."
    )
    marcador = "\n" + "*" * 50 + "\n"
    msg = (
        f"{marcador}Erro{exemplo}!\n"
        f"Acervo:\n{pformat(acervo)}\n"
        f"Empréstimos:\n{pformat(emprestimos)}\n"
        f"Esperado:\n{pformat(esperado)}\n"
    )
    try:
        obtido = funcoes.livro_mais_antigo_disponivel(deepcopy(acervo), deepcopy(emprestimos))
    except Exception as e:
        pytest.fail(f"{msg}Erro na execução: {type(e).__name__}: {e}")

    msg += f"Obtido:\n{pformat(obtido)}\n"
    assert isinstance(obtido, dict), f"{marcador}Era esperado um dicionário.\n{msg}"
    verifica_dicionario(esperado, obtido, msg)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("acervo,emprestimos,esperado", [
    pytest.param(acervo, emp, esp, id=f"livro_mais_antigo_disponivel caso {i}")
    for i, (acervo, emp, esp) in enumerate([
        # Caso base: Iracema (1865) é o disponível mais antigo
        (
            ACERVO_BASE,
            EMPRESTIMOS_BASE,
            {"id": 6, "titulo": "Iracema", "autor": "José de Alencar", "ano": 1865, "genero": "romance"},
        ),
        # Sem empréstimos: Iracema (1865) continua sendo o mais antigo do acervo
        (
            ACERVO_BASE,
            [],
            {"id": 6, "titulo": "Iracema", "autor": "José de Alencar", "ano": 1865, "genero": "romance"},
        ),
        # Iracema emprestada: próximo mais antigo disponível é Memórias Póstumas (1881)
        (
            ACERVO_BASE,
            [{"id_livro": 6, "usuario": "Ana", "dias_restantes": 3}],
            {"id": 4, "titulo": "Memórias Póstumas", "autor": "Machado de Assis", "ano": 1881, "genero": "romance"},
        ),
        # Apenas um livro no acervo, disponível
        (
            [{"id": 1, "titulo": "Único", "autor": "Autor X", "ano": 1800, "genero": "romance"}],
            [],
            {"id": 1, "titulo": "Único", "autor": "Autor X", "ano": 1800, "genero": "romance"},
        ),
        # Todos emprestados exceto o mais recente (Sagarana 1946)
        (
            ACERVO_BASE,
            [
                {"id_livro": 1, "usuario": "X", "dias_restantes": 1},
                {"id_livro": 2, "usuario": "X", "dias_restantes": 1},
                {"id_livro": 3, "usuario": "X", "dias_restantes": 1},
                {"id_livro": 4, "usuario": "X", "dias_restantes": 1},
                {"id_livro": 5, "usuario": "X", "dias_restantes": 1},
                {"id_livro": 6, "usuario": "X", "dias_restantes": 1},
                {"id_livro": 7, "usuario": "X", "dias_restantes": 1},
            ],
            {"id": 8, "titulo": "Sagarana", "autor": "Guimarães Rosa", "ano": 1946, "genero": "conto"},
        ),
    ])
])
def test_nivel3_livro_mais_antigo_disponivel(acervo, emprestimos, esperado):
    assert_livro_mais_antigo_disponivel(acervo, emprestimos, esperado)
