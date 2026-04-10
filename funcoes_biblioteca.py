from enum import auto


def livros_disponiveis(acervo, emprestimos):
    alugados = []
    disponiveis = []
    for livro_alugado in emprestimos:
        alugados.append(livro_alugado['id_livro'])
    for livro in acervo:
        if livro['id'] not in alugados:
            disponiveis.append(livro)

    return disponiveis

def emprestimos_em_atraso(acervo,emprestimos):
    saida = []
    for livro in emprestimos:
        if livro['dias_restantes'] <= 0:
            for book in acervo:
                if livro['id_livro'] == book['id']:
                    saida.append({
                        "titulo": book['titulo'],
                        'usuario': livro['usuario'],
                        'dias_restantes': livro['dias_restantes']
                    })
    return saida

def contagem_por_genero(acervo):
    livro_quantidade = {}
    for livro in acervo:
        if livro['genero'] not in livro_quantidade:
            livro_quantidade[livro['genero']] = 1
        else: 
            livro_quantidade[livro['genero']] +=1
    return livro_quantidade

def autor_mais_emprestado(acervo,emprestimos):
    autor_qtd = {}
    autor_mais_emprestado = ''
    maior_qtd = -1
    for emprestado in emprestimos:
        for livro in acervo:
            if livro['id'] == emprestado['id_livro']:
                if livro['autor'] not in autor_qtd:
                    autor_qtd[livro['autor']] = 1
                else:
                    autor_qtd[livro['autor']] +=1
    
    for autor,valor in autor_qtd.items():
        if valor > maior_qtd:
            maior_qtd = valor
            autor_mais_emprestado = autor

    return autor_mais_emprestado

def relatorio_usuario(acervo,emprestimos,nome_usuario):
    relatorio = {}
    relatorio['usuario'] = nome_usuario
    relatorio['total_emprestimos'] = 0
    relatorio['livros_com_prazo'] = []
    relatorio['livros_atrasados'] = []

    for livro in acervo:
        for emprestimo in emprestimos:
            if emprestimo['id_livro'] == livro['id']:
                if emprestimo['usuario'] == nome_usuario:
                    relatorio['total_emprestimos'] += 1
                    if emprestimo['dias_restantes']>0:
                        if relatorio['livros_com_prazo'] != []:
                            relatorio['livros_com_prazo'] += [livro['titulo']]
                        else:
                            relatorio['livros_com_prazo'] = [livro['titulo']]
                    else:
                        if relatorio['livros_atrasados'] != []:
                            relatorio['livros_atrasados'] += [livro['titulo']]
                        else:
                            relatorio['livros_atrasados'] = [livro['titulo']]
    return relatorio

def livro_mais_antigo_disponivel(acervo, emprestimo):
    livros_disp = livros_disponiveis(acervo,emprestimo)
    ano_mais_antigo = float('inf')
    livro_antigo = {}
    for livro in livros_disp:
        if livro['ano'] < ano_mais_antigo:
            ano_mais_antigo = livro['ano']
            livro_antigo = livro
    return livro_antigo
    




