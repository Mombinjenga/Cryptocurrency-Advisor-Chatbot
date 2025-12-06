# frontend/app.py

import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
from PIL import Image, ImageTk  # For displaying bot icon

# Placeholder function for chatbot response
# Later, replace this with a call to backend/chatbot.py
def get_bot_response(user_input):
    return f"Bot: I’ll answer '{user_input}' from the dataset soon!"

# Function to send user message
def send_message():
    user_msg = user_input.get()  # Get text from input box
    if user_msg.strip() != "":   # Ignore empty messages
        # Show user message with timestamp
        timestamp = datetime.now().strftime("%H:%M")
        chat_area.config(state='normal')  # Enable editing
        chat_area.insert(tk.END, f"You ({timestamp}): {user_msg}\n", "user")
        
        # Get bot response
        bot_msg = get_bot_response(user_msg)
        chat_area.insert(tk.END, f"{bot_msg}\n\n", "bot")
        
        chat_area.config(state='disabled')  # Disable editing
        chat_area.yview(tk.END)  # Scroll to the latest message
        
        # Clear input box
        user_input.delete(0, tk.END)

# Initialize main window
root = tk.Tk()
root.title("Crypto Advisor Chatbot")
root.geometry("500x600")

# Chat area (scrollable)
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Arial", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Tag configurations for different colors
chat_area.tag_configure("user", foreground="blue")  # User messages in blue
chat_area.tag_configure("bot", foreground="green")  # Bot messages in green

# User input box
user_input = tk.Entry(root, width=60, font=("Arial", 12))
user_input.pack(padx=10, pady=(0,10), side=tk.LEFT, expand=True, fill=tk.X)
user_input.bind("<Return>", lambda event: send_message())  # Press Enter to send

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=(0,10), side=tk.RIGHT)

# Optional: display bot icon
try:
    bot_img = Image.open("frontend/assets/bot_icon.png")
    bot_img = bot_img.resize((30, 30))  # Resize icon
    bot_photo = ImageTk.PhotoImage(bot_img)
    bot_label = tk.Label(root, image=bot_photo)
    bot_label.pack(padx=5, pady=(0,5), side=tk.LEFT)
except Exception as e:
    print("Bot icon not found or PIL not installed:", e)

# Run the application
root.mainloop()