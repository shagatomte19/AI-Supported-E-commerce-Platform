# AI-Supported E-commerce Platform

Production-ready scaffold for a realtime AI customer support system with RAG, realtime product data, and observability hooks.

## Structure
- `backend/`: FastAPI app, RAG services, data layer, cache/vector adapters, tests.
- `frontend/`: React + TypeScript client (Vite) with chat widget and websocket hooks.
- `infrastructure/`: Docker/K8s manifests, reverse proxy, monitoring configs.
- `scripts/`: Setup, seeding, benchmarks.
- `docs/`: API, architecture, deployment guides.
- `.github/workflows/`: CI/CD pipelines.

## Quick Start
1) Create a `.env` using `backend/.env.example`.
2) Run `docker-compose` from `infrastructure/` (to be provided) or use local FastAPI/Vite dev servers.
3) Add API keys (OpenAI, Cohere, etc.) to environment variables only—never commit secrets.

## Next Steps
- Implement FastAPI endpoints in `backend/app/api/`.
- Fill service logic under `backend/app/services/`.
- Wire Redis/Qdrant/Postgres credentials in config.
- Build frontend chat components and websocket client.

