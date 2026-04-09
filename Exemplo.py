from funcoes_biblioteca import *

acervo = [
    {"id": 1, "titulo": "Dom Casmurro",        "autor": "Machado de Assis", "ano": 1899, "genero": "romance"},
    {"id": 2, "titulo": "O Cortiço",            "autor": "Aluísio Azevedo",  "ano": 1890, "genero": "romance"},
    {"id": 3, "titulo": "Capitães da Areia",    "autor": "Jorge Amado",      "ano": 1937, "genero": "romance"},
    {"id": 4, "titulo": "Memórias Póstumas",    "autor": "Machado de Assis", "ano": 1881, "genero": "romance"},
    {"id": 5, "titulo": "Vidas Secas",          "autor": "Graciliano Ramos", "ano": 1938, "genero": "romance"},
    {"id": 6, "titulo": "Iracema",              "autor": "José de Alencar",  "ano": 1865, "genero": "romance"},
    {"id": 7, "titulo": "O Alienista",          "autor": "Machado de Assis", "ano": 1882, "genero": "conto"},
    {"id": 8, "titulo": "Sagarana",             "autor": "Guimarães Rosa",   "ano": 1946, "genero": "conto"},
]

emprestimos = [
    {"id_livro": 1, "usuario": "Ana",    "dias_restantes": 3},
    {"id_livro": 3, "usuario": "Bruno",  "dias_restantes": 0},
    {"id_livro": 7, "usuario": "Carla",  "dias_restantes": -2},
    {"id_livro": 5, "usuario": "Ana",    "dias_restantes": 10},
]

print(livros_disponiveis(acervo, emprestimos))

# Saída esperada:
'''
[
    {"id": 2, "titulo": "O Cortiço",         "autor": "Aluísio Azevedo", "ano": 1890, "genero": "romance"},
    {"id": 4, "titulo": "Memórias Póstumas", "autor": "Machado de Assis", "ano": 1881, "genero": "romance"},
    {"id": 6, "titulo": "Iracema",           "autor": "José de Alencar",  "ano": 1865, "genero": "romance"},
    {"id": 8, "titulo": "Sagarana",          "autor": "Guimarães Rosa",   "ano": 1946, "genero": "conto"},
]
'''

print(emprestimos_em_atraso(acervo, emprestimos))



# Saída esperada
'''
[
    {"titulo": "Capitães da Areia", "usuario": "Bruno", "dias_restantes": 0},
    {"titulo": "O Alienista",       "usuario": "Carla", "dias_restantes": -2},
]
'''
print(contagem_por_genero(acervo))


# Saída esperada:
## {"romance": 6, "conto": 2}

print(autor_mais_emprestado(acervo, emprestimos))

# Saída esperada: "Machado de Assis"

print(relatorio_usuario(acervo, emprestimos, nome_usuario))

# Saída esperada:

'''
{
    "usuario": "Ana",
    "livros_com_prazo": ["Dom Casmurro", "Vidas Secas"],
    "livros_atrasados": [],
    "total_emprestimos": 2
}
'''

print(ivro_mais_antigo_disponivel(acervo, emprestimos))

# Saída esperada:
# {"id": 6, "titulo": "Iracema", "autor": "José de Alencar", "ano": 1865, "genero": "romance"}