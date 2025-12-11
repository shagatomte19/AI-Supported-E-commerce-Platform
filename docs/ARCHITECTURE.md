# Architecture

- React frontend with websocket client.
- Nginx gateway routing REST/WebSocket to FastAPI.
- FastAPI hosts chat REST and WS endpoints.
- RAG orchestrator calls preprocess, intent classifier, retriever, reranker, context optimizer, and LLM.
- Data layer: Postgres (users/tickets/conversations), Qdrant (vectors), Redis (cache/session), S3/MinIO (object storage placeholder).
- Observability: Sentry, Prometheus/Grafana, structured logs.

