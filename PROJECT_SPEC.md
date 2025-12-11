# Production-Ready System Architecture: Realtime AI Customer Support

## 📋 Project Overview

A secure, scalable, high-availability AI-powered customer support system combining Retrieval-Augmented Generation (RAG), real-time product data, and conversational intelligence.

---

## 🏗️ Production-Grade System Architecture

```mermaid
graph TD
    subgraph Frontend
        A1[Web App (React/TS)]
        A2[Socket.io Client]
    end

    subgraph API Layer
        B1[Web/API Gateway (Nginx)]
        B2[FastAPI (Uvicorn)]
    end

    subgraph Services
        C1[RAG Orchestrator]
        C2[LLM Service (OpenAI, GPT-4/4o)]
        C3[Retrieval Service (Qdrant/Semantic Search)]
        C4[Rerank Service (Cohere)]
        C5[Intent Classification Service (HuggingFace)]
        C6[Session State (Redis)]
        C7[Product Data API/Adapter]
    end

    subgraph Data Layer
        D1[PostgreSQL (User, Ticket, Audit)]
        D2[Qdrant (Vector DB)]
        D3[Object Storage (S3/MinIO)]
        D4[Redis Cache]
    end

    subgraph Monitoring & Ops
        E1[Sentry (APM + Error Tracking)]
        E2[Prometheus/Grafana (Metrics)]
        E3[Logging (Structured)]
        E4[CI/CD (GitHub Actions)]
    end

    A1 -->|HTTPS/WebSocket| B1 --> B2
    A2 -->|WebSocket| B2

    B2 -->|REST/WebSocket| C1
    C1 -->|Async| C2 & C3 & C5

    C3 -->|Query| D2
    C2 -->|API| [OpenAI Cloud]
    C3 -->|Rerank| C4
    C1 -->|State| C6
    C1 -->|Product/Order| C7
    C7 -->|Product Info| D1
    C1 -->|Storage| D3
    C1 -->|Cache| D4

    B2 -->|Logs| E3
    C1 -->|Metrics| E2
    B2 -->|Errors| E1

    E4-.->|Deploy| B2 & C1 & C3 & D1 & D2

```

**Key Features:**
- API Gateway handles routing, security, throttling.
- FastAPI enables async REST and real-time WebSocket endpoints.
- Modular microservices for LLM, retrieval, ranking, and intent detection.
- Fully containerized and deployable on Kubernetes, Docker Compose, or managed cloud platforms.
- Extensive observability and secure API key management.

---

## 📦 Production Folder Structure

```
realtime-ai-support/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI app entry
│   │   ├── config.py               # Env & secret config
│   │   ├── dependencies.py         # Dependency wire-up
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── chat.py             # Chat REST endpoints
│   │   │   ├── websocket.py        # Real-time endpoints
│   │   │   └── admin.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── rag_orchestrator.py # Pipeline entrypoint
│   │   │   ├── preprocess.py       # Query cleaning/expansion
│   │   │   ├── intent.py           # Intent classifier
│   │   │   ├── retriever.py        # Hybrid retriever (FAQ/Product)
│   │   │   ├── rerank.py           # Cohere reranker
│   │   │   ├── context_opt.py      # Token budgeting/attribution
│   │   │   └── llm.py              # Call to OpenAI/GPT
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   ├── postgres.py         # SQLAlchemy ORM models
│   │   │   └── migrations/
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── ticket.py
│   │   │   └── conversation.py
│   │   ├── vector_store/
│   │   │   ├── __init__.py
│   │   │   └── qdrant.py           # Vector DB operations
│   │   ├── cache/
│   │   │   ├── __init__.py
│   │   │   └── redis_cache.py      # Query/result caching
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── logging.py
│   │   │   ├── monitoring.py
│   │   │   └── compression.py
│   │   └── settings/
│   │       └── secrets.py          # API keys (never in Git!)
│   ├── tests/
│   │   ├── test_chat.py
│   │   ├── test_rag.py
│   │   └── test_intent.py
│   ├── data/
│   │   ├── faqs/
│   │   ├── products/
│   │   └── scripts/
│   │       └── ingest_docs.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── pyproject.toml
│   └── .env.example
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatWidget.tsx
│   │   │   ├── MessageList.tsx
│   │   │   ├── InputBox.tsx
│   │   │   └── TypingIndicator.tsx
│   │   ├── hooks/
│   │   │   ├── useChat.ts
│   │   │   └── useWebSocket.ts
│   │   ├── services/
│   │   │   └── api.ts
│   │   ├── types/
│   │   │   └── index.ts
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── tailwind.config.js
├── infrastructure/
│   ├── docker-compose.yaml
│   ├── k8s/
│   │   └── deployment.yaml
│   ├── prometheus.yml
│   ├── grafana/
│   │   └── dashboards/
│   ├── nginx/
│   │   └── nginx.conf
│   └── scripts/
│       └── register_services.sh
├── scripts/
│   ├── setup.sh
│   ├── seed_data.py
│   └── benchmark.py
├── docs/
│   ├── API.md
│   ├── DEPLOYMENT.md
│   └── ARCHITECTURE.md
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── deploy.yml
├── README.md
└── .gitignore
```

### 🗝️ Structural Notes

- **Backend** is modular, with clear separation of concerns per microservice-like layers (api, services, data/models, vector store, caching, utils, settings).
- **Frontend** (React + TypeScript) is designed for scalability, with dedicated folders for components, hooks, services, and type definitions.
- **Infrastructure** contains Docker, Kubernetes, Nginx, and observability config for easy CI/CD and cloud-native deployment.
- **All secrets (API keys etc) must reside in settings/secrets.py or environment variables; never checked into source control.**

---

## 🔒 Security & Compliance

- API keys and credentials loaded only from environment/configs outside source.
- All inter-service communication secured via HTTPS/mTLS in production.
- Rate-limiting, request validation, session/CSRF protections at API Gateway.
- All user PII, logs, and data in compliance with GDPR/CCPA via encrypted storage.

---

## 🚦 Observability

- **Sentry** for end-to-end error and performance monitoring.
- **Prometheus/Grafana** to record API, retrieval, and LLM/adapter service metrics.
- **Structured logging** for audit trails and incident traceability.

---

## 🔄 Production Workflow

1. **User interacts with React widget** → API Gateway → Web/API server (FastAPI).
2. **Request is routed to RAG Orchestrator**, which:
    - Cleans/preprocesses query, classifies intent.
    - Executes parallel retrieval (FAQ/product), applies Cohere re-ranking.
    - Tokenizes, budgets, and attributes sources for LLM prompt context.
    - Calls LLM API (OpenAI) and streams/caches response.
3. **All data & context is monitored, logged, and optionally cached** for performance.
4. **Response delivered back to frontend with source attributions and confidence indicators.**

---

## 📂 Example Environment Variables

```bash
# .env.example
OPENAI_API_KEY=sk-xxxx
COHERE_API_KEY=xxxx
QDRANT_URL=http://qdrant:6333
QDRANT_API_KEY=xxxx
REDIS_URL=redis://redis:6379
POSTGRES_URL=postgresql://user:password@postgres:5432/supportdb

RAG_MAX_CONTEXT_TOKENS=3000
RAG_TOP_K=5
RAG_RERANK_TOP_N=5
RAG_CACHE_TTL=300

EMBEDDING_MODEL=all-MiniLM-L6-v2
LLM_MODEL=gpt-4
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=500
SENTRY_DSN=xxxx
```

---

## ✅ Ready for Production

- All folders, configs, and patterns align to containerized production best practices.
- Subsystems are decoupled, tested, and observable.
- Ready for CI/CD automation and cloud scaling.

For implementation details, see `/docs/ARCHITECTURE.md` and `/backend/app/services/*`.

