from fake_repository import FakeRepository
from services import PessoaService
from api.main import app
from api.dependencies import get_service
from fastapi.testclient import TestClient

def get_fake_service() -> PessoaService:
    fake_repository = FakeRepository()
    return PessoaService(fake_repository)

client = TestClient(app)

def test_api_cadastra_pessoa_valida() -> None:
    app.dependency_overrides[get_service] = get_fake_service
    response = client.post(
        "/pessoas",
        json={
            "nome": "Lucas Benfatti",
            "idade": 18
        }
    )
    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["nome"] == "Lucas Benfatti"
    assert response.json()["idade"] == 18

def test_api_cadastra_pessoa_com_idade_invalida() -> None:
    app.dependency_overrides[get_service] = get_fake_service
    response = client.post(
        "/pessoas",
        json={
            "nome": "Lucas Benfatti",
            "idade": 180
        }
    )
    assert response.status_code == 422

def test_api_cadastra_pessoa_com_nome_duplicado() -> None:
    fake_repository = FakeRepository()
    def get_fake_service() -> PessoaService:
        return PessoaService(fake_repository)
    app.dependency_overrides[get_service] = get_fake_service
    response_1 = client.post(
        "/pessoas",
        json={
            "nome": "Lucas Benfatti",
            "idade": 30
        }
    )
    response_2 = client.post(
        "/pessoas",
        json={
            "nome": "Lucas Benfatti",
            "idade": 18
        }
    )
    assert response_1.status_code == 201
    assert response_2.status_code == 409
