def livros_disponiveis(acervo, emprestimos):
    ids_emprestados = []
    for emp in emprestimos:
        ids_emprestados.append(emp["id_livro"])

    disponiveis = []
    for livro in acervo:
        disponivel = True
        for id_emp in ids_emprestados:
            if livro["id"] == id_emp:
                disponivel = False
        if disponivel:
            disponiveis.append(livro)
    return disponiveis


def emprestimos_em_atraso(acervo, emprestimos):
    atrasados = []
    for emp in emprestimos:
        if emp["dias_restantes"] <= 0:
            for livro in acervo:
                if livro["id"] == emp["id_livro"]:
                    atrasados.append({
                        "titulo": livro["titulo"],
                        "usuario": emp["usuario"],
                        "dias_restantes": emp["dias_restantes"],
                    })
    return atrasados


def contagem_por_genero(acervo):
    contagem = {}
    for livro in acervo:
        genero = livro["genero"]
        if genero not in contagem:
            contagem[genero] = 0
        contagem[genero] = contagem[genero] + 1
    return contagem


def autor_mais_emprestado(acervo, emprestimos):
    contagem = {}
    for emp in emprestimos:
        for livro in acervo:
            if livro["id"] == emp["id_livro"]:
                autor = livro["autor"]
                if autor not in contagem:
                    contagem[autor] = 0
                contagem[autor] = contagem[autor] + 1

    mais_emprestado = ""
    maior = 0
    for autor in contagem:
        if contagem[autor] > maior:
            maior = contagem[autor]
            mais_emprestado = autor
    return mais_emprestado


def relatorio_usuario(acervo, emprestimos, nome_usuario):
    com_prazo = []
    atrasados = []
    total = 0

    for emp in emprestimos:
        if emp["usuario"] == nome_usuario:
            total = total + 1
            for livro in acervo:
                if livro["id"] == emp["id_livro"]:
                    if emp["dias_restantes"] > 0:
                        com_prazo.append(livro["titulo"])
                    else:
                        atrasados.append(livro["titulo"])

    return {
        "usuario": nome_usuario,
        "livros_com_prazo": com_prazo,
        "livros_atrasados": atrasados,
        "total_emprestimos": total,
    }


def livro_mais_antigo_disponivel(acervo, emprestimos):
    ids_emprestados = []
    for emp in emprestimos:
        ids_emprestados.append(emp["id_livro"])

    mais_antigo = None
    for livro in acervo:
        emprestado = False
        for id_emp in ids_emprestados:
            if livro["id"] == id_emp:
                emprestado = True
        if not emprestado:
            if mais_antigo is None or livro["ano"] < mais_antigo["ano"]:
                mais_antigo = livro
    return mais_antigo
