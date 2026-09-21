<h1 align="center">📋 Gerenciador de Usuários</h1>

<p align="center">
  💻 CRUD em Python para gerenciamento de pessoas<br>
  🌐 API REST com FastAPI e interface CLI<br>
  🗄️ PostgreSQL com arquitetura em camadas
</p>

---

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?color=00FF00&size=22&center=true&vCenter=true&width=800&lines=CRUD+em+Python...;API+REST+com+FastAPI...;PostgreSQL...;Arquitetura+em+Camadas...;Regras+de+Negócio...;DTOs+com+Pydantic...;Testes+automatizados...;Tratamento+de+Exceções" />
</p>

---

## 🚀 Sobre o projeto

O **Users Manager** é uma aplicação CRUD desenvolvida em Python para gerenciamento de pessoas.

O projeto evoluiu de uma aplicação **CLI** para uma **API REST com FastAPI**, mantendo o domínio e as regras de negócio independentes das interfaces de acesso.

A aplicação foi estruturada com separação de responsabilidades entre domínio, serviços, repositórios, persistência, interfaces e testes.

Principais recursos:

* Cadastro, consulta, atualização e exclusão de pessoas;
* Atualização completa e parcial;
* Validação e normalização de dados;
* Regras de negócio centralizadas;
* Persistência em PostgreSQL;
* Implementação alternativa para SQLite;
* Tratamento de exceções personalizadas;
* Injeção de dependências;
* DTOs com Pydantic;
* Documentação automática com OpenAPI/Swagger;
* Testes automatizados para domínio, serviços e API.

O projeto tem como objetivo consolidar conhecimentos em **Python, desenvolvimento backend, APIs REST, bancos de dados, testes automatizados e arquitetura de software**.

---

## 🛠️ Tecnologias

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,postgres,sqlite,git,github,pytest" />
</p>

* **Python**
* **FastAPI**
* **Pydantic**
* **PostgreSQL**
* **SQLite**
* **Psycopg**
* **Uvicorn**
* **python-dotenv**
* **Pytest**
* **Git / GitHub**

---

## 🎯 Funcionalidades

### 👤 Pessoas

| Método   | Endpoint        | Descrição                         |
| -------- | --------------- | --------------------------------- |
| `GET`    | `/pessoas`      | Lista todas as pessoas            |
| `GET`    | `/pessoas/{id}` | Busca uma pessoa por ID           |
| `POST`   | `/pessoas`      | Cadastra uma pessoa               |
| `PUT`    | `/pessoas/{id}` | Atualiza completamente uma pessoa |
| `PATCH`  | `/pessoas/{id}` | Atualiza parcialmente uma pessoa  |
| `DELETE` | `/pessoas/{id}` | Remove uma pessoa                 |

A API utiliza códigos HTTP adequados para representar o resultado das operações:

| Código | Descrição                                      |
| ------ | ---------------------------------------------- |
| `200`  | Operação realizada com sucesso                 |
| `201`  | Pessoa cadastrada com sucesso                  |
| `204`  | Pessoa excluída com sucesso                   |
| `404`  | Pessoa não encontrada                          |
| `409`  | Conflito de regra de negócio                  |
| `422`  | Dados inválidos ou erro de domínio            |
| `500`  | Erro interno ou falha de infraestrutura       |

---

## 🏗️ Arquitetura

O projeto utiliza uma **arquitetura em camadas**, separando domínio, regras de negócio, persistência e interfaces.

```text
                    ┌──────────────────┐
                    │    CLI / HTTP    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  API / FastAPI   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  PessoaService   │
                    │ Regras de negócio│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ PessoaRepository │
                    │    Abstração     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    PessoaDAO     │
                    │ PostgreSQL/SQLite│
                    └──────────────────┘

                    ┌──────────────────┐
                    │      Domain      │
                    │      Pessoa      │
                    └──────────────────┘
```

### 📂 Estrutura

* **`crud-cadastro/domain/`** — entidade `Pessoa`, validações, normalização e controle de estado;
* **`crud-cadastro/services/`** — regras e orquestração através do `PessoaService`;
* **`crud-cadastro/repositories/`** — abstração utilizada pela camada de negócio;
* **`crud-cadastro/database/postgres/`** — conexão, criação da tabela e DAO para PostgreSQL;
* **`crud-cadastro/database/sqlite/`** — implementação alternativa de persistência com SQLite;
* **`crud-cadastro/api/`** — rotas HTTP, DTOs, dependências e handlers;
* **`crud-cadastro/interface/`** — interface de linha de comando;
* **`crud-cadastro/exceptions/`** — exceções de domínio, negócio e infraestrutura;
* **`crud-cadastro/tests/`** — testes de domínio, serviços e API;
* **`crud-cadastro/main.py`** — ponto de entrada da aplicação CLI.

A aplicação utiliza **Dependency Injection** para fornecer o Repository ao Service, reduzindo o acoplamento entre negócio e infraestrutura.

---

## 📦 DTOs

A API utiliza modelos Pydantic separados da entidade de domínio:

```python
class PessoaCreate(BaseModel):
    nome: str
    idade: int

class PessoaPatch(BaseModel):
    nome: str | None = None
    idade: int | None = None

class PessoaResponse(BaseModel):
    id: int
    nome: str
    idade: int
```

* `PessoaCreate` — dados necessários para criação e atualização completa;
* `PessoaPatch` — dados opcionais para atualização parcial;
* `PessoaResponse` — estrutura retornada pela API.

Essa separação mantém o contrato HTTP desacoplado da implementação interna do domínio.

---

## 🧠 Domínio e regras de negócio

A entidade `Pessoa` controla seu próprio estado e realiza validações antes da persistência.

Entre as regras implementadas:

* Nome completo obrigatório;
* Primeiro nome com tamanho entre `3` e `32` caracteres;
* Sobrenomes com tamanho entre `2` e `50` caracteres;
* Validação de caracteres alfabéticos;
* Normalização do nome;
* Idade entre `0` e `130`;
* Prevenção de nomes duplicados;
* ID definido apenas uma vez;
* Atualizações parciais exigindo pelo menos um campo.

As regras de negócio permanecem independentes do FastAPI e da implementação do banco.

---

## ⚠️ Tratamento de exceções

A aplicação utiliza exceções personalizadas para separar diferentes tipos de falha.

```text
DominioError
RegraDeNegocioError
BancoDeDadosError
PessoaJaCadastradaError
NomeInvalidoError
NomeIncompletoError
NomeComCaracteresInvalidosError
IdadeInvalidaError
IdJaDefinidoError
NomeEIdadeNaoFornecidos
```

Na API, essas exceções são tratadas por handlers específicos e convertidas em respostas HTTP adequadas, sem expor detalhes internos da aplicação.

* Erros de domínio são convertidos em respostas `422`;
* Erros de regras de negócio são convertidos em respostas `409`;
* Erros de banco de dados são convertidos em respostas `500`.

---

## 🗄️ Persistência

A implementação utilizada atualmente pela **CLI e pela API** é baseada em **PostgreSQL**, utilizando **Psycopg**.

O projeto também mantém uma implementação equivalente para **SQLite**, permitindo utilizar diferentes estratégias de persistência através da abstração `PessoaRepository`.

As conexões utilizam **Context Managers** para centralizar:

* Abertura e fechamento da conexão;
* `commit`;
* `rollback`;
* Tratamento de erros de infraestrutura.

As consultas ao banco utilizam parâmetros, evitando a interpolação direta de valores nas queries.

As credenciais do PostgreSQL são configuradas através de variáveis de ambiente.

---

## 🔄 Fluxo da aplicação

O fluxo principal mantém as responsabilidades separadas:

```text
Cliente
   │
   ▼
FastAPI / CLI
   │
   ▼
PessoaService
   │
   ▼
PessoaRepository
   │
   ▼
PessoaDAO
   │
   ▼
PostgreSQL / SQLite
```

A camada de entrada não acessa diretamente o banco nem concentra regras de negócio.

---

## 🧩 Conceitos aplicados

**Python**

* Programação Orientada a Objetos;
* Encapsulamento;
* Properties;
* Type Hints;
* Exceções;
* Context Managers.

**Arquitetura**

* Layered Architecture;
* Service Layer;
* Repository Pattern;
* DAO;
* Dependency Injection;
* Separação de responsabilidades;
* Baixo acoplamento.

**Banco de dados**

* PostgreSQL;
* SQLite;
* SQL;
* CRUD;
* Queries parametrizadas;
* Transações.

**API**

* HTTP;
* REST;
* JSON;
* Status Codes;
* Pydantic;
* OpenAPI / Swagger;
* Exception Handlers.

**Testes**

* Pytest;
* Testes unitários;
* Testes de domínio;
* Testes de serviço;
* Testes de API;
* Fake Repository;
* Dependency Overrides.

---

## 🧪 Testes

O projeto possui testes automatizados utilizando **Pytest**.

Os testes estão organizados da seguinte forma:

* **`tests/test_pessoa_domain.py`** — validações, normalização de nomes e regras da entidade;
* **`tests/test_pessoa_service.py`** — regras de negócio, cadastro, busca, atualização e exclusão;
* **`tests/test_api.py`** — integração com os endpoints da API utilizando `TestClient`;
* **`tests/fake_repository.py`** — repositório em memória utilizado nos testes.

Para executar todos os testes:

```bash
pytest
```

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/LucasBenfatti14/users-manager.git
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
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o PostgreSQL

Crie um arquivo `.env` a partir do `.env.example`:

```env
POSTGRES_HOST=seu_host
POSTGRES_PORT=sua_porta
POSTGRES_DB=seu_banco
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
```

No Linux/macOS, você pode copiar o arquivo de exemplo utilizando:

```bash
cp .env.example .env
```

No Windows, copie manualmente o arquivo `.env.example`, renomeie-o para `.env` e preencha as credenciais do banco.

### 5. Acesse a aplicação

Entre na pasta principal do código:

```bash
cd crud-cadastro
```

### 6. Execute a CLI

```bash
python main.py
```

### 7. Execute a API

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

### 8. Execute os testes

Ainda dentro da pasta `crud-cadastro`, execute:

```bash
pytest
```

A tabela `pessoas` é criada automaticamente durante a inicialização da aplicação caso ainda não exista.

---

## 🚧 Próximos passos

* Logging e observabilidade;
* Configuração por ambiente;
* Autenticação e autorização;
* JWT e controle de acesso;
* Docker e Docker Compose;
* CI/CD com GitHub Actions;
* Paginação, filtros e ordenação;
* Padronização de respostas de erro;
* Expansão dos testes de integração com banco de dados;
* Evolução para Clean Architecture / Ports and Adapters.

---

## 👨‍💻 Autor

<p align="center">
  <strong>Lucas Benfatti</strong><br>
  📍 SP - Brasil
</p>

<p align="center">
  🚀 Projeto em constante evolução
</p>
