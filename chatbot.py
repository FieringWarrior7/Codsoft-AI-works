import re
from datetime import datetime

def enhanced_chatbot_response(user_input):
    user_input = user_input.lower()

    # Greeting the user
    if re.search(r'\bhello\b|\bhi\b|\bhey\b', user_input):
        return "Hi there! How can I assist you?"

    # Asking the chatbot how are you
    elif re.search(r'\bhow (are|r) (you|u)\b', user_input):
        return "I'm just a bot, but I'm doing well! How about you?"

    # Asking for the chatbot's name
    elif re.search(r'\bwhat(\'s|\s+is) your name\b', user_input):
        return "I'm your friendly chatbot!"

    # Asking the chatbot what it does
    elif re.search(r'\bwhat do you (do|can)\b', user_input):
        return "I try to assist you with your queries and make your day better!"

    # Saying goodbye
    elif re.search(r'\b(bye|goodbye|see you)\b', user_input):
        return "Goodbye! Have a great day!"

    # Gratitude
    elif re.search(r'\b(thank you|thanks)\b', user_input):
        return "You're welcome! Anything else I can help with?"

    # Asking about the chatbot's creation
    elif re.search(r'\bwho (created|made) you\b', user_input):
        return "I was created by a brilliant developer!"

    # Asking about the time
    elif re.search(r'\bwhat time is it\b|\bcurrent time\b|\btime now\b', user_input):
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."

    # Asking about the weather (example response)
    elif re.search(r'\bwhat(\'s|\s+is) the weather like\b|\bcurrent weather\b', user_input):
        return "I'm not connected to a weather service, but you can check the weather online!"

    # Asking general questions
    elif re.search(r'\bhow does\b|\bhow do\b|\bhow can\b', user_input):
        return "That's a great question! Can you provide more details so I can help you better?"

    # Asking about the chatbot's capabilities
    elif re.search(r'\bwhat can you (do|assist with)\b', user_input):
        return "I can chat with you, provide basic information, and help you with simple tasks!"

    # Default response for unrecognized inputs
    return "I'm sorry, I don't understand that. Can you rephrase?"

def chat():
    print("Chatbot: Hi! Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        
        response = enhanced_chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
chat()
