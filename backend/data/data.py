"""Lightweight in-memory corpus used by the RAG pipeline."""

FAQS = [
    {
        "id": "faq_1",
        "question": "How do I track my order?",
        "answer": "You can track your order from the Orders page using the tracking link.",
    },
    {
        "id": "faq_2",
        "question": "What is the return policy?",
        "answer": "Returns are accepted within 30 days of delivery in original condition.",
    },
    {
        "id": "faq_3",
        "question": "How do I contact support?",
        "answer": "Email support@example.com or start a chat from the help center.",
    },
]

PRODUCTS = [
    {
        "id": "product_1",
        "name": "Noise Cancelling Headphones",
        "description": "Over-ear headphones with 30h battery life and ANC.",
    },
    {
        "id": "product_2",
        "name": "Smartwatch Pro",
        "description": "Water-resistant smartwatch with GPS and heart-rate monitor.",
    },
    {
        "id": "product_3",
        "name": "USB-C Charger",
        "description": "65W GaN charger compatible with laptops and phones.",
    },
]


def corpus() -> list:
    """Return combined FAQ and product docs for retrieval."""
    docs = []
    for item in FAQS:
        docs.append(
            {
                "id": item["id"],
                "type": "faq",
                "title": item["question"],
                "body": item["answer"],
            }
        )
    for item in PRODUCTS:
        docs.append(
            {
                "id": item["id"],
                "type": "product",
                "title": item["name"],
                "body": item["description"],
            }
        )
    return docs

