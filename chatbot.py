import random

# random greetings
greetings = ["Hi!", "Hello!", "Hey there!"]

# memory variable
name = ""

def get_response(user_input):
    global name
    user_input = user_input.lower()

    if "hello" in user_input:
        return random.choice(greetings)
    
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great 😄"
    
    elif "your name" in user_input:
        return "I am your AI chatbot."
    
    elif "help" in user_input:
        return "You can ask me basic questions!"

    elif "my name is" in user_input:
        name = user_input.replace("my name is", "").strip()
        return f"Nice to meet you, {name}!"

    elif "what is my name" in user_input:
        if name:
            return f"Your name is {name}"
        else:
            return "I don't know your name yet."
    
    elif "bye" in user_input:
        return "Goodbye 👋"
    
    else:
        return "Sorry, I didn't understand that."

# main loop
print("🤖 AI Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ")
    response = get_response(user)
    print("Bot:", response)

    if "bye" in user.lower():
        break