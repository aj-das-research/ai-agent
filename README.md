# AI Agent

This project is a simple AI agent that fetches Bitcoin prices and handles language translation requests, maintaining English as its primary communication language.

### Features

- **Real-time Bitcoin Prices:** Retrieves the latest Bitcoin price using the CoinMarketCap API.
- **Language Detection and Translation:** Detects the language of user input and translates it to English using the `langdetect` and `deep_translator` libraries.
- **Rate Limiting:** Implements rate limiting to prevent excessive API usage.
- **Caching:** Caches responses for cryptocurrency prices with a 5-minute Time-To-Live (TTL) to enhance performance.

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/ai_agent.git
   cd ai_agent
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**

   Create a `.env` file in the project root directory with the following content:

   ```plaintext
   TOGETHER_API_KEY=your_together_ai_api_key
   CRYPTO_API_KEY=your_coinmarketcap_api_key
   ```

   Replace `your_together_ai_api_key` and `your_coinmarketcap_api_key` with your actual API keys.

5. **Run the Application:**

   ```bash
   python main.py
   ```

### Example Conversations

- **User:** "What's the current Bitcoin price?"
- **AI Agent:** "The current price of Bitcoin is $34,500."

- **User:** "¿Cuál es el precio actual de Bitcoin?"
- **AI Agent:** "The current price of Bitcoin is $34,500."

- **User:** "Tell me a joke."
- **AI Agent:** "Why don't scientists trust atoms? Because they make up everything!"

### Assumptions and Limitations

- The AI Agent uses the Together AI API for language model responses. Ensure you have a valid API key and sufficient quota.
- Cryptocurrency prices are fetched from the CoinMarketCap API. Obtain a valid API key and be aware of the API's rate limits.
- The agent maintains context within a single session but does not persist conversations across different sessions.
- Language detection is performed using the `langdetect` library, which may not be 100% accurate for all inputs.

### Prompt Engineering Approach

The AI Agent constructs prompts by combining the user's input with relevant context to generate coherent and contextually appropriate responses. This involves:

1. **Identifying User Intent:** Analyzing the user's input to determine the underlying request or question.
2. **Constructing the Prompt:** Formulating a prompt that provides the language model with sufficient context to generate an accurate response.
3. **Incorporating Context:** Maintaining conversation history to ensure responses are relevant to the ongoing dialogue.


