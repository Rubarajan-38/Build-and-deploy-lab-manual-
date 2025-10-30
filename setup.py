#!/usr/bin/env python3
"""
Setup script for Nike Customer Support Chatbot
Downloads required NLTK data
"""

import os
import sys
import subprocess

def install_requirements():
    """Install required Python packages"""
    print("Installing required packages...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    print("✓ Packages installed successfully")

def setup_nltk():
    """Download required NLTK data"""
    print("Setting up NLTK data...")
    try:
        import nltk
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('wordnet', quiet=True)
        print("✓ NLTK data downloaded successfully")
    except Exception as e:
        print(f"⚠ NLTK setup failed: {e}")

def create_env_file():
    """Create .env file template"""
    env_content = """# Nike Customer Support Chatbot Environment Variables
OPENAI_API_KEY=your-openai-api-key-here
FLASK_SECRET_KEY=your-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True
"""
    
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✓ .env file created - Please add your OpenAI API key")
    else:
        print("✓ .env file already exists")

def main():
    """Main setup function"""
    print("🚀 Setting up Nike Customer Support Chatbot...")
    print("-" * 50)
    
    # Install requirements
    install_requirements()
    
    # Setup NLTK
    setup_nltk()
    
    # Create environment file
    create_env_file()
    
    print("-" * 50)
    print("✅ Setup complete!")
    print("\nNext steps:")
    print("1. Add your OpenAI API key to the .env file")
    print("2. Run: python app.py")
    print("3. Open: http://localhost:5000")

if __name__ == '__main__':
    main()