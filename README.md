<h1 align="center">📋 Gerenciador de Usuários CLI</h1>

<p align="center">
  💻 Projeto pessoal em Python para gerenciamento de cadastros <br>
  🗄️ Persistência de dados em banco SQLite com arquitetura modular
</p>

---

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?color=00FF00&size=22&center=true&vCenter=true&width=700&lines=CRUD+em+Python...;Banco+de+Dados+SQLite...;Arquitetura+Modular...;Tratamento+de+Exceções..." />
</p>

---

## 🚀 Sobre o projeto

Este projeto consiste em um sistema CRUD desenvolvido em Python para gerenciamento de pessoas através de uma interface de linha de comando (CLI).

A aplicação permite cadastrar, listar, buscar, atualizar e excluir registros armazenados em um banco de dados SQLite, utilizando SQL para realizar as operações de persistência dos dados.

Durante o desenvolvimento, o projeto foi estruturado seguindo o princípio da separação de responsabilidades, dividindo a aplicação em módulos responsáveis pela interface com o usuário, lógica de execução e acesso ao banco de dados.

O projeto também utiliza tratamento de exceções para lidar com possíveis erros durante as operações de banco de dados, além de validações de entrada para garantir maior consistência dos dados fornecidos pelo usuário.

Trata-se de um projeto **100% autoral**, desenvolvido com o objetivo de praticar programação em Python, integração com bancos de dados relacionais, SQL, operações CRUD, modularização e boas práticas de desenvolvimento.

---

## 🖥️ Tecnologias utilizadas

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,sqlite" />
</p>

---

## 🎯 Funcionalidades

* 👤 Cadastro de novas pessoas
* 📋 Listagem de todas as pessoas cadastradas
* 🔍 Busca de uma pessoa por ID
* ✏️ Atualização dos dados de uma pessoa
* 🗑️ Exclusão de uma pessoa cadastrada
* 💾 Persistência de dados em banco SQLite
* 🗄️ Criação automática da tabela no banco de dados
* 🔐 Uso de consultas parametrizadas para execução segura de SQL
* ✅ Validação de entradas do usuário
* ⚠️ Tratamento de exceções com `try` / `except`
* 🔄 Controle de transações com `commit()` e `rollback()`
* 🧩 Arquitetura modular com separação de responsabilidades

---

## 🏗️ Estrutura do projeto

```text
crud-cadastro/
├── database/
│   ├── __init__.py
│   └── db.py
├── interface/
│   ├── __init__.py
│   └── menu.py
├── main.py
├── .gitignore
└── README.md
```

### 📂 Organização

* `database/` → Responsável pela conexão e pelas operações realizadas no banco de dados SQLite.
* `interface/` → Responsável pela interação com o usuário, validação das entradas e apresentação das informações no terminal.
* `main.py` → Responsável por coordenar o fluxo principal da aplicação.

---

## 🌐 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/LucasBenfatti14/users-manager
```

### 2. Acesse a pasta do projeto

```bash
cd users-manager
```

### 3. Execute a aplicação

```bash
python main.py
```

O banco de dados SQLite será criado automaticamente na primeira execução, assim como a tabela necessária para armazenar os registros.

---

## 💡 Aprendizados

* Fundamentos de bancos de dados relacionais
* Integração de Python com SQLite
* Utilização da biblioteca `sqlite3`
* Criação e gerenciamento de conexões com banco de dados
* Utilização de `cursor` para execução de comandos SQL
* Execução de comandos SQL através de `execute()`
* Operações CRUD com SQL
* Utilização de `fetchone()` e `fetchall()`
* Controle de transações com `commit()` e `rollback()`
* Gerenciamento de recursos com `try`, `except` e `finally`
* Tratamento de exceções específicas do SQLite
* Consultas parametrizadas com placeholders (`?`)
* Modularização de projetos Python
* Separação de responsabilidades
* Validação de dados de entrada
* Organização de aplicações em múltiplos módulos
* Desenvolvimento de aplicações CLI

---

## 🚧 Próximos passos

* 🔄 Melhorar o gerenciamento de conexões utilizando `with`
* 🧱 Criar uma camada de serviço para separar a lógica de negócio do acesso ao banco
* 🧪 Adicionar testes automatizados
* 📝 Implementar logs da aplicação
* 🔐 Aprimorar as validações e regras de negócio
* 🌐 Desenvolver uma API REST utilizando Flask ou FastAPI

---

## 👨‍💻 Autor

<p align="center">
  Lucas Benfatti <br>
  📍 Santos - SP
</p>

---

<p align="center">
  🚀 Em constante evolução
</p>
