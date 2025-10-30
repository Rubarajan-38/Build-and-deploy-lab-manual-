# Nike Customer Support Chatbot

A production-ready MVP chatbot for Nike Sneaker Store customer support, built with Flask, NLTK, and integrated with OpenAI's GPT for enhanced conversational capabilities.

## Features

### Core Functionality
- **Flask Backend**: Clean Python Flask application with render_template_string()
- **NLTK Integration**: Word tokenization, lemmatization, and stopword removal
- **FAQ Knowledge Base**: Comprehensive database of Nike sneaker-related questions
- **OpenAI Integration**: GPT-3.5 fallback for complex queries (confidence threshold < 0.8)
- **Product Information**: Detailed Nike sneaker catalog with pricing and specifications
- **Responsive UI**: Clean, modern interface embedded in Flask template

### Supported Query Types
- **Product Information**: Air Max, Jordan, React, Zoom, Dunk, and more
- **Sizing Advice**: Fit recommendations and size chart guidance
- **Shipping Details**: Delivery options, tracking, and international shipping
- **Returns & Exchanges**: Policy information and warranty details
- **Price Inquiries**: Current pricing and discount information
- **Care Instructions**: Cleaning and maintenance tips

## Technical Stack

- **Backend**: Flask with render_template_string()
- **NLP**: NLTK (tokenization, lemmatization, stopwords)
- **AI Integration**: OpenAI GPT-3.5 with confidence-based fallback
- **Database**: In-memory FAQ storage (easily extensible to SQL)
- **Frontend**: Responsive HTML/CSS embedded in Flask template

## Installation

### Prerequisites
- Python 3.8+
- OpenAI API key

### Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Run setup script (downloads NLTK data)
python setup.py

# Add your OpenAI API key to .env file
# Edit .env and replace 'your-openai-api-key-here' with your actual key

# Start the application
python app.py
```

### Manual Installation
```bash
# Install dependencies
pip install flask openai nltk python-dotenv

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"

# Create environment file
cp .env.example .env
# Edit .env with your OpenAI API key

# Run application
python app.py
```

## Configuration

### Environment Variables
Edit the `.env` file with:
```
OPENAI_API_KEY=your-actual-openai-api-key
FLASK_SECRET_KEY=your-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True
```

### OpenAI Settings
- **Model**: GPT-3.5-turbo
- **Temperature**: 0.7 (balanced creativity)
- **Max Tokens**: 150 (concise responses)
- **System Prompt**: "You are a knowledgeable Nike sneaker store assistant and manage shipping for it"
- **Trigger**: Confidence threshold < 0.8

## Usage

1. **Start the application**: `python app.py`
2. **Open browser**: Navigate to `http://localhost:5000`
3. **Start chatting**: Type your Nike sneaker questions in the input field

### Example Queries
- "What size should I get for Air Max 270?"
- "How much do Jordan 1s cost?"
- "What's your return policy?"
- "Do you have Air Force 1 in stock?"
- "How do I clean my Nike sneakers?"

## Architecture

### Query Processing Flow
1. **User Input**: Raw text query from web interface
2. **NLTK Processing**: Tokenization, stopword removal, lemmatization
3. **Intent Matching**: Compare against FAQ knowledge base using similarity scoring
4. **Confidence Scoring**: Calculate match confidence (0-1)
5. **Response Generation**: 
   - High confidence (≥0.8): Return FAQ response
   - Low confidence (<0.8): Query OpenAI GPT
6. **Response Formatting**: Format and return to user

### File Structure
```
nike-chatbot/
├── app.py              # Main Flask application
├── chatbot.py          # Chatbot logic and OpenAI integration
├── nlp_processor.py    # NLTK processing utilities
├── data.py             # FAQ knowledge base and product catalog
├── requirements.txt    # Python dependencies
├── setup.py           # Automated setup script
├── .env               # Environment variables
└── README.md          # This file
```

## Customization

### Adding New FAQs
Edit `data.py` to add new categories:
```python
FAQ_DATA["new_category"] = {
    "keywords": ["keyword1", "keyword2"],
    "responses": ["Response 1", "Response 2"]
}
```

### Adding New Products
Extend the `NIKE_PRODUCTS` dictionary:
```python
NIKE_PRODUCTS["Product Name"] = {
    "price": "$XXX",
    "description": "Product description",
    "sizes": "Size range",
    "colors": "Available colors"
}
```

### Adjusting AI Behavior
Modify the OpenAI system prompt in `chatbot.py`:
```python
{"role": "system", "content": "Your custom system prompt here"}
```

## API Integration

The chatbot uses OpenAI's ChatCompletion API with the following configuration:
- **Model**: gpt-3.5-turbo
- **Temperature**: 0.7
- **Max Tokens**: 150
- **Fallback Trigger**: FAQ confidence < 0.8

## Performance

- **Response Time**: <2 seconds for FAQ queries
- **AI Fallback**: <5 seconds for OpenAI queries
- **Memory Usage**: ~30MB base + NLTK data
- **Session Management**: Stores last 20 messages per user

## Security

- Environment variable configuration for API keys
- Session-based message storage (no persistent data)
- Input sanitization for all user queries
- Rate limiting through OpenAI API quotas

## Troubleshooting

### Common Issues

**NLTK Download Errors**
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

**OpenAI API Errors**
- Verify your API key is correct in `.env`
- Check your OpenAI account has sufficient credits
- Ensure your API key has the correct permissions

**Flask Port Issues**
```bash
# The app runs on port 5000 by default
# Access at: http://localhost:5000
```

