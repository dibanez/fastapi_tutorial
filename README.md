# 🚀 FastAPI Tutorial con PostgreSQL, JWT, Docker y Render

Este es un ejemplo completo de cómo crear una API REST con [FastAPI](https://fastapi.tiangolo.com/), usar PostgreSQL, autenticación JWT, y desplegar en Render.com.

---

## 🧱 Estructura del Proyecto

```
fastapi_tutorial/
├── app/
│   ├── api/
│   ├── models/
│   ├── schemas/
│   ├── utils/
│   ├── main.py
│   ├── config.py
│   └── db.py
├── tests/
├── .env.dev
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🧪 Tecnologías utilizadas

- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker + Docker Compose
- Pydantic (v2)
- JWT (`python-jose`)
- `passlib` (hashing de contraseñas)
- pytest

---

## ▶️ Cómo ejecutar en local

### 1. Clonar el repositorio

```bash
git clone https://github.com/dibanez/fastapi_tutorial.git
cd fastapi_tutorial
```

### 2. Crear archivo `.env.dev`

```env
PROJECT_NAME=FastAPI with PostgreSQL
API_VERSION=v1
DATABASE_URL=postgresql://postgres:postgres@db:5433/fastapi_db
```

### 3. Levantar servicios

```bash
docker-compose up --build
```

Visita [http://localhost:8001/docs](http://localhost:8001/docs) para ver la documentación interactiva.

---

## 👤 Autenticación con JWT

### Registro de usuario

```bash
curl -X POST http://localhost:8001/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "password": "secret123"}'
```

### Login y obtención del token

```bash
curl -X POST http://localhost:8001/auth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=alice&password=secret123"
```

Respuesta esperada:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

---

## 🛡 Rutas protegidas

### Crear un item

```bash
curl -X POST http://localhost:8001/items/ \
  -H "Authorization: Bearer TU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{"name": "Laptop", "price": 1299.99, "in_stock": true}'
```

### Listar items

```bash
curl -X GET http://localhost:8001/items/ \
  -H "Authorization: Bearer TU_TOKEN_AQUI"
```

---

## 🗃 Base de datos PostgreSQL

- Usuario: `postgres`
- Contraseña: `postgres`
- Base de datos: `fastapi_db`
- Servicio en Docker: `db`

---

## 🧪 Tests

```bash
docker exec -it fastapi_app pytest
```

---

## 🌐 Despliegue en Render

Render no admite `docker-compose`, pero puedes:

1. Subir tu repo a GitHub
2. Crear un servicio web en Render:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `uvicorn app.main:app --host 0.0.0.0 --port 10000`
   - Añade tus variables de entorno (como `DATABASE_URL`)
3. Crear un servicio de PostgreSQL y conectar tu backend

---

## 📄 Licencia

MIT License.