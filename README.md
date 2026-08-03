<h1 align="center">📋 Gerenciador de Usuários CLI</h1>

<p align="center">
  💻 Sistema CRUD desenvolvido em Python para gerenciamento de pessoas <br>
  🗄️ Persistência em SQLite com arquitetura em camadas e separação de responsabilidades
</p>

---

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?color=00FF00&size=22&center=true&vCenter=true&width=700&lines=CRUD+em+Python...;Banco+de+Dados+SQLite...;Arquitetura+em+Camadas...;Regras+de+Negócio...;Injeção+de+Dependência..." />
</p>

---

## 🚀 Sobre o projeto

O **Gerenciador de Usuários CLI** é um sistema CRUD desenvolvido em Python para gerenciamento de pessoas através de uma interface de linha de comando.

A aplicação permite **cadastrar, listar, buscar, atualizar e excluir** registros armazenados em um banco de dados SQLite, utilizando SQL para as operações de persistência.

O projeto foi estruturado utilizando **arquitetura em camadas**, separando responsabilidades entre interface, domínio, regras de negócio e acesso a dados.

Durante o desenvolvimento, foram aplicados conceitos de **Programação Orientada a Objetos, separação de responsabilidades, injeção de dependência, validação de dados, normalização e exceções personalizadas**.

Trata-se de um projeto **100% autoral**, desenvolvido com o objetivo de aprofundar conhecimentos em Python, bancos de dados relacionais, SQL, arquitetura de software e boas práticas de desenvolvimento.

---

## 🖥️ Tecnologias utilizadas

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,sqlite" />
</p>

* **Python**
* **SQLite**
* **SQL**
* **Git/GitHub**

---

## 🎯 Funcionalidades

* 👤 Cadastro de novas pessoas
* 📋 Listagem de pessoas cadastradas
* 🔍 Busca de pessoa por ID
* ✏️ Atualização de cadastro
* 🗑️ Exclusão de cadastro
* 💾 Persistência de dados em SQLite
* 🗄️ Criação automática da tabela
* 🔐 Consultas SQL parametrizadas
* ✅ Validação de dados
* ✨ Normalização de nomes
* ⚠️ Exceções personalizadas
* 🔄 Tratamento de erros de banco de dados
* 🧩 Arquitetura em camadas
* 💉 Injeção de dependência

---

## 🏗️ Arquitetura

A aplicação utiliza uma arquitetura em camadas para separar responsabilidades:

```text
Interface
    ↓
Main
    ↓
Service
    ↓
DAO
    ↓
SQLite
```

### 📂 Camadas

**`interface/`**
Responsável pela interação com o usuário, entrada de dados, menus e apresentação das informações.

**`domain/`**
Contém as entidades do domínio utilizadas pela aplicação, como `Pessoa`.

**`services/`**
Responsável pelas regras de negócio, validações, normalização e orquestração das operações.

**`database/`**
Responsável pela persistência dos dados e comunicação direta com o SQLite através do DAO.

**`exceptions/`**
Centraliza as exceções específicas da aplicação, permitindo que diferentes tipos de erro sejam tratados adequadamente.

**`main.py`**
Coordena o fluxo da aplicação e conecta as diferentes camadas.

---

## 🧠 Conceitos aplicados

* Programação Orientada a Objetos (POO)
* Entidades e modelagem de domínio
* CRUD
* Persistência de dados
* SQL e banco de dados relacional
* Data Access Object (DAO)
* Service Layer
* Arquitetura em camadas
* Separação de responsabilidades
* Injeção de dependência
* Regras de negócio
* Validação e normalização de dados
* Exceções personalizadas
* Encapsulamento de detalhes de infraestrutura
* Consultas parametrizadas
* Gerenciamento de recursos com `with`

---

## 📚 Aprendizados

Durante o desenvolvimento, o projeto foi evoluindo de uma aplicação simples para uma estrutura mais próxima de aplicações profissionais.

Entre os principais aprendizados estão:

* Separar regras de negócio do código de interface.
* Evitar que a aplicação dependa diretamente da tecnologia de banco utilizada.
* Utilizar entidades para representar conceitos do domínio.
* Centralizar o acesso aos dados através do DAO.
* Utilizar injeção de dependência para reduzir acoplamento.
* Criar exceções específicas para diferentes situações de erro.
* Diferenciar ausência de dados, falha operacional e exceções.
* Validar e normalizar dados antes da persistência.
* Organizar o código visando manutenção, legibilidade e evolução.

---

## 🌐 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/LucasBenfatti14/users-manager
```

### 2. Acesse a pasta

```bash
cd users-manager
```

### 3. Execute a aplicação

```bash
python main.py
```

O banco SQLite e a tabela necessária são preparados automaticamente durante a inicialização da aplicação.

---

## 🚧 Próximos passos

* 🧪 Implementar testes automatizados
* 📝 Adicionar logging da aplicação
* 🔄 Implementar Repository Pattern
* 🔐 Aprimorar regras de negócio e validações
* 🌐 Criar uma API REST utilizando FastAPI
* 📦 Melhorar configuração e gerenciamento do projeto

---

## 👨‍💻 Autor

<p align="center">
  Lucas Benfatti <br>
  📍 Santos - SP
</p>

---

<p align="center">
  🚀 Projeto em constante evolução
</p>
