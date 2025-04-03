from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot(
    'DynamicBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation'
    ],
    database_uri='sqlite:///database.sqlite3'  # Database to store conversations
)

# Train the chatbot with English corpus data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

print("Welcome to DynamicBot! Type 'exit' to end the conversation.")

# Define a dictionary of patterns and responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I am DynamicBot, your personal assistant.",
    "bye": "Goodbye! Have a great day!",
    "help": "Sure! I can answer your questions or assist you with basic tasks. What do you need help with?",
}

# Chat loop
while True:
    user_input = input("You: ").lower()  # Convert input to lowercase for matching
    if user_input == "exit":
        print("DynamicBot: Goodbye!")
        break

    # Check if the input matches any predefined patterns
    response = responses.get(user_input, "I'm sorry, I don't understand that. Can you rephrase?")
    print(f"DynamicBot: {response}")