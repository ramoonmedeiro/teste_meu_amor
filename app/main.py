"""Aplicação FastAPI do projeto teste_meu_amor.

Expõe dois endpoints:
    - GET  /health  -> health check
    - POST /amor    -> recebe um nome e devolve uma frase amorosa
"""

from __future__ import annotations

import random

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="teste_meu_amor",
    description="API simples com health check e mensagens amorosas.",
    version="0.1.0",
)

# Frases amorosas. O placeholder {nome} é substituído pelo nome recebido.
FRASES_AMOROSAS: list[str] = [
    "{nome}, você é a razão do meu sorriso mais sincero. 💖",
    "Se eu pudesse, {nome}, eu te daria todas as estrelas do céu. ✨",
    "{nome}, meu coração bate mais forte só de pensar em você. 💓",
    "Com você, {nome}, até os dias cinzas ganham cor. 🌈",
    "{nome}, você é o meu lugar favorito no mundo. 🏡",
    "Amar você, {nome}, é a minha melhor decisão todos os dias. 💘",
    "{nome}, você é poesia que o meu coração insiste em recitar. 📖",
    "Se o amor tem um nome, {nome}, com certeza é o seu. 🌹",
]


class NomeRequest(BaseModel):
    """Corpo da requisição do endpoint /amor."""

    nome: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Nome da pessoa que receberá a mensagem amorosa.",
        examples=["Maria"],
    )


class FraseResponse(BaseModel):
    """Resposta do endpoint /amor."""

    nome: str = Field(..., description="Nome recebido na requisição.")
    frase: str = Field(..., description="Frase amorosa gerada.")


class HealthResponse(BaseModel):
    """Resposta do endpoint /health."""

    status: str = Field(..., description="Status da aplicação.")
    service: str = Field(..., description="Nome do serviço.")
    version: str = Field(..., description="Versão da aplicação.")


@app.get("/health", response_model=HealthResponse, tags=["health"])
def health() -> HealthResponse:
    """Health check: confirma que a aplicação está no ar."""
    return HealthResponse(status="ok", service="teste_meu_amor", version=app.version)


@app.post("/amor", response_model=FraseResponse, tags=["amor"])
def amor(payload: NomeRequest) -> FraseResponse:
    """Recebe um nome e devolve uma frase amorosa personalizada."""
    nome = payload.nome.strip()
    frase = random.choice(FRASES_AMOROSAS).format(nome=nome)
    return FraseResponse(nome=nome, frase=frase)
