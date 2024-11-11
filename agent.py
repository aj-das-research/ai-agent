import os
from together import Together
from crypto_api import CryptoAPI
from translator import Translator
from conversation_manager import ConversationManager
from rate_limiter import RateLimiter
from cache import Cache
import warnings

warnings.filterwarnings("ignore")

class AIAgent:
    def __init__(self):
        self.together_client = Together(api_key=os.getenv('TOGETHER_API_KEY'))
        self.crypto_api = CryptoAPI()
        self.translator = Translator()
        self.conversation_manager = ConversationManager()
        self.rate_limiter = RateLimiter(max_calls=5, period=60)
        self.cache = Cache()
        self.model = "meta-llama/Llama-Vision-Free"

    def handle_user_input(self, user_input):
        # Check rate limit
        if not self.rate_limiter.allow_request():
            return "Rate limit exceeded. Please wait and try again."

        # Detect language and translate to English if needed
        detected_language = self.translator.detect_language(user_input)
        if detected_language != 'en':
            user_input = self.translator.translate_to_english(user_input)

        # Check for cached response
        cached_response = self.cache.get(user_input)
        if cached_response:
            return cached_response

        # Check for cryptocurrency price request
        if 'bitcoin price' in user_input.lower():
            price = self.crypto_api.get_bitcoin_price()
            if price:
                response = f"The current price of Bitcoin is ${price}."
            else:
                response = "I'm unable to fetch the Bitcoin price at the moment."
        else:
            # Generate response using Together AI
            prompt = self.conversation_manager.construct_prompt(user_input)
            try:
                ai_response = self.together_client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}]
                )
                # Access the content using dot notation
                response = ai_response.choices[0].message.content
            except Exception as e:
                response = f"An error occurred while processing your request: {e}"

        # Maintain conversation context
        self.conversation_manager.update_conversation(user_input, response)
        self.cache.set(user_input, response)
        return response
