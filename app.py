import os
from flask import Flask, request, render_template_string, session
from dotenv import load_dotenv
from enhanced_chatbot import EnhancedNikeChatbot

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your-secret-key-here')

# Initialize chatbot
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    print("Warning: OPENAI_API_KEY not found in environment variables")
    openai_api_key = 'your-openai-api-key-here'

chatbot = EnhancedNikeChatbot(openai_api_key)

# HTML template with embedded CSS and JavaScript
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nike Customer Support Chatbot</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            max-width: 800px;
            width: 100%;
            overflow: hidden;
            height: 80vh;
            display: flex;
            flex-direction: column;
        }
        
        .header {
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
            color: white;
            padding: 30px;
            text-align: center;
            position: relative;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            position: relative;
            z-index: 1;
        }
        
        .header p {
            font-size: 1.2em;
            opacity: 0.9;
            position: relative;
            z-index: 1;
        }
        
        .chat-container {
            flex: 1;
            overflow-y: auto;
            padding: 30px;
            background: #f8f9fa;
            border-bottom: 1px solid #e9ecef;
        }
        
        .message {
            margin-bottom: 20px;
            padding: 15px 20px;
            border-radius: 15px;
            max-width: 80%;
            line-height: 1.6;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .user-message {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            margin-left: auto;
            border-bottom-right-radius: 5px;
        }
        
        .bot-message {
            background: white;
            color: #333;
            border: 1px solid #e9ecef;
            border-bottom-left-radius: 5px;
        }
        
        .input-container {
            padding: 30px;
            background: white;
        }
        
        .input-form {
            display: flex;
            gap: 15px;
            align-items: center;
        }
        
        .input-field {
            flex: 1;
            padding: 15px 20px;
            border: 2px solid #e9ecef;
            border-radius: 25px;
            font-size: 16px;
            outline: none;
            transition: all 0.3s ease;
        }
        
        .input-field:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        .send-button {
            padding: 15px 25px;
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
            color: white;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            min-width: 80px;
        }
        
        .send-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 107, 107, 0.3);
        }
        
        .welcome-message {
            text-align: center;
            padding: 40px 20px;
            color: #666;
            font-size: 1.1em;
        }
        
        .welcome-message h3 {
            margin-bottom: 15px;
            color: #333;
        }
        
        .feature-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }
        
        .feature-item {
            background: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .feature-item strong {
            color: #ff6b6b;
            display: block;
            margin-bottom: 5px;
        }
        
        @media (max-width: 600px) {
            .header h1 {
                font-size: 2em;
            }
            
            .input-form {
                flex-direction: column;
            }
            
            .input-field, .send-button {
                width: 100%;
            }
            
            .container {
                height: 90vh;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Nike Customer Support</h1>
            <p>Get instant help with your Nike sneaker questions</p>
        </div>
        
        <div class="chat-container" id="chatContainer">
            {% if messages %}
                {% for message in messages %}
                    <div class="message {{ 'user-message' if message.type == 'user' else 'bot-message' }}">
                        {{ message.content | safe }}
                    </div>
                {% endfor %}
            {% else %}
                <div class="welcome-message">
                    <h3>Welcome to Nike Customer Support! 👋</h3>
                    <p>I'm here to help you with all your Nike sneaker questions. I can assist you with:</p>
                    <div class="feature-list">
                        <div class="feature-item">
                            <strong>Product Info</strong>
                            Ask about specific Nike models, pricing, and availability
                        </div>
                        <div class="feature-item">
                            <strong>Sizing Help</strong>
                            Get sizing recommendations and fit advice
                        </div>
                        <div class="feature-item">
                            <strong>Shipping</strong>
                            Track orders and learn about delivery options
                        </div>
                        <div class="feature-item">
                            <strong>Returns</strong>
                            Information about our return and exchange policy
                        </div>
                    </div>
                    <p style="margin-top: 20px;"><strong>Just type your question below to get started!</strong></p>
                </div>
            {% endif %}
        </div>
        
        <div class="input-container">
            <form class="input-form" method="POST" id="chatForm">
                <input type="text" name="message" class="input-field" placeholder="Ask me anything about Nike sneakers..." required id="messageInput">
                <button type="submit" class="send-button">Send</button>
            </form>
        </div>
    </div>
    
    <script>
        // Auto-scroll to bottom of chat
        function scrollToBottom() {
            const chatContainer = document.getElementById('chatContainer');
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
        
        // Focus on input field
        document.getElementById('messageInput').focus();
        
        // Scroll to bottom on page load
        scrollToBottom();
        
        // Handle form submission
        document.getElementById('chatForm').addEventListener('submit', function() {
            setTimeout(scrollToBottom, 100);
        });
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def chat():
    # Initialize session messages if not exists
    if 'messages' not in session:
        session['messages'] = []
    
    if request.method == 'POST':
        user_message = request.form.get('message', '').strip()
        
        if user_message:
            # Add user message to session
            session['messages'].append({
                'type': 'user',
                'content': user_message
            })
            
            # Get bot response
            bot_response = chatbot.process_query(user_message)
            
            # Add bot response to session
            session['messages'].append({
                'type': 'bot',
                'content': bot_response
            })
            
            # Keep only last 20 messages to prevent session overflow
            if len(session['messages']) > 20:
                session['messages'] = session['messages'][-20:]
            
            session.modified = True
    
    return render_template_string(HTML_TEMPLATE, messages=session['messages'])

@app.route('/clear')
def clear_chat():
    """Clear chat history"""
    session['messages'] = []
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)