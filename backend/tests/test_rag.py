from backend.app.services.retriever import search


def test_retriever_returns_results():
    results = search("noise cancelling headphones")
    assert results
    assert all("score" in r for r in results)

