 # Realtime AI Customer Support System -
Complete Project Guide
## 📋 Project Overview

## 🛠️ Technology Stack
### Backend & APIs
- FastAPI (Python 3.11+) - Async web framework
- Uvicorn - ASGI server
- Pydantic - Data validation
- Python-multipart - File upload handling
### LLM & AI Components
- OpenAI API (GPT-4/GPT-4o) - Conversational AI
- Langchain/LangGraph - LLM orchestration & agent workflows
- Qdrant - Vector database for RAG
- Sentence-Transformers - Embedding generation
- Cohere Rerank API - Result re-ranking
- Transformers (HuggingFace) - Intent classification
### Databases & Caching
- Redis - Session/conversation state management
- PostgreSQL - Persistent data storage
- S3/MinIO - Object storage for documents
### Frontend
- React 18 + TypeScript
- Tailwind CSS - Styling
- Socket.io-client - Realtime communication
- React Query - Data fetching
### DevOps & Monitoring
- Docker + Docker Compose - Containerization
- Railway/Render - Backend deployment
- Vercel - Frontend deployment
- Sentry - Error tracking
- Prometheus + Grafana - Metrics monitoring
- Nginx - Reverse proxy (optional)

## 📦 Project Structure
realtime-ai-support/
├── backend/
│ ├── app/
│ │ ├── __init__.py
│ │ ├── main.py # FastAPI app entry
│ │ ├── config.py # Environment configs
│ │ ├── dependencies.py # Dependency injection
│ │ │
│ │ ├── api/
│ │ │ ├── __init__.py
│ │ │ ├── chat.py # Chat endpoints
│ │ │ ├── admin.py # Admin dashboard
│ │ │ └── websocket.py # WebSocket handlers
│ │ │
│ │ ├── models/
│ │ │ ├── __init__.py
│ │ │ ├── conversation.py # Pydantic models
│ │ │ ├── user.py
│ │ │ └── ticket.py
│ │ │
│ │ ├── services/
│ │ │ ├── __init__.py
│ │ │ ├── llm_service.py # OpenAI integration
│ │ │ ├── rag_service.py # RAG pipeline
│ │ │ ├── intent_classifier.py
│ │ │ ├── routing_service.py # Human handoff logic
│ │ │ └── redis_service.py # Session management
│ │ │
│ │ ├── core/
│ │ │ ├── __init__.py
│ │ │ ├── embeddings.py # Vector embeddings
│ │ │ ├── vector_store.py # Qdrant operations
│ │ │ ├── cache.py # Query deduplication
│ │ │ └── memory.py # Conversation memory
│ │ │
│ │ ├── db/
│ │ │ ├── __init__.py
│ │ │ ├── postgres.py # SQLAlchemy models
│ │ │ └── migrations/ # Alembic migrations
│ │ │
│ │ └── utils/
│ │ ├── __init__.py
│ │ ├── compression.py # Response compression
│ │ ├── logging.py # Structured logging
│ │ └── monitoring.py # Prometheus metrics
│ │
│ ├── tests/
│ │ ├── test_api.py
│ │ ├── test_rag.py
│ │ └── test_intent.py
│ │
│ ├── data/
│ │ ├── faqs/ # FAQ documents
│ │ ├── products/ # Product catalog
│ │ └── scripts/
│ │ └── ingest_docs.py # Data ingestion
│ │
│ ├── Dockerfile
│ ├── requirements.txt
│ ├── pyproject.toml
│ └── .env.example
│
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ │ ├── ChatWidget.tsx # Main chat interface
│ │ │ ├── MessageList.tsx
│ │ │ ├── InputBox.tsx
│ │ │ └── TypingIndicator.tsx
│ │ │
│ │ ├── hooks/
│ │ │ ├── useChat.ts # Chat logic
│ │ │ └── useWebSocket.ts
│ │ │
│ │ ├── services/
│ │ │ └── api.ts # API client
│ │ │
│ │ ├── types/
│ │ │ └── index.ts
│ │ │
│ │ ├── App.tsx
│ │ └── main.tsx
│ │
│ ├── package.json
│ ├── tsconfig.json
│ ├── vite.config.ts
│ └── tailwind.config.js
│
├── infrastructure/
│ ├── docker-compose.yml
│ ├── prometheus.yml
│ ├── grafana/
│ │ └── dashboards/
│ └── nginx/
│ └── nginx.conf
│
├── scripts/
│ ├── setup.sh
│ ├── seed_data.py
│ └── benchmark.py
│
├── docs/
│ ├── API.md
│ ├── DEPLOYMENT.md
│ └── ARCHITECTURE.md
│
├── .github/
│ └── workflows/
│ ├── ci.yml
│ └── deploy.yml
├── README.md
└── .gitignore

# 🔄 Hybrid RAG Pipeline Process Flow

Complete implementation guide for a hybrid RAG system handling both static FAQs and real-time product catalog data.

---

## 📊 Architecture Overview

```
User Query
    ↓
┌───────────────────────────────────────────┐
│  1. QUERY PREPROCESSING                   │
│  - Normalize & clean                      │
│  - Extract entities (product IDs, etc)    │
│  - Query expansion/rewriting              │
└───────────────────────────────────────────┘
    ↓
┌───────────────────────────────────────────┐
│  2. QUERY ROUTING (Intent Classification) │
│  - FAQ intent                             │
│  - Product search intent                  │
│  - Hybrid intent                          │
└───────────────────────────────────────────┘
    ↓
    ├─────────────────────┬──────────────────────┐
    ↓                     ↓                      ↓
┌─────────┐      ┌──────────────┐      ┌────────────┐
│FAQ Path │      │Product Path  │      │Hybrid Path │
│(Static) │      │(Real-time)   │      │(Combined)  │
└─────────┘      └──────────────┘      └────────────┘
    ↓                     ↓                      ↓
┌─────────────────────────────────────────────────┐
│  3. PARALLEL RETRIEVAL                          │
│  ┌──────────────┐    ┌──────────────────────┐  │
│  │ FAQ Retrieval│    │ Product Retrieval    │  │
│  │ - Semantic   │    │ - SQL/API queries    │  │
│  │ - Keyword    │    │ - Metadata filters   │  │
│  │ - Hybrid BM25│    │ - Real-time pricing  │  │
│  └──────────────┘    └──────────────────────┘  │
└─────────────────────────────────────────────────┘
    ↓
┌───────────────────────────────────────────┐
│  4. CONTEXT FUSION & RERANKING            │
│  - Merge results                          │
│  - Cohere rerank                          │
│  - Deduplicate                            │
│  - Score normalization                    │
└───────────────────────────────────────────┘
    ↓
┌───────────────────────────────────────────┐
│  5. CONTEXT OPTIMIZATION                  │
│  - Top-K selection (K=5-7)                │
│  - Token budget management                │
│  - Source attribution tagging             │
└───────────────────────────────────────────┘
    ↓
┌───────────────────────────────────────────┐
│  6. LLM GENERATION                        │
│  - Prompt construction                    │
│  - GPT-4 with context                     │
│  - Streaming response                     │
└───────────────────────────────────────────┘
    ↓
┌───────────────────────────────────────────┐
│  7. POST-PROCESSING                       │
│  - Citation injection                     │
│  - Confidence scoring                     │
│  - Fallback handling                      │
└───────────────────────────────────────────┘
    ↓
Response to User
```

---

## 🎯 Detailed Implementation

### **1. Query Preprocessing Module**

**File:** `services/query_processor.py`

```python
from typing import Dict, List, Tuple
import re
from langchain.text_splitter import RecursiveCharacterTextSplitter

class QueryPreprocessor:
    def __init__(self):
        self.entity_patterns = {
            'product_id': r'[A-Z]{2,3}-\d{4,6}',
            'price': r'\$\d+(?:\.\d{2})?',
            'order_id': r'ORD-\d{8}'
        }
    
    async def process(self, query: str) -> Dict:
        """Preprocess and enhance query"""
        return {
            'original': query,
            'normalized': self._normalize(query),
            'entities': self._extract_entities(query),
            'expanded': await self._expand_query(query),
            'keywords': self._extract_keywords(query)
        }
    
    def _normalize(self, query: str) -> str:
        """Clean and normalize query"""
        query = query.lower().strip()
        query = re.sub(r'\s+', ' ', query)
        return query
    
    def _extract_entities(self, query: str) -> Dict[str, List[str]]:
        """Extract structured entities"""
        entities = {}
        for entity_type, pattern in self.entity_patterns.items():
            matches = re.findall(pattern, query)
            if matches:
                entities[entity_type] = matches
        return entities
    
    async def _expand_query(self, query: str) -> List[str]:
        """Generate query variations"""
        expansions = [query]
        
        # Synonym expansion
        synonyms = {
            'buy': ['purchase', 'order', 'get'],
            'broken': ['defective', 'not working', 'damaged'],
            'return': ['refund', 'send back', 'exchange']
        }
        
        for word, syns in synonyms.items():
            if word in query.lower():
                for syn in syns:
                    expansions.append(query.lower().replace(word, syn))
        
        return expansions[:3]  # Limit expansions
    
    def _extract_keywords(self, query: str) -> List[str]:
        """Extract important keywords"""
        # Simple keyword extraction (can use KeyBERT for better results)
        stopwords = {'what', 'how', 'where', 'when', 'can', 'is', 'the', 'a', 'an'}
        words = query.lower().split()
        return [w for w in words if w not in stopwords and len(w) > 2]
```

**Key Features:**
- Entity extraction (product IDs, order numbers, prices)
- Query normalization and cleaning
- Synonym-based query expansion
- Keyword extraction for hybrid search

---

### **2. Intent-Based Routing**

**File:** `services/intent_router.py`

```python
from enum import Enum
from transformers import pipeline
import numpy as np

class IntentType(Enum):
    FAQ = "faq"
    PRODUCT_SEARCH = "product_search"
    PRODUCT_AVAILABILITY = "product_availability"
    PRICING = "pricing"
    HYBRID = "hybrid"

class IntentRouter:
    def __init__(self):
        self.classifier = pipeline(
            "text-classification",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
        
        self.intent_keywords = {
            IntentType.FAQ: ['how to', 'what is', 'help', 'guide', 'tutorial'],
            IntentType.PRODUCT_SEARCH: ['show', 'find', 'search', 'looking for'],
            IntentType.PRODUCT_AVAILABILITY: ['available', 'in stock', 'stock'],
            IntentType.PRICING: ['price', 'cost', 'how much', 'expensive']
        }
    
    async def route(self, processed_query: Dict) -> Dict:
        """Determine retrieval strategy"""
        query = processed_query['normalized']
        entities = processed_query['entities']
        
        # Rule-based routing
        intents = []
        scores = {}
        
        # Check for explicit product references
        if entities.get('product_id'):
            intents.append(IntentType.PRODUCT_SEARCH)
            scores[IntentType.PRODUCT_SEARCH] = 0.95
        
        # Keyword matching
        for intent_type, keywords in self.intent_keywords.items():
            score = sum(1 for kw in keywords if kw in query) / len(keywords)
            if score > 0:
                scores[intent_type] = score
        
        # Determine primary intent
        if not scores:
            intents.append(IntentType.HYBRID)
        elif len(scores) > 1:
            intents.append(IntentType.HYBRID)
        else:
            intents.append(max(scores, key=scores.get))
        
        return {
            'primary_intent': intents[0],
            'confidence_scores': scores,
            'retrieval_strategy': self._get_strategy(intents[0])
        }
    
    def _get_strategy(self, intent: IntentType) -> Dict:
        """Define retrieval parameters per intent"""
        strategies = {
            IntentType.FAQ: {
                'faq_weight': 0.8,
                'product_weight': 0.2,
                'use_semantic': True,
                'use_keyword': True,
                'top_k': 5
            },
            IntentType.PRODUCT_SEARCH: {
                'faq_weight': 0.2,
                'product_weight': 0.8,
                'use_realtime': True,
                'use_filters': True,
                'top_k': 8
            },
            IntentType.HYBRID: {
                'faq_weight': 0.5,
                'product_weight': 0.5,
                'use_semantic': True,
                'use_realtime': True,
                'top_k': 7
            }
        }
        return strategies.get(intent, strategies[IntentType.HYBRID])
```

**Routing Logic:**
- **FAQ Intent**: User asking "how-to" or general questions
- **Product Search**: User looking for specific products
- **Hybrid Intent**: Mixed queries requiring both FAQ and product data

---

### **3. Parallel Retrieval Engines**

**File:** `services/rag_service.py`

```python
import asyncio
from typing import List, Dict
from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
from sentence_transformers import SentenceTransformer
import cohere

class HybridRAGPipeline:
    def __init__(self):
        self.qdrant = QdrantClient(url="http://localhost:6333")
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.cohere = cohere.Client(api_key="your-key")
        
        # Collections
        self.faq_collection = "faq_knowledge"
        self.product_collection = "product_catalog"
    
    async def retrieve(
        self, 
        processed_query: Dict,
        routing_result: Dict
    ) -> List[Dict]:
        """Execute hybrid retrieval"""
        strategy = routing_result['retrieval_strategy']
        
        # Parallel retrieval tasks
        tasks = []
        
        # FAQ retrieval (if needed)
        if strategy['faq_weight'] > 0:
            tasks.append(
                self._retrieve_faq(
                    processed_query,
                    top_k=int(strategy['top_k'] * strategy['faq_weight'])
                )
            )
        
        # Product retrieval (if needed)
        if strategy['product_weight'] > 0:
            tasks.append(
                self._retrieve_products(
                    processed_query,
                    top_k=int(strategy['top_k'] * strategy['product_weight']),
                    use_realtime=strategy.get('use_realtime', False)
                )
            )
        
        # Execute in parallel
        results = await asyncio.gather(*tasks)
        
        # Flatten results
        all_chunks = []
        for result_set in results:
            all_chunks.extend(result_set)
        
        return all_chunks
    
    async def _retrieve_faq(self, query: Dict, top_k: int) -> List[Dict]:
        """Semantic + Keyword hybrid search for FAQs"""
        query_text = query['normalized']
        query_vector = self.embedder.encode(query_text).tolist()
        
        # Semantic search
        semantic_results = self.qdrant.search(
            collection_name=self.faq_collection,
            query_vector=query_vector,
            limit=top_k * 2,  # Over-retrieve for reranking
            score_threshold=0.5
        )
        
        # Keyword search (BM25-like via payload filtering)
        keyword_results = self.qdrant.search(
            collection_name=self.faq_collection,
            query_vector=query_vector,
            limit=top_k,
            query_filter=Filter(
                should=[
                    FieldCondition(
                        key="text",
                        match=MatchValue(value=kw)
                    ) for kw in query['keywords']
                ]
            )
        )
        
        # Combine and deduplicate
        combined = self._merge_results(semantic_results, keyword_results)
        
        return [
            {
                'content': hit.payload.get('text', ''),
                'metadata': hit.payload.get('metadata', {}),
                'score': hit.score,
                'source': 'faq',
                'id': hit.id
            }
            for hit in combined[:top_k]
        ]
    
    async def _retrieve_products(
        self, 
        query: Dict, 
        top_k: int,
        use_realtime: bool
    ) -> List[Dict]:
        """Product catalog retrieval with real-time data"""
        products = []
        
        # Check for specific product IDs
        if query['entities'].get('product_id'):
            products.extend(
                await self._fetch_products_by_id(
                    query['entities']['product_id']
                )
            )
        
        # Semantic product search
        query_vector = self.embedder.encode(query['normalized']).tolist()
        
        semantic_products = self.qdrant.search(
            collection_name=self.product_collection,
            query_vector=query_vector,
            limit=top_k,
            score_threshold=0.6
        )
        
        # Enrich with real-time data
        for hit in semantic_products:
            product_data = {
                'content': hit.payload.get('description', ''),
                'metadata': hit.payload.get('metadata', {}),
                'score': hit.score,
                'source': 'product',
                'id': hit.id
            }
            
            if use_realtime:
                # Fetch live inventory, pricing
                realtime_data = await self._fetch_realtime_data(
                    hit.payload['product_id']
                )
                product_data['metadata'].update(realtime_data)
            
            products.append(product_data)
        
        return products[:top_k]
    
    async def _fetch_realtime_data(self, product_id: str) -> Dict:
        """Fetch live product data from API/DB"""
        # Simulate API call (replace with actual implementation)
        await asyncio.sleep(0.05)  # Simulated latency
        
        return {
            'stock_status': 'in_stock',
            'current_price': 29.99,
            'discount': 0.15,
            'estimated_delivery': '2-3 days',
            'last_updated': 'real-time'
        }
    
    async def _fetch_products_by_id(self, product_ids: List[str]) -> List[Dict]:
        """Direct product lookup by ID"""
        products = []
        for pid in product_ids:
            result = self.qdrant.retrieve(
                collection_name=self.product_collection,
                ids=[pid]
            )
            if result:
                products.extend([
                    {
                        'content': r.payload.get('description', ''),
                        'metadata': r.payload,
                        'score': 1.0,  # Perfect match
                        'source': 'product_direct',
                        'id': r.id
                    }
                    for r in result
                ])
        return products
    
    def _merge_results(self, semantic, keyword):
        """Merge and deduplicate results"""
        seen_ids = set()
        merged = []
        
        for hit in semantic + keyword:
            if hit.id not in seen_ids:
                merged.append(hit)
                seen_ids.add(hit.id)
        
        # Sort by score
        merged.sort(key=lambda x: x.score, reverse=True)
        return merged
```

**Retrieval Strategy:**
- **FAQ Path**: Semantic + keyword hybrid search on static knowledge base
- **Product Path**: Real-time API calls + semantic search with inventory updates
- **Parallel Execution**: Both paths run concurrently for speed

---

### **4. Context Fusion & Reranking**

**File:** `services/reranker.py`

```python
import cohere
from typing import List, Dict
from sentence_transformers import SentenceTransformer

class ContextFusion:
    def __init__(self):
        self.cohere = cohere.Client(api_key="your-key")
    
    async def fuse_and_rerank(
        self,
        query: str,
        chunks: List[Dict],
        top_k: int = 5
    ) -> List[Dict]:
        """Rerank and fuse contexts"""
        
        if not chunks:
            return []
        
        # Prepare documents for reranking
        documents = [chunk['content'] for chunk in chunks]
        
        # Cohere rerank
        reranked = self.cohere.rerank(
            query=query,
            documents=documents,
            top_n=top_k,
            model='rerank-english-v2.0'
        )
        
        # Map back to original chunks with new scores
        reranked_chunks = []
        for result in reranked:
            original_chunk = chunks[result.index]
            original_chunk['rerank_score'] = result.relevance_score
            original_chunk['final_score'] = self._compute_final_score(
                original_chunk
            )
            reranked_chunks.append(original_chunk)
        
        # Deduplicate similar content
        final_chunks = self._deduplicate(reranked_chunks)
        
        return final_chunks[:top_k]
    
    def _compute_final_score(self, chunk: Dict) -> float:
        """Weighted scoring"""
        weights = {
            'retrieval': 0.3,
            'rerank': 0.5,
            'source': 0.2
        }
        
        source_boost = {
            'faq': 1.0,
            'product_direct': 1.2,
            'product': 1.0
        }
        
        score = (
            chunk.get('score', 0) * weights['retrieval'] +
            chunk.get('rerank_score', 0) * weights['rerank'] +
            source_boost.get(chunk['source'], 1.0) * weights['source']
        )
        
        return score
    
    def _deduplicate(self, chunks: List[Dict], threshold: float = 0.85) -> List[Dict]:
        """Remove near-duplicate chunks"""
        from sklearn.metrics.pairwise import cosine_similarity
        
        if len(chunks) <= 1:
            return chunks
        
        # Compute embeddings for deduplication
        embedder = SentenceTransformer('all-MiniLM-L6-v2')
        embeddings = embedder.encode([c['content'] for c in chunks])
        
        # Compute similarity matrix
        similarity_matrix = cosine_similarity(embeddings)
        
        # Keep only distinct chunks
        unique_indices = []
        for i in range(len(chunks)):
            is_unique = True
            for j in unique_indices:
                if similarity_matrix[i][j] > threshold:
                    is_unique = False
                    break
            if is_unique:
                unique_indices.append(i)
        
        return [chunks[i] for i in unique_indices]
```

**Reranking Benefits:**
- Improves relevance by 15-25% over pure vector search
- Cross-encoder models understand query-document relationships better
- Removes near-duplicate content

---

### **5. Context Optimization**

**File:** `services/context_optimizer.py`

```python
class ContextOptimizer:
    def __init__(self, max_tokens: int = 3000):
        self.max_tokens = max_tokens
    
    def optimize(self, chunks: List[Dict]) -> str:
        """Build optimized context within token budget"""
        context_parts = []
        current_tokens = 0
        
        for chunk in chunks:
            content = chunk['content']
            metadata = chunk['metadata']
            source = chunk['source']
            
            # Format chunk with attribution
            formatted = self._format_chunk(content, metadata, source)
            chunk_tokens = self._estimate_tokens(formatted)
            
            if current_tokens + chunk_tokens <= self.max_tokens:
                context_parts.append(formatted)
                current_tokens += chunk_tokens
            else:
                break
        
        return "\n\n---\n\n".join(context_parts)
    
    def _format_chunk(self, content: str, metadata: Dict, source: str) -> str:
        """Format chunk with source attribution"""
        if source == 'product':
            return f"""[PRODUCT INFO]
{content}
Stock: {metadata.get('stock_status', 'N/A')}
Price: ${metadata.get('current_price', 'N/A')}
Delivery: {metadata.get('estimated_delivery', 'N/A')}
"""
        elif source == 'faq':
            return f"""[FAQ]
{content}
Category: {metadata.get('category', 'General')}
"""
        else:
            return content
    
    def _estimate_tokens(self, text: str) -> int:
        """Rough token estimation (1 token ≈ 4 chars)"""
        return len(text) // 4
```

**Token Budget Management:**
- Keeps context under 3000 tokens for cost control
- Prioritizes highest-scored chunks
- Adds source attribution for transparency

---

### **6. Complete Pipeline Orchestration**

**File:** `services/pipeline_orchestrator.py`

```python
from openai import OpenAI
from typing import List, Dict

class RAGOrchestrator:
    def __init__(self):
        self.preprocessor = QueryPreprocessor()
        self.router = IntentRouter()
        self.retriever = HybridRAGPipeline()
        self.reranker = ContextFusion()
        self.optimizer = ContextOptimizer()
        self.llm = OpenAI(api_key="your-key")
    
    async def process(self, user_query: str, conversation_history: List = None) -> Dict:
        """End-to-end RAG pipeline"""
        
        # Step 1: Preprocess
        processed_query = await self.preprocessor.process(user_query)
        
        # Step 2: Route
        routing_result = await self.router.route(processed_query)
        
        # Step 3: Retrieve (parallel)
        chunks = await self.retriever.retrieve(
            processed_query,
            routing_result
        )
        
        # Step 4: Rerank
        reranked_chunks = await self.reranker.fuse_and_rerank(
            user_query,
            chunks,
            top_k=5
        )
        
        # Step 5: Optimize context
        context = self.optimizer.optimize(reranked_chunks)
        
        # Step 6: Generate response
        response = await self._generate_response(
            user_query,
            context,
            conversation_history
        )
        
        # Step 7: Post-process
        final_response = self._post_process(response, reranked_chunks)
        
        return {
            'response': final_response,
            'sources': reranked_chunks,
            'intent': routing_result['primary_intent'].value,
            'confidence': self._calculate_confidence(reranked_chunks)
        }
    
    async def _generate_response(
        self,
        query: str,
        context: str,
        history: List
    ) -> str:
        """Generate LLM response"""
        
        prompt = f"""You are a helpful customer support AI assistant. Use the provided context to answer the user's question accurately.

CONTEXT:
{context}

CONVERSATION HISTORY:
{self._format_history(history)}

USER QUESTION: {query}

INSTRUCTIONS:
- Answer based on the context provided
- If the context contains product info, include pricing and availability
- If you're not certain, say so
- Be concise but informative
- Cite sources when mentioning specific information

RESPONSE:"""
        
        response = await self.llm.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content
    
    def _post_process(self, response: str, chunks: List[Dict]) -> str:
        """Add citations and confidence indicators"""
        # Add source citations
        sources = set(chunk['source'] for chunk in chunks)
        
        citation = "\n\n---\n📚 Sources: " + ", ".join(sources)
        
        return response + citation
    
    def _calculate_confidence(self, chunks: List[Dict]) -> float:
        """Calculate response confidence score"""
        if not chunks:
            return 0.0
        
        avg_score = sum(c.get('final_score', 0) for c in chunks) / len(chunks)
        return min(avg_score, 1.0)
    
    def _format_history(self, history: List) -> str:
        """Format conversation history"""
        if not history:
            return "No previous context"
        
        formatted = []
        for msg in history[-5:]:  # Last 5 messages
            role = msg.get('role', 'user')
            content = msg.get('content', '')
            formatted.append(f"{role.upper()}: {content}")
        
        return "\n".join(formatted)
```

---

## 📈 Performance Optimization

### **Caching Layer**

**File:** `core/cache.py`

```python
import hashlib
import json
from redis import Redis

class RAGCache:
    def __init__(self, redis_client: Redis):
        self.redis = redis_client
        self.ttl = 300  # 5 minutes
    
    async def get_cached_retrieval(self, query: str) -> List[Dict]:
        """Get cached retrieval results"""
        cache_key = self._generate_key(query)
        cached = await self.redis.get(cache_key)
        
        if cached:
            return json.loads(cached)
        return None
    
    async def cache_retrieval(self, query: str, results: List[Dict]):
        """Cache retrieval results"""
        cache_key = self._generate_key(query)
        await self.redis.setex(
            cache_key,
            self.ttl,
            json.dumps(results)
        )
    
    def _generate_key(self, query: str) -> str:
        """Generate cache key"""
        return f"rag:retrieval:{hashlib.md5(query.encode()).hexdigest()}"
```

### **Monitoring & Metrics**

**File:** `utils/monitoring.py`

```python
from prometheus_client import Histogram, Counter

# Metrics
retrieval_latency = Histogram(
    'rag_retrieval_latency_seconds',
    'Time spent in retrieval',
    ['source_type']
)

rerank_latency = Histogram(
    'rag_rerank_latency_seconds',
    'Time spent in reranking'
)

context_relevance = Histogram(
    'rag_context_relevance_score',
    'Average relevance score of retrieved contexts'
)

cache_hits = Counter(
    'rag_cache_hits_total',
    'Number of cache hits'
)

cache_misses = Counter(
    'rag_cache_misses_total',
    'Number of cache misses'
)
```

---

## 🎯 Performance Targets

| Metric | Target | Typical Range |
|--------|--------|---------------|
| **Total Pipeline Latency** | < 1.2s | 0.8-1.5s |
| **FAQ Retrieval** | < 200ms | 150-300ms |
| **Product Retrieval (real-time)** | < 400ms | 300-600ms |
| **Reranking** | < 150ms | 100-200ms |
| **LLM Generation** | < 800ms | 600-1200ms |
| **Cache Hit Rate** | > 40% | 30-60% |
| **Retrieval Accuracy (MRR@5)** | > 0.85 | 0.80-0.90 |

---

## 🔧 Configuration

### **Environment Variables**

```bash
# .env
OPENAI_API_KEY=sk-...
COHERE_API_KEY=...
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=...
REDIS_URL=redis://localhost:6379
POSTGRES_URL=postgresql://user:pass@localhost:5432/db

# RAG Settings
RAG_MAX_CONTEXT_TOKENS=3000
RAG_TOP_K=5
RAG_RERANK_TOP_N=5
RAG_CACHE_TTL=300

# Model Settings
EMBEDDING_MODEL=all-MiniLM-L6-v2
LLM_MODEL=gpt-4
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=500
```

---



