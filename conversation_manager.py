class ConversationManager:
    def __init__(self):
        self.conversation_history = []

    def construct_prompt(self, user_input):
        prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\n"
        for entry in self.conversation_history:
            prompt += f"User: {entry['user']}\nAI: {entry['ai']}\n"
        prompt += f"User: {user_input}\nAI:"
        return prompt

    def update_conversation(self, user_input, ai_response):
        self.conversation_history.append({'user': user_input, 'ai': ai_response})
        if len(self.conversation_history) > 10:
            self.conversation_history.pop(0)
