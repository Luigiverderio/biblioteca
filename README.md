# Desafio Pre-Prova - Biblioteca

Projeto de treino para praticar logica de programacao com Python, usando testes automatizados para validar a solucao.

## O que voce precisa fazer

1. Ler o enunciado no navegador.
2. Implementar as funcoes no arquivo de solucao.
3. Rodar os testes e corrigir ate passar tudo.

## Setup rapido

### 1) Instalar Node.js (o npm vem junto)

No Windows:

```bash
winget install OpenJS.NodeJS.LTS
```

### 2) Confirmar instalacao

```bash
node -v
npm -v
```

### 3) Instalar dependencias do front

```bash
npm install
```

### 4) Abrir o enunciado

```bash
npm run dev
```

Depois disso, abra o link mostrado no terminal (normalmente http://localhost:5173).

Se voce nao puder instalar o Node agora, ainda da para fazer quase tudo do desafio usando apenas Python:

1. Edite o arquivo funcoes_biblioteca.py.
2. Rode os testes com pytest para validar sua solucao.

Nesse caso, voce so nao vai abrir o enunciado via npm run dev.

## Onde escrever a solucao

Implemente sua resposta no arquivo:

- funcoes_biblioteca.py

## Como rodar os testes

Se voce ja tiver o pytest instalado:

```bash
pytest -q
```

Se nao tiver:

```bash
pip install pytest
pytest -q
```

## Estrutura principal

- index.html e src/: interface com o enunciado
- test_solution.py: testes automatizados
- funcoes_biblioteca.py: arquivo da sua implementacao
- Gabarito.py: referencia de solucao

Bom estudo e boa prova.
