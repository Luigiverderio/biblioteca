export default function BibliotecaPrairieLearn() {
  const acervo = `acervo = [
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
]`;

  const niveis = [
    {
      badge: "NÍVEL 1",
      titulo: "livros_disponiveis",
      descricao:
        "Implemente a função que retorna todos os livros que não estão emprestados.",
      assinatura: "def livros_disponiveis(acervo, emprestimos):",
      retorno: "Retorna uma lista de dicionários com os livros disponíveis.",
      saida: `[
    {"id": 2, "titulo": "O Cortiço",         "autor": "Aluísio Azevedo", "ano": 1890, "genero": "romance"},
    {"id": 4, "titulo": "Memórias Póstumas", "autor": "Machado de Assis", "ano": 1881, "genero": "romance"},
    {"id": 6, "titulo": "Iracema",           "autor": "José de Alencar",  "ano": 1865, "genero": "romance"},
    {"id": 8, "titulo": "Sagarana",          "autor": "Guimarães Rosa",   "ano": 1946, "genero": "conto"},
]`,
    },
    {
      badge: "NÍVEL 1",
      titulo: "emprestimos_em_atraso",
      descricao:
        "Implemente a função que retorna os títulos dos livros com empréstimo em atraso (dias_restantes ≤ 0), junto com o usuário responsável.",
      assinatura: "def emprestimos_em_atraso(acervo, emprestimos):",
      retorno:
        'Retorna uma lista de dicionários com as chaves "titulo", "usuario" e "dias_restantes".',
      saida: `[
    {"titulo": "Capitães da Areia", "usuario": "Bruno", "dias_restantes": 0},
    {"titulo": "O Alienista",       "usuario": "Carla", "dias_restantes": -2},
]`,
    },
    {
      badge: "NÍVEL 2",
      titulo: "contagem_por_genero",
      descricao:
        "Implemente a função que conta quantos livros existem em cada gênero no acervo completo.",
      assinatura: "def contagem_por_genero(acervo):",
      retorno:
        "Retorna um dicionário onde cada chave é um gênero e o valor é a quantidade de livros daquele gênero.",
      saida: '{"romance": 6, "conto": 2}',
    },
    {
      badge: "NÍVEL 2",
      titulo: "autor_mais_emprestado",
      descricao:
        "Implemente a função que descobre qual autor tem mais livros emprestados no momento.",
      assinatura: "def autor_mais_emprestado(acervo, emprestimos):",
      retorno: 'Retorna uma string com o nome do autor.\n\nSaída esperada: "Machado de Assis"',
      saida:
        'Dica: use um dicionário auxiliar para acumular contagens por autor enquanto percorre os empréstimos.',
    },
    {
      badge: "NÍVEL 3",
      titulo: "relatorio_usuario",
      descricao:
        "Implemente a função que gera um relatório completo de um usuário específico.",
      assinatura: "def relatorio_usuario(acervo, emprestimos, nome_usuario):",
      retorno:
        'Retorna um dicionário com as chaves "usuario", "livros_com_prazo", "livros_atrasados" e "total_emprestimos".',
      saida: `{
    "usuario": "Ana",
    "livros_com_prazo": ["Dom Casmurro", "Vidas Secas"],
    "livros_atrasados": [],
    "total_emprestimos": 2
}`,
    },
    {
      badge: "NÍVEL 3",
      titulo: "livro_mais_antigo_disponivel",
      descricao:
        "Implemente a função que encontra o livro disponível mais antigo do acervo (menor ano de publicação), sem usar min.",
      assinatura: "def livro_mais_antigo_disponivel(acervo, emprestimos):",
      retorno: "Retorna um dicionário com os dados do livro.",
      saida:
        '{"id": 6, "titulo": "Iracema", "autor": "José de Alencar", "ano": 1865, "genero": "romance"}',
    },
  ];

  const Code = ({ children }) => (
    <pre className="overflow-x-auto rounded-2xl border border-slate-200 bg-slate-950 p-4 text-sm leading-6 text-slate-100 shadow-sm">
      <code>{children}</code>
    </pre>
  );

  const Section = ({ item }) => (
    <section className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
      <div className="mb-4 flex items-center gap-3">
        <span className="rounded-full bg-emerald-50 px-3 py-1 text-xs font-semibold tracking-wide text-emerald-700">
          {item.badge}
        </span>
        <h3 className="text-xl font-semibold text-slate-900">{item.titulo}</h3>
      </div>

      <p className="mb-4 text-sm leading-7 text-slate-700">{item.descricao}</p>

      <div className="mb-4 rounded-2xl border border-slate-200 bg-slate-50 p-4 text-sm text-slate-800">
        <div className="mb-2 text-xs font-semibold uppercase tracking-wide text-slate-500">
          Assinatura
        </div>
        <code className="font-mono">{item.assinatura}</code>
      </div>

      <p className="mb-4 whitespace-pre-line text-sm leading-7 text-slate-700">{item.retorno}</p>

      <div>
        <div className="mb-2 text-xs font-semibold uppercase tracking-wide text-slate-500">
          Saída esperada
        </div>
        <Code>{item.saida}</Code>
      </div>
    </section>
  );

  return (
    <div className="min-h-screen bg-slate-100 text-slate-900">
      <header className="border-b border-slate-200 bg-white/95 backdrop-blur">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
          <div>
            <div className="text-sm font-medium text-slate-500">PrairieLearn</div>
            <h1 className="text-2xl font-bold tracking-tight">Sistema de gerenciamento de biblioteca</h1>
          </div>
          <div className="hidden items-center gap-3 md:flex">
            <span className="rounded-full bg-amber-100 px-3 py-1 text-sm font-semibold text-amber-800">
              Programação com listas e dicionários
            </span>
            <button className="rounded-2xl border border-slate-200 px-4 py-2 text-sm font-medium text-slate-700 shadow-sm">
              Open workspace
            </button>
          </div>
        </div>
      </header>

      <main className="mx-auto grid max-w-7xl grid-cols-1 gap-6 px-6 py-6 lg:grid-cols-[minmax(0,1fr)_320px]">
        <div className="space-y-6">
          <section className="rounded-3xl border border-slate-200 bg-white p-7 shadow-sm">
            <div className="mb-4 flex flex-wrap items-center gap-3">
              <span className="rounded-full bg-sky-100 px-3 py-1 text-xs font-semibold tracking-wide text-sky-700">
                DESCRIÇÃO DO PROBLEMA
              </span>
              <span className="rounded-full bg-rose-100 px-3 py-1 text-xs font-semibold tracking-wide text-rose-700">
                Proibido usar sum, min, max, sorted, count e afins
              </span>
            </div>

            <p className="mb-4 text-[15px] leading-7 text-slate-700">
              Você deve implementar funções para gerenciar o acervo e os empréstimos de uma biblioteca usando
              dicionários, listas e estruturas de repetição. Todas as operações devem ser feitas manualmente com laços.
            </p>

            <p className="mb-4 text-[15px] leading-7 text-slate-700">
              Uma biblioteca mantém seu acervo como uma lista de dicionários, onde cada dicionário representa um livro.
              Os empréstimos ativos são armazenados em uma lista separada. Um livro está disponível se seu id não aparece
              em nenhum empréstimo. Dias negativos ou zero significam atraso.
            </p>

            <Code>{acervo}</Code>
          </section>

          {niveis.map((item, index) => (
            <Section item={item} key={index} />
          ))}
        </div>

        <aside className="space-y-6">
          <div className="rounded-3xl border border-slate-200 bg-white p-5 shadow-sm">
            <div className="mb-3 text-sm font-semibold text-slate-900">Sobre a correção</div>
            <p className="text-sm leading-6 text-slate-700">
              As soluções podem ser avaliadas por testes automáticos. Mesmo com testes passando, a implementação pode
              ser revisada manualmente se não respeitar as restrições do enunciado.
            </p>
          </div>

          <div className="rounded-3xl border border-slate-200 bg-white p-5 shadow-sm">
            <div className="mb-3 text-sm font-semibold text-slate-900">Checklist</div>
            <div className="space-y-3 text-sm text-slate-700">
              <div className="flex items-center gap-3"><span>✅</span><span>Usar laços manualmente</span></div>
              <div className="flex items-center gap-3"><span>✅</span><span>Manipular listas e dicionários</span></div>
              <div className="flex items-center gap-3"><span>✅</span><span>Evitar funções prontas proibidas</span></div>
              <div className="flex items-center gap-3"><span>✅</span><span>Retornar exatamente o formato pedido</span></div>
            </div>
          </div>

          <div className="rounded-3xl border border-slate-200 bg-slate-900 p-5 text-slate-100 shadow-sm">
            <div className="mb-2 text-sm font-semibold">Resumo rápido</div>
            <div className="space-y-2 text-sm text-slate-300">
              <p>6 funções</p>
              <p>3 níveis de dificuldade</p>
              <p>Dados de entrada já definidos no enunciado</p>
              <p>Foco em lógica com estruturas básicas</p>
            </div>
          </div>
        </aside>
      </main>
    </div>
  );
}
