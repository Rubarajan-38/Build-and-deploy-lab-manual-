import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class NLPProcessor:
    def __init__(self):
        # Download required NLTK data
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt', quiet=True)
        
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords', quiet=True)
        
        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet', quiet=True)
        
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
        # Remove some words that might be important for Nike queries
        self.stop_words.discard('size')
        self.stop_words.discard('big')
        self.stop_words.discard('small')
        self.stop_words.discard('wide')
        self.stop_words.discard('narrow')
    
    def tokenize(self, text):
        """Tokenize text using NLTK"""
        try:
            tokens = word_tokenize(text.lower())
            # Keep only alphabetic tokens and numbers (for sizes)
            tokens = [token for token in tokens if token.isalpha() or token.isdigit()]
            return tokens
        except:
            # Fallback tokenization
            return re.findall(r'\b\w+\b', text.lower())
    
    def remove_stopwords(self, tokens):
        """Remove stopwords from tokens"""
        return [token for token in tokens if token not in self.stop_words]
    
    def lemmatize(self, tokens):
        """Lemmatize tokens using WordNet lemmatizer"""
        try:
            return [self.lemmatizer.lemmatize(token) for token in tokens]
        except:
            # Fallback - return tokens as is
            return tokens
    
    def process_query(self, query):
        """Process user query through complete NLP pipeline"""
        if not query:
            return [], ""
        
        # Clean the query
        query = re.sub(r'[^\w\s]', ' ', query)  # Remove punctuation
        query = re.sub(r'\s+', ' ', query).strip()  # Normalize whitespace
        
        # Tokenize
        tokens = self.tokenize(query)
        
        # Remove stopwords
        tokens = self.remove_stopwords(tokens)
        
        # Lemmatize
        tokens = self.lemmatize(tokens)
        
        return tokens, query.lower()