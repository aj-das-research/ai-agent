from agent import AIAgent
import os
from dotenv import load_dotenv
import warnings

warnings.filterwarnings("ignore")

# Load environment variables from .env file
load_dotenv()

def main():
    agent = AIAgent()
    print("AI Agent: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("AI Agent: Goodbye!")
            break
        response = agent.handle_user_input(user_input)
        print(f"AI Agent: {response}")

if __name__ == "__main__":
    main()
