"""
Nike Sneaker Store FAQ Knowledge Base
Contains common customer inquiries and responses
"""

FAQ_DATA = {
    "greeting": {
        "keywords": ["hi", "hello", "hey", "good morning", "good afternoon", "good evening", "greetings"],
        "responses": [
            "Hello! Welcome to Nike Customer Support. I'm here to help you with any questions about our sneakers, sizing, shipping, returns, or anything else Nike-related. How can I assist you today?",
            "Hi there! Thanks for contacting Nike Customer Support. I can help you with product information, sizing advice, shipping details, returns, and more. What can I do for you?",
            "Hey! Welcome to Nike! I'm your customer support assistant, ready to help with all your Nike sneaker questions. What would you like to know?"
        ]
    },
    
    "sizing": {
        "keywords": ["size", "fit", "sizing", "big", "small", "wide", "narrow", "length", "width", "measurement", "chart"],
        "responses": [
            "Nike sneakers generally run true to size. For the best fit, we recommend measuring your foot and checking our size chart on the website. If you're between sizes, we suggest going half a size up.",
            "For sizing help: Nike Air Max models tend to run slightly large, while Nike Free and Flyknit models run true to size. Would you like specific sizing advice for a particular model?",
            "For wide feet, consider Nike models with 'Wide' options or go half a size up. Nike Air Monarch and Air Max 90 are great options for wider feet. Need help with a specific model?"
        ]
    },
    
    "returns": {
        "keywords": ["return", "refund", "exchange", "money back", "unworn", "defective", "wrong size", "policy"],
        "responses": [
            "Nike offers a 30-day return policy for unworn items in original packaging. Returns are free with our prepaid return label. Just visit our website to start the return process.",
            "You can return or exchange Nike sneakers within 30 days of purchase. Items must be unworn and in original condition with all tags attached. We'll email you a prepaid return label.",
            "For defective products, we offer a 2-year warranty. Please contact us with photos of the defect for immediate assistance. We'll replace or refund defective items right away."
        ]
    },
    
    "shipping": {
        "keywords": ["shipping", "delivery", "fast", "expedited", "overnight", "tracking", "when will", "arrive", "ship"],
        "responses": [
            "Standard shipping takes 3-5 business days and costs $5. Free shipping on orders over $50. Express shipping (1-2 days) is available for $15.",
            "We offer overnight shipping for $25. All orders placed before 2 PM EST ship the same day. You'll receive tracking information via email once your order ships.",
            "International shipping is available to most countries. Delivery times vary by location (7-14 business days) with costs starting at $20. Duties and taxes may apply."
        ]
    },
    
    "availability": {
        "keywords": ["stock", "available", "sold out", "restock", "when back", "inventory", "in stock", "out of stock"],
        "responses": [
            "You can check real-time availability on our website. Popular sizes tend to sell out quickly, so we recommend signing up for restock notifications on product pages.",
            "Most Nike sneakers are restocked regularly. Sign up for our newsletter to get notified about restocks and new releases. You can also follow us on social media for updates.",
            "Limited edition and collaboration sneakers have limited availability. Follow our social media accounts for release updates and drop times. SNKRS app users get early access!"
        ]
    },
    
    "products": {
        "keywords": ["air max", "jordan", "react", "zoom", "dunk", "blazer", "cortez", "air force", "product", "shoe", "sneaker", "model"],
        "responses": [
            "We have an amazing selection of Nike sneakers! Popular models include Air Max 270 ($150), Air Jordan 1 ($170), React Element 55 ($130), Zoom Pegasus 39 ($130), and Dunk Low ($100). What style interests you?",
            "Our top Nike sneakers: Air Max for maximum comfort, Jordan for iconic style, React for responsive cushioning, Zoom for performance, and Dunk for retro vibes. Which category appeals to you?",
            "Nike offers something for everyone! From running shoes like Pegasus to lifestyle sneakers like Air Max, basketball shoes like Jordan, and skateboarding shoes like Dunk. What's your intended use?"
        ]
    },
    
    "price": {
        "keywords": ["price", "cost", "expensive", "cheap", "sale", "discount", "deal", "coupon", "promo", "money"],
        "responses": [
            "Nike sneaker prices range from $80-$200 depending on the model and technology. Check our website for current pricing and ongoing sales. We often have seasonal promotions!",
            "We regularly offer seasonal sales with up to 30% off select styles. Sign up for our newsletter to receive exclusive discount codes and be first to know about sales.",
            "Special discounts available: Students get 10% off with valid student ID, Military personnel receive 15% off with verification, Healthcare workers get 20% off. Verify your status on our website!"
        ]
    },
    
    "care": {
        "keywords": ["clean", "wash", "care", "maintain", "protect", "waterproof", "stain", "cleaning"],
        "responses": [
            "Clean Nike sneakers with mild soap and water using a soft brush. Remove laces and insoles first. Air dry only - never put them in the dryer as heat can damage materials.",
            "For leather Nike shoes, use a leather cleaner and conditioner. For mesh and fabric materials, spot clean with gentle detergent. Avoid harsh chemicals that can damage colors.",
            "Nike offers waterproofing sprays and cleaning kits specifically designed for our sneakers. Available in stores and online. Regular cleaning extends the life of your shoes!"
        ]
    },
    
    "warranty": {
        "keywords": ["warranty", "defect", "broken", "manufacturing", "quality", "guarantee", "problem"],
        "responses": [
            "Nike provides a 2-year warranty against manufacturing defects. This covers issues like sole separation, upper tearing, or hardware failure - not normal wear and tear.",
            "For warranty claims, please provide photos of the issue and proof of purchase. We'll review your case and provide a replacement or refund for valid manufacturing defects.",
            "We stand behind our quality! If you experience any manufacturing defects within 2 years, we'll make it right with a replacement or refund. Contact us with details and photos."
        ]
    }
}

# Nike product catalog for detailed inquiries
NIKE_PRODUCTS = {
    "Air Max 270": {
        "price": "$150",
        "description": "Experience maximum comfort with our largest Air unit ever. The Air Max 270 delivers exceptional all-day comfort with its innovative design and premium materials.",
        "sizes": "Men's 6-14, Women's 5-12 (including half sizes)",
        "colors": "15+ colorways including Black/White, Triple White, Rainbow, and seasonal releases"
    },
    "Air Jordan 1 Retro High": {
        "price": "$170",
        "description": "The iconic basketball silhouette that started it all. Premium leather construction meets timeless design in this legendary sneaker that transcends sports and culture.",
        "sizes": "Men's 6-18, Women's 5-15 (including half sizes)",
        "colors": "Multiple colorways including Chicago, Bred, Royal, Shadow, and limited collaborations"
    },
    "React Element 55": {
        "price": "$130",
        "description": "Lightweight React foam technology provides bouncy, responsive cushioning with every step. Modern design meets innovative comfort technology.",
        "sizes": "Men's 6-13, Women's 5-12 (including half sizes)",
        "colors": "8 colorways including Black/White, Triple Black, Bright Crimson, and seasonal options"
    },
    "Zoom Pegasus 39": {
        "price": "$130",
        "description": "Our most popular running shoe trusted by millions of runners worldwide. Features responsive Zoom Air cushioning and breathable mesh upper.",
        "sizes": "Men's 6-15, Women's 5-12 (including half sizes)",
        "colors": "12 colorways including classic Black/White, vibrant seasonal colors, and special editions"
    },
    "Dunk Low": {
        "price": "$100",
        "description": "Retro basketball shoe reimagined for modern style. Classic silhouette with updated comfort features and premium materials.",
        "sizes": "Men's 6-14, Women's 5-12 (including half sizes)",
        "colors": "20+ colorways including Panda, University Blue, Chicago, and exclusive collaborations"
    },
    "Air Force 1": {
        "price": "$90",
        "description": "The legendary basketball shoe that became a cultural icon. Clean, classic design with premium leather and Air cushioning.",
        "sizes": "Men's 6-18, Women's 5-15 (including half sizes)",
        "colors": "Triple White, Triple Black, and 50+ seasonal colorways and collaborations"
    },
    "Blazer Mid": {
        "price": "$100",
        "description": "Vintage basketball style meets modern comfort. Premium suede and leather construction with classic Nike styling.",
        "sizes": "Men's 6-13, Women's 5-12 (including half sizes)",
        "colors": "Classic colorways and seasonal releases including vintage-inspired options"
    }
}