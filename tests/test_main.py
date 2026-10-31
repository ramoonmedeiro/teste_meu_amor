"""Testes básicos dos endpoints da API."""

from fastapi.testclient import TestClient

from app.main import FRASES_AMOROSAS, app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["service"] == "teste_meu_amor"


def test_amor_retorna_frase_com_nome() -> None:
    response = client.post("/amor", json={"nome": "Maria"})
    assert response.status_code == 200
    body = response.json()
    assert body["nome"] == "Maria"
    assert "Maria" in body["frase"]


def test_amor_nome_vazio_e_rejeitado() -> None:
    response = client.post("/amor", json={"nome": ""})
    assert response.status_code == 422
