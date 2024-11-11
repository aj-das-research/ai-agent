# AI Agent

This project is a simple AI agent that can fetch Bitcoin prices and handle language translation requests while maintaining English as its primary language. 

### Features
- Fetches real-time Bitcoin prices
- Translates user input to English
- Rate-limited API requests to avoid excessive usage
- Cached responses for cryptocurrency prices (5-minute TTL)

### Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/ai_agent.git
    cd ai_agent
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Environment Variables Setup:**

    - Create a `.env` file with the following content:
    
    ```plaintext
    TOGETHER_API_KEY=your_together_ai_api_key
    CRYPTO_API_KEY=your_crypto_api_key
    ```

4. **Run the Application:**

    ```bash
    python main.py
    ```

### Example Conversations

- **User:** "What's the current
