# teste_meu_amor 💖

API simples feita com **FastAPI** que expõe dois endpoints:

| Método | Rota      | Descrição                                                        |
| ------ | --------- | ---------------------------------------------------------------- |
| `GET`  | `/health` | Health check — confirma que o serviço está no ar.                |
| `POST` | `/amor`   | Recebe um nome (string) e devolve uma frase amorosa personalizada.|

## Requisitos

- Python 3.14+
- `venv` (já vem com o Python)

## Como rodar

### 1. Criar e ativar o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Subir o servidor

```bash
uvicorn app.main:app --reload
```

A API fica disponível em `http://127.0.0.1:8000`.
Documentação interativa (Swagger): `http://127.0.0.1:8000/docs`.

## Exemplos de uso

**Health check**

```bash
curl http://127.0.0.1:8000/health
# {"status":"ok","service":"teste_meu_amor","version":"0.1.0"}
```

**Frase amorosa**

```bash
curl -X POST http://127.0.0.1:8000/amor \
  -H "Content-Type: application/json" \
  -d '{"nome": "Maria"}'
# {"nome":"Maria","frase":"Maria, você é a razão do meu sorriso mais sincero. 💖"}
```

## Testes

```bash
pip install -r requirements-dev.txt
pytest -v
```

## Estrutura do projeto

```
.
├── app/
│   ├── __init__.py
│   └── main.py          # Aplicação FastAPI e endpoints
├── tests/
│   ├── __init__.py
│   └── test_main.py     # Testes dos endpoints
├── requirements.txt     # Dependências de produção
├── requirements-dev.txt # Dependências de desenvolvimento/teste
├── .gitignore
└── README.md
```
