import tkinter as tk
import random

# chatbot logic
greetings = ["Hi!", "Hello!", "Hey there!"]
name = ""

def get_response(user_input):
    global name
    user_input = user_input.lower()

    if "hello" in user_input:
        return random.choice(greetings)
    
    elif "how are you" in user_input:
        return "I'm doing great 😄"
    
    elif "your name" in user_input:
        return "I am your AI chatbot."
    
    elif "my name is" in user_input:
        name = user_input.replace("my name is", "").strip()
        return f"Nice to meet you, {name}!"
    
    elif "what is my name" in user_input:
        return f"Your name is {name}" if name else "I don't know your name yet."
    
    elif "bye" in user_input:
        return "Goodbye 👋"
    
    else:
        return "Sorry, I didn't understand that."

# send message function
def send_message():
    user_input = entry.get()
    
    if user_input.strip() == "":
        return

    chat_box.insert(tk.END, "You: " + user_input + "\n")
    
    response = get_response(user_input)
    chat_box.insert(tk.END, "Bot: " + response + "\n\n")
    
    entry.delete(0, tk.END)
    chat_box.see(tk.END)  # auto scroll

# window
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("400x500")

# chat area
chat_box = tk.Text(root, bg="#f0f0f0", fg="black", font=("Arial", 12))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# frame for input + button
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# input box
entry = tk.Entry(frame, width=25, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=5)

# send button
send_btn = tk.Button(frame, text="Send", command=send_message)
send_btn.pack(side=tk.LEFT)

# press Enter to send
entry.bind("<Return>", lambda event: send_message())

root.mainloop()