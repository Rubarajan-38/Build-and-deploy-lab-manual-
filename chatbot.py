import random
import openai
from difflib import SequenceMatcher
from data import FAQ_DATA, NIKE_PRODUCTS
from nlp_processor import NLPProcessor

class NikeChatbot:
    def __init__(self, openai_api_key):
        self.nlp = NLPProcessor()
        self.confidence_threshold = 0.3  # Lowered threshold for better matching
        openai.api_key = openai_api_key
    
    def calculate_similarity(self, query_tokens, keywords):
        """Calculate similarity between query tokens and keywords"""
        if not query_tokens or not keywords:
            return 0
        
        # Check for direct keyword matches
        matches = 0
        for token in query_tokens:
            for keyword in keywords:
                if token in keyword or keyword in token:
                    matches += 1
                    break
        
        # Calculate similarity score
        similarity = matches / len(query_tokens) if query_tokens else 0
        return similarity
    
    def find_best_match(self, processed_query):
        """Find the best matching FAQ category"""
        query_tokens, original_query = processed_query
        best_match = None
        best_score = 0
        
        # Check each FAQ category
        for category, data in FAQ_DATA.items():
            # Direct keyword matching
            keyword_matches = 0
            for token in query_tokens:
                for keyword in data['keywords']:
                    if token.lower() in keyword.lower() or keyword.lower() in token.lower():
                        keyword_matches += 1
                        break
            
            # Calculate score based on keyword matches
            if len(query_tokens) > 0:
                score = keyword_matches / len(query_tokens)
            else:
                score = 0
            
            # Boost score for exact matches
            for keyword in data['keywords']:
                if keyword.lower() in original_query.lower():
                    score += 0.3
            
            if score > best_score:
                best_score = score
                best_match = category
        
        return best_match, best_score
    
    def check_product_mention(self, query):
        """Check if query mentions specific Nike products"""
        query_lower = query.lower()
        for product_name, details in NIKE_PRODUCTS.items():
            # Check for product name variations
            product_variations = [
                product_name.lower(),
                product_name.lower().replace(' ', ''),
                product_name.lower().replace(' ', '-')
            ]
            
            for variation in product_variations:
                if variation in query_lower:
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
    
    def get_faq_response(self, category):
        """Get a random response from FAQ category"""
        if category in FAQ_DATA:
            return random.choice(FAQ_DATA[category]['responses'])
        return None
    
    def get_openai_response(self, query):
        """Get response from OpenAI when FAQ confidence is low"""
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
        
        # Greeting responses
        if any(word in query_lower for word in ['hi', 'hello', 'hey', 'good morning', 'good afternoon']):
            return "Hello! Welcome to Nike Customer Support. I'm here to help you with any questions about our sneakers, sizing, shipping, returns, or anything else Nike-related. How can I assist you today?"
        
        # Sizing queries
        if any(word in query_lower for word in ['size', 'fit', 'sizing']):
            return "For sizing help: Nike sneakers generally run true to size. I recommend checking our size chart on the website. If you're between sizes, go half a size up. Would you like specific sizing advice for a particular Nike model?"
        
        # Shipping queries
        if any(word in query_lower for word in ['shipping', 'delivery', 'ship']):
            return "Shipping Information: Standard shipping takes 3-5 business days ($5). Free shipping on orders over $50. Express shipping (1-2 days) is $15. Overnight shipping is $25. All orders placed before 2 PM EST ship same day."
        
        # Return queries
        if any(word in query_lower for word in ['return', 'refund', 'exchange']):
            return "Returns & Exchanges: Nike offers a 30-day return policy for unworn items in original packaging. Returns are free with our prepaid return label. For defective products, we offer a 2-year warranty."
        
        # Product queries
        if any(word in query_lower for word in ['product', 'shoe', 'sneaker', 'nike']):
            return "I can help you with information about Nike products! We have Air Max, Jordan, React, Zoom, Dunk, and many other popular models. What specific Nike sneaker are you interested in learning about?"
        
        # Default response
        return "Thank you for contacting Nike Customer Support! I'm here to help with questions about our sneakers, sizing, shipping, returns, and more. Could you please provide more details about what you're looking for?"
    
    def process_query(self, user_query):
        """Main query processing function"""
        if not user_query or not user_query.strip():
            return "Please ask me a question about Nike sneakers and I'll be happy to help!"
        
        # Process query with NLP
        processed_query = self.nlp.process_query(user_query)
        
        # Check for specific product mentions first
        product_name, product_details = self.check_product_mention(user_query)
        if product_name and product_details:
            return f"**{product_name}**\n\n{product_details['description']}\n\n💰 **Price:** {product_details['price']}\n📏 **Sizes:** {product_details['sizes']}\n🎨 **Colors:** {product_details['colors']}\n\nWould you like more information about this product or help with sizing?"
        
        # Find best FAQ match
        best_category, confidence = self.find_best_match(processed_query)
        
        print(f"Query: {user_query}")
        print(f"Best category: {best_category}, Confidence: {confidence}")
        
        if best_category and confidence >= self.confidence_threshold:
            # High confidence - return FAQ response
            faq_response = self.get_faq_response(best_category)
            return f"**Nike Customer Support:** {faq_response}"
        else:
            # Low confidence - use OpenAI or fallback
            return self.get_openai_response(user_query)