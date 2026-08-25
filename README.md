<h1 align="center">📋 Users Manager</h1>

<p align="center">
  💻 CRUD em Python para gerenciamento de pessoas<br>
  🌐 API REST com FastAPI e interface CLI<br>
  🗄️ SQLite com arquitetura em camadas
</p>

---

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?color=00FF00&size=22&center=true&vCenter=true&width=800&lines=CRUD+em+Python...;API+REST+com+FastAPI...;SQLite...;Arquitetura+em+Camadas...;Regras+de+Negócio...;DTOs+com+Pydantic...;Tratamento+de+Exceções" />
</p>

---

## 🚀 Sobre o projeto

O **Users Manager** é uma aplicação CRUD desenvolvida em Python para gerenciamento de pessoas.

O projeto começou como uma aplicação **CLI** e evoluiu para uma **API REST com FastAPI**, mantendo a mesma camada de domínio e regras de negócio.

A aplicação possui:

* Cadastro, consulta, atualização e exclusão de pessoas;
* Atualização completa e parcial;
* Validação e normalização de dados;
* Regras de negócio centralizadas;
* Persistência em SQLite;
* Tratamento de exceções;
* API REST com documentação OpenAPI.

O principal objetivo é aplicar conceitos de **desenvolvimento backend, Programação Orientada a Objetos e arquitetura de software** em um projeto evolutivo e prático.

---

## 🛠️ Tecnologias

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,sqlite,git,github" />
</p>

* **Python**
* **FastAPI**
* **Pydantic**
* **SQLite / SQL**
* **Uvicorn**
* **Git / GitHub**

---

## 🎯 Funcionalidades

### 👤 Pessoas

| Método   | Endpoint        | Descrição              |
| -------- | --------------- | ---------------------- |
| `GET`    | `/pessoas`      | Lista pessoas          |
| `GET`    | `/pessoas/{id}` | Busca por ID           |
| `POST`   | `/pessoas`      | Cadastra uma pessoa    |
| `PUT`    | `/pessoas/{id}` | Atualiza completamente |
| `PATCH`  | `/pessoas/{id}` | Atualiza parcialmente  |
| `DELETE` | `/pessoas/{id}` | Remove uma pessoa      |

A API utiliza códigos HTTP apropriados, incluindo `200`, `201`, `204`, `404`, `409`, `422` e `500`.

---

## 🏗️ Arquitetura

O projeto utiliza uma arquitetura em camadas para separar responsabilidades e reduzir o acoplamento.

```text
                ┌──────────────────┐
                │   CLI / HTTP     │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │  API / FastAPI   │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │   PessoaService  │
                │ Regras de negócio│
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │    Repository    │
                │   Persistência   │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │      SQLite      │
                └──────────────────┘

                ┌──────────────────┐
                │      Domain      │
                │     Pessoa       │
                └──────────────────┘
```

### `domain/`

Contém as entidades e comportamentos do domínio, incluindo validação, normalização e controle do estado de `Pessoa`.

### `services/`

Responsável pela orquestração das regras de negócio através do `PessoaService`.

### `repositories/`

Define a abstração de persistência, mantendo a camada de negócio independente da implementação do banco.

### `database/`

Contém a implementação de persistência utilizando SQLite, SQL e gerenciamento de conexões.

### `api/`

Responsável pela interface HTTP, validação dos dados, rotas, respostas e tradução de exceções para HTTP.

### `exceptions/`

Centraliza as exceções de domínio, negócio e infraestrutura.

---

## 📦 DTOs

Os DTOs representam os dados transportados pela API sem expor diretamente as entidades do domínio.

```python
class PessoaCreate(BaseModel):
    nome: str
    idade: int
```

```python
class PessoaResponse(BaseModel):
    id: int
    nome: str
    idade: int
```

Também existe o `PessoaPatch`, utilizado em atualizações parciais.

A separação entre **DTO** e **Domain Entity** permite manter a API desacoplada da implementação interna.

---

## 🧠 Regras de negócio

As regras são mantidas fora da camada HTTP.

Entre elas:

* Validação e normalização do nome;
* Validação da idade;
* Verificação de duplicidade;
* Controle do ID;
* Validação de atualizações parciais.

Dessa forma:

```text
DTO
 ↓
Domain
 ↓
Service
 ↓
Repository
 ↓
Database
```

Cada camada possui uma responsabilidade específica.

---

## ⚠️ Tratamento de exceções

A aplicação utiliza exceções personalizadas e handlers globais.

Exemplos:

```text
DominioError
RegraDeNegocioError
BancoDeDadosError
PessoaJaCadastradaError
NomeInvalidoError
IdadeInvalidaError
```

Essas exceções são convertidas pela API em respostas HTTP adequadas, evitando expor detalhes internos da aplicação ou do banco.

---

## 🧩 Conceitos aplicados

O projeto consolida conhecimentos em:

**Python**

* POO
* Encapsulamento
* Properties
* Type Hints
* Exceções
* Context Managers

**Arquitetura**

* Layered Architecture
* Service Layer
* Repository Pattern
* DAO
* Dependency Injection
* Separação de responsabilidades

**Banco de dados**

* SQLite
* SQL
* CRUD
* Queries parametrizadas
* Transações

**API**

* HTTP
* REST
* JSON
* Status Codes
* Pydantic
* OpenAPI
* Exception Handlers

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/LucasBenfatti14/users-manager
cd users-manager
```

### 2. Crie e ative o ambiente virtual

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a CLI

```bash
python main.py
```

### 5. Execute a API

```bash
uvicorn api.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

OpenAPI:

```text
http://127.0.0.1:8000/openapi.json
```

---

## 🚧 Próximos passos

* Testes unitários e de integração com **Pytest**;
* PostgreSQL e migrações;
* Logging e configuração por ambiente;
* Autenticação e autorização com JWT;
* Docker e Docker Compose;
* CI/CD com GitHub Actions;
* Paginação, filtros e ordenação;
* Evolução para Clean Architecture / Ports and Adapters.

---

## 👨‍💻 Autor

<p align="center">
  <strong>Lucas Benfatti</strong><br>
  📍 Santos - SP, Brasil
</p>

<p align="center">
  🚀 Projeto em constante evolução
</p>
