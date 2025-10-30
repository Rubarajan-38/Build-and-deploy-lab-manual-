"""
Enhanced Nike Chatbot with ML-based intent classification
"""

import random
import openai
from data import FAQ_DATA, NIKE_PRODUCTS
from ml_trainer import intent_classifier
from nlp_processor import NLPProcessor

class EnhancedNikeChatbot:
    def __init__(self, openai_api_key):
        self.nlp = NLPProcessor()
        self.classifier = intent_classifier
        self.confidence_threshold = 0.3
        openai.api_key = openai_api_key
        
        # Train the classifier on startup
        self.classifier.train()
        
    def process_query(self, user_query):
        """Main query processing function with ML intent classification"""
        if not user_query or not user_query.strip():
            return "Please ask me a question about Nike sneakers and I'll be happy to help!"
        
        print(f"Processing query: {user_query}")
        
        # Step 1: Check for specific product mentions
        product_name, product_details = self.check_product_mention(user_query)
        if product_name and product_details:
            return self.format_product_response(product_name, product_details)
        
        # Step 2: Use ML intent classification
        predicted_intent, confidence = self.classifier.predict_intent(user_query)
        
        print(f"Predicted intent: {predicted_intent}, Confidence: {confidence:.3f}")
        
        if predicted_intent and confidence >= self.confidence_threshold:
            # High confidence - return FAQ response
            faq_response = self.get_faq_response(predicted_intent)
            if faq_response:
                return f"**Nike Customer Support:** {faq_response}"
        
        # Step 3: Fallback to OpenAI or rule-based response
        return self.get_openai_response(user_query)
    
    def check_product_mention(self, query):
        """Check if query mentions specific Nike products"""
        query_lower = query.lower()
        for product_name, details in NIKE_PRODUCTS.items():
            if product_name.lower() in query_lower:
                return product_name, details
        
        # Check for common product keywords
        product_keywords = {
            'air max': 'Air Max 270',
            'jordan': 'Air Jordan 1 Retro High',
            'react': 'React Element 55',
            'pegasus': 'Zoom Pegasus 39',
            'dunk': 'Dunk Low'
        }
        
        for keyword, product_name in product_keywords.items():
            if keyword in query_lower:
                return product_name, NIKE_PRODUCTS[product_name]
        
        return None, None
    
    def format_product_response(self, product_name, product_details):
        """Format product information response"""
        return f"""**{product_name}**

{product_details['description']}

💰 **Price:** {product_details['price']}
📏 **Sizes:** {product_details['sizes']}
🎨 **Colors:** {product_details['colors']}

Would you like more information about this product or help with sizing?"""
    
    def get_faq_response(self, intent):
        """Get a random response from FAQ category"""
        if intent in FAQ_DATA:
            return random.choice(FAQ_DATA[intent]['responses'])
        return None
    
    def get_openai_response(self, query):
        """Get response from OpenAI when intent classification fails"""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a knowledgeable Nike sneaker store assistant. Provide helpful, accurate information about Nike products, sizing, shipping, returns, and general customer service. Keep responses under 150 words and be friendly and professional."},
                    {"role": "user", "content": query}
                ],
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"OpenAI API Error: {e}")
            return self.get_fallback_response(query)
    
    def get_fallback_response(self, query):
        """Provide fallback responses when OpenAI is unavailable"""
        query_lower = query.lower()
        
        if any(word in query_lower for word in ['hi', 'hello', 'hey']):
            return "Hello! Welcome to Nike Customer Support. I'm here to help you with any questions about our sneakers, sizing, shipping, returns, or anything else Nike-related. How can I assist you today?"
        
        if any(word in query_lower for word in ['size', 'fit']):
            return "For sizing help: Nike sneakers generally run true to size. I recommend checking our size chart on the website. If you're between sizes, go half a size up. Would you like specific sizing advice for a particular Nike model?"
        
        if any(word in query_lower for word in ['shipping', 'delivery']):
            return "Shipping Information: Standard shipping takes 3-5 business days ($5). Free shipping on orders over $50. Express shipping (1-2 days) is $15. Overnight shipping is $25."
        
        if any(word in query_lower for word in ['return', 'refund']):
            return "Returns & Exchanges: Nike offers a 30-day return policy for unworn items in original packaging. Returns are free with our prepaid return label."
        
        return "Thank you for contacting Nike Customer Support! I'm here to help with questions about our sneakers, sizing, shipping, returns, and more. Could you please provide more details about what you're looking for?"
    
    def get_training_stats(self):
        """Get training statistics"""
        return self.classifier.get_training_stats()