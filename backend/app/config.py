from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    cohere_api_key: str = Field(..., env="COHERE_API_KEY")
    qdrant_url: str = Field("http://qdrant:6333", env="QDRANT_URL")
    qdrant_api_key: str = Field("", env="QDRANT_API_KEY")
    redis_url: str = Field("redis://redis:6379", env="REDIS_URL")
    postgres_url: str = Field("postgresql://user:password@postgres:5432/supportdb", env="POSTGRES_URL")

    rag_max_context_tokens: int = Field(3000, env="RAG_MAX_CONTEXT_TOKENS")
    rag_top_k: int = Field(5, env="RAG_TOP_K")
    rag_rerank_top_n: int = Field(5, env="RAG_RERANK_TOP_N")
    rag_cache_ttl: int = Field(300, env="RAG_CACHE_TTL")

    embedding_model: str = Field("all-MiniLM-L6-v2", env="EMBEDDING_MODEL")
    llm_model: str = Field("gpt-4", env="LLM_MODEL")
    llm_temperature: float = Field(0.7, env="LLM_TEMPERATURE")
    llm_max_tokens: int = Field(500, env="LLM_MAX_TOKENS")

    sentry_dsn: str = Field("", env="SENTRY_DSN")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

