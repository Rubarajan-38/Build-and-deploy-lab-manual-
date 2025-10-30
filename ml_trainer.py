"""
Machine Learning trainer for Nike Customer Support Chatbot
Implements TF-IDF and similarity-based intent classification
"""

import re
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from training_data import TRAINING_DATA, INTENT_PATTERNS
from nlp_processor import NLPProcessor

class IntentClassifier:
    def __init__(self):
        self.nlp = NLPProcessor()
        self.vectorizer = TfidfVectorizer(
            max_features=1000,
            stop_words='english',
            ngram_range=(1, 2)
        )
        self.training_vectors = None
        self.training_intents = None
        self.is_trained = False
        
    def train(self):
        """Train the intent classifier using training data"""
        print("Training intent classifier...")
        
        # Prepare training data
        training_queries = []
        training_intents = []
        
        for example in TRAINING_DATA:
            # Process query with NLP
            processed_tokens, _ = self.nlp.process_query(example["query"])
            processed_query = " ".join(processed_tokens)
            
            training_queries.append(processed_query)
            training_intents.append(example["intent"])
        
        # Create TF-IDF vectors
        self.training_vectors = self.vectorizer.fit_transform(training_queries)
        self.training_intents = training_intents
        self.is_trained = True
        
        print(f"✓ Trained on {len(training_queries)} examples")
        print(f"✓ Vocabulary size: {len(self.vectorizer.vocabulary_)}")
        
    def predict_intent(self, query, threshold=0.3):
        """Predict intent for a given query"""
        if not self.is_trained:
            self.train()
        
        # Process query
        processed_tokens, original_query = self.nlp.process_query(query)
        processed_query = " ".join(processed_tokens)
        
        # Check pattern matching first
        pattern_intent = self._check_patterns(original_query)
        if pattern_intent:
            return pattern_intent, 0.9
        
        # Create vector for query
        query_vector = self.vectorizer.transform([processed_query])
        
        # Calculate similarities
        similarities = cosine_similarity(query_vector, self.training_vectors)[0]
        
        # Find best match
        best_idx = np.argmax(similarities)
        best_score = similarities[best_idx]
        best_intent = self.training_intents[best_idx]
        
        if best_score >= threshold:
            return best_intent, best_score
        else:
            return None, best_score
    
    def _check_patterns(self, query):
        """Check if query matches any regex patterns"""
        query_lower = query.lower()
        
        for intent, patterns in INTENT_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, query_lower):
                    return intent
        
        return None
    
    def get_training_stats(self):
        """Get statistics about training data"""
        if not self.is_trained:
            return None
        
        intent_counts = Counter(self.training_intents)
        return {
            "total_examples": len(self.training_intents),
            "unique_intents": len(intent_counts),
            "intent_distribution": dict(intent_counts),
            "vocabulary_size": len(self.vectorizer.vocabulary_)
        }

# Global classifier instance
intent_classifier = IntentClassifier()