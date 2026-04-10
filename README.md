# Desafio Pre-Prova - Biblioteca

Projeto de treino para praticar logica de programacao com Python, com testes automatizados para validar a solucao.

## Objetivo

1. Abrir o enunciado no navegador.
2. Implementar as funcoes em `funcoes_biblioteca.py`.
3. Rodar os testes ate passar tudo.

## Como clonar e instalar

Clone este repositorio na sua maquina:

```bash
git clone https://github.com/Luigiverderio/biblioteca.git
```

Entre na pasta do projeto:

```bash
cd biblioteca
```

Instale as dependencias e abra o enunciado:

```bash
npm install
npm run dev
```

No terminal, abra o link exibido (geralmente `http://localhost:5173`).

## Passo a passo completo

### 1) Instalar Node.js (com npm)

Windows:

```bash
winget install OpenJS.NodeJS.LTS
```

macOS (Homebrew):

```bash
brew install node
```

Se preferir, use o instalador oficial em nodejs.org.

### 2) Confirmar instalacao

```bash
node -v
npm -v
```

### 3) Instalar dependencias e abrir o enunciado

```bash
npm install
npm run dev
```

## Onde implementar

Implemente sua solucao em `funcoes_biblioteca.py`.

`Gabarito.py` pode ser usado como referencia.

## Rodando os testes (recomendado)

Use ambiente virtual para evitar conflito de pacotes.

Se ainda nao estiver na pasta do projeto, entre com:

```bash
cd biblioteca
```

Crie e ative a venv:

Windows:

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale dependencias de teste e execute:

```bash
pip install pytest pytest-timeout
pytest -q
```

## VS Code: configurar Testing pelo terminal (testes)

No Windows (PowerShell), este comando cria `.vscode/settings.json` com Pytest habilitado:

```bash
New-Item -ItemType Directory -Force .vscode | Out-Null
@'
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "python.testing.pytestArgs": [".", "-q"],
  "python.testing.cwd": "${workspaceFolder}"
}
'@ | Set-Content .vscode/settings.json -Encoding UTF8
```

Bom estudo e boa prova.
