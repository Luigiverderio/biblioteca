# Desafio Pre-Prova - Biblioteca

Projeto de treino para praticar logica de programacao com Python, usando testes automatizados para validar a solucao.

## O que voce precisa fazer

1. Ler o enunciado no navegador.
2. Implementar as funcoes no arquivo de solucao.
3. Rodar os testes e corrigir ate passar tudo.

## Setup rapido

Antes de rodar qualquer comando, entre na pasta do projeto.

No Windows (PowerShell):

```bash
cd "C:\Users\luigi\OneDrive\Área de Trabalho\Insper\Estudos\biblioteca"
```

No macOS (zsh/bash):

```bash
cd ~/caminho/para/biblioteca
```

### 1) Instalar Node.js (o npm vem junto)

No Windows:

```bash
winget install OpenJS.NodeJS.LTS
```

No macOS (Homebrew):

```bash
brew install node
```

Se voce nao usa Homebrew, pode instalar pelo instalador oficial em nodejs.org.

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

Recomendado: usar ambiente virtual (venv).

Se ainda nao estiver na pasta do projeto, entre nela:

No Windows (PowerShell):

```bash
cd "C:\Users\luigi\OneDrive\Área de Trabalho\Insper\Estudos\biblioteca"
```

No macOS (zsh/bash):

```bash
cd ~/caminho/para/biblioteca
```

No Windows (PowerShell):

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

No macOS (zsh/bash):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependencias de teste:

```bash
pip install pytest pytest-timeout
```

Agora rode os testes:

```bash
pytest -q
```

## Prompt pronto para configurar testes no VS Code

Se quiser automatizar isso com Copilot Chat, copie e cole o prompt abaixo:

```text
Configure o ambiente de testes Python deste repositório no VS Code, sem perguntar nada.
1. Selecione Pytest como framework.
2. Use a pasta raiz do projeto para descoberta.
3. Use padrão de arquivos test_*.py.
4. Garanta que o interpretador ativo seja da venv do projeto:
	- prefira .venv
	- se não existir, use .venv_clean
5. Se faltar dependência, instale na venv ativa: pytest e pytest-timeout.
6. Crie ou ajuste as configurações necessárias para o VS Code não pedir isso de novo.
7. Rode descoberta de testes e execute pytest -q.
8. No fim, mostre um resumo curto com:
	- interpretador selecionado
	- pacotes instalados
	- quantidade de testes descobertos
	- resultado da execução
```

## Estrutura principal

- index.html e src/: interface com o enunciado
- test_solution.py: testes automatizados
- funcoes_biblioteca.py: arquivo da sua implementacao
- Gabarito.py: referencia de solucao

Bom estudo e boa prova.
