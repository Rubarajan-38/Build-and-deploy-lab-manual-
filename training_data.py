"""
Training data for Nike Customer Support Chatbot
Contains labeled examples for intent classification
"""

# Training examples with user queries and their corresponding intents
TRAINING_DATA = [
    # Sizing queries
    {"query": "What size should I get for Air Max?", "intent": "sizing", "confidence": 1.0},
    {"query": "Do Nike shoes run big or small?", "intent": "sizing", "confidence": 1.0},
    {"query": "I wear size 9 in Adidas, what Nike size?", "intent": "sizing", "confidence": 1.0},
    {"query": "Are Air Jordans true to size?", "intent": "sizing", "confidence": 1.0},
    {"query": "I have wide feet, what should I order?", "intent": "sizing", "confidence": 1.0},
    {"query": "Size chart for women's Nike", "intent": "sizing", "confidence": 1.0},
    {"query": "How do I measure my foot for Nike shoes?", "intent": "sizing", "confidence": 1.0},
    
    # Shipping queries
    {"query": "How long does shipping take?", "intent": "shipping", "confidence": 1.0},
    {"query": "Do you offer overnight delivery?", "intent": "shipping", "confidence": 1.0},
    {"query": "What are your shipping options?", "intent": "shipping", "confidence": 1.0},
    {"query": "Can I track my order?", "intent": "shipping", "confidence": 1.0},
    {"query": "Free shipping minimum order?", "intent": "shipping", "confidence": 1.0},
    {"query": "International shipping available?", "intent": "shipping", "confidence": 1.0},
    {"query": "When will my shoes arrive?", "intent": "shipping", "confidence": 1.0},
    
    # Return queries
    {"query": "What's your return policy?", "intent": "returns", "confidence": 1.0},
    {"query": "Can I return worn shoes?", "intent": "returns", "confidence": 1.0},
    {"query": "How do I return my order?", "intent": "returns", "confidence": 1.0},
    {"query": "Refund processing time?", "intent": "returns", "confidence": 1.0},
    {"query": "Exchange for different size?", "intent": "returns", "confidence": 1.0},
    {"query": "Return shipping label?", "intent": "returns", "confidence": 1.0},
    {"query": "Defective shoe warranty?", "intent": "returns", "confidence": 1.0},
    
    # Product queries
    {"query": "Tell me about Air Max 270", "intent": "products", "confidence": 1.0},
    {"query": "What Nike shoes are popular?", "intent": "products", "confidence": 1.0},
    {"query": "Air Jordan 1 price?", "intent": "products", "confidence": 1.0},
    {"query": "Best Nike running shoes?", "intent": "products", "confidence": 1.0},
    {"query": "New Nike releases?", "intent": "products", "confidence": 1.0},
    {"query": "Nike Dunk availability?", "intent": "products", "confidence": 1.0},
    {"query": "Difference between Air Max models?", "intent": "products", "confidence": 1.0},
    
    # Price queries
    {"query": "How much do Air Jordans cost?", "intent": "price", "confidence": 1.0},
    {"query": "Are there any sales right now?", "intent": "price", "confidence": 1.0},
    {"query": "Student discount available?", "intent": "price", "confidence": 1.0},
    {"query": "Price range for Nike sneakers?", "intent": "price", "confidence": 1.0},
    {"query": "Coupon codes for Nike?", "intent": "price", "confidence": 1.0},
    {"query": "When do Nike shoes go on sale?", "intent": "price", "confidence": 1.0},
    
    # Availability queries
    {"query": "Is Air Max 270 in stock?", "intent": "availability", "confidence": 1.0},
    {"query": "When will size 10 be restocked?", "intent": "availability", "confidence": 1.0},
    {"query": "Sold out shoes restock date?", "intent": "availability", "confidence": 1.0},
    {"query": "Check inventory for Jordan 1", "intent": "availability", "confidence": 1.0},
    {"query": "Notify me when back in stock", "intent": "availability", "confidence": 1.0},
    
    # Care queries
    {"query": "How to clean Nike shoes?", "intent": "care", "confidence": 1.0},
    {"query": "Can I wash Nike sneakers?", "intent": "care", "confidence": 1.0},
    {"query": "Shoe care products for Nike?", "intent": "care", "confidence": 1.0},
    {"query": "How to protect white sneakers?", "intent": "care", "confidence": 1.0},
    {"query": "Remove stains from Nike shoes", "intent": "care", "confidence": 1.0},
    
    # Greeting queries
    {"query": "Hi", "intent": "greeting", "confidence": 1.0},
    {"query": "Hello", "intent": "greeting", "confidence": 1.0},
    {"query": "Good morning", "intent": "greeting", "confidence": 1.0},
    {"query": "Hey there", "intent": "greeting", "confidence": 1.0},
    {"query": "I need help", "intent": "greeting", "confidence": 0.8},
]

# Negative examples (queries that should NOT match certain intents)
NEGATIVE_EXAMPLES = [
    {"query": "What's the weather like?", "intent": "none", "confidence": 0.0},
    {"query": "Tell me a joke", "intent": "none", "confidence": 0.0},
    {"query": "What time is it?", "intent": "none", "confidence": 0.0},
    {"query": "How to cook pasta?", "intent": "none", "confidence": 0.0},
]

# Intent patterns for better matching
INTENT_PATTERNS = {
    "sizing": [
        r"what size.*",
        r".*size.*should.*",
        r".*fit.*",
        r".*big.*small.*",
        r".*wide.*feet.*",
        r".*true.*size.*",
        r".*size.*chart.*"
    ],
    "shipping": [
        r".*shipping.*",
        r".*delivery.*",
        r".*arrive.*",
        r".*track.*order.*",
        r".*overnight.*",
        r".*express.*",
        r".*free.*shipping.*"
    ],
    "returns": [
        r".*return.*",
        r".*refund.*",
        r".*exchange.*",
        r".*warranty.*",
        r".*defective.*",
        r".*money.*back.*"
    ],
    "products": [
        r".*air.*max.*",
        r".*jordan.*",
        r".*dunk.*",
        r".*react.*",
        r".*zoom.*",
        r".*tell.*me.*about.*",
        r".*what.*nike.*"
    ],
    "price": [
        r".*price.*",
        r".*cost.*",
        r".*how.*much.*",
        r".*sale.*",
        r".*discount.*",
        r".*coupon.*",
        r".*cheap.*"
    ],
    "availability": [
        r".*stock.*",
        r".*available.*",
        r".*sold.*out.*",
        r".*restock.*",
        r".*inventory.*",
        r".*in.*stock.*"
    ],
    "care": [
        r".*clean.*",
        r".*wash.*",
        r".*care.*",
        r".*maintain.*",
        r".*protect.*",
        r".*stain.*"
    ]
}

def get_training_examples_by_intent(intent):
    """Get all training examples for a specific intent"""
    return [example for example in TRAINING_DATA if example["intent"] == intent]

def get_all_intents():
    """Get list of all available intents"""
    return list(set([example["intent"] for example in TRAINING_DATA]))

def get_training_queries():
    """Get all training queries as a list"""
    return [example["query"] for example in TRAINING_DATA]