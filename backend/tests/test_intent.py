from backend.app.services.intent import classify


def test_intent_matches_keywords():
    assert classify("What is the return policy?") == "return"
    assert classify("Tell me about the product size") == "product_info"

