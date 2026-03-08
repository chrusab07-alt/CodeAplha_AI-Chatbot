import tkinter as tk
from datetime import datetime
import random

# ---------------- CHATBOT LOGIC ----------------
def get_response(user_input):

    text = " ".join(user_input.lower().split())

    # greetings
    if any(word in text for word in ["hi", "hello", "hey", "salam", "assalamualaikum"]):
        return "Hello! How can I help you?"

    elif "how are you" in text:
        return "I'm doing great. Hope you're having a good day!"

    elif "fine" in text or "good" in text or "great" in text:
        return "That's wonderful to hear! How can I assist you further?"

    elif "your name" in text:
        return "I am a Basic AI Chatbot created using Python."

    elif "who made you" in text or "who created you" in text:
        return "I was created by a Python developer."

    elif "time" in text:
        return "Current time is " + datetime.now().strftime("%H:%M")

    elif "date" in text:
        return "Today's date is " + datetime.now().strftime("%d %B %Y")

    elif "day" in text:
        return "Today is " + datetime.now().strftime("%A")

    elif "weather" in text:
        return "I can't check real weather yet, but I hope it's nice!"

    elif "thank" in text:
        return "You're welcome!"

    elif "python" in text:
        return "Python is a popular programming language used for AI, automation and software."

    elif "programming" in text:
        return "Programming is writing instructions for computers."

    elif "joke" in text:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "Why did the programmer quit his job? Because he didn't get arrays.",
            "Debugging is like being the detective in a crime movie where you are also the murderer.",
            "A SQL query walks into a bar and asks: Can I join you?"
        ]
        return random.choice(jokes)

    elif "what can you do" in text:
        return "I can answer basic questions, tell time, date and jokes."

    elif "help" in text:
        return "Sure.You can ask me about time, date, programming, python or ask for a joke."

    elif "good morning" in text:
        return "Good morning! Have a productive day."

    elif "good afternoon" in text:
        return "Good afternoon! Hope your day is going well."

    elif "good evening" in text:
        return "Good evening! How can I help you?"

    elif "good night" in text:
        return "Good night! Sleep well."

    elif "your purpose" in text:
        return "My purpose is to demonstrate a basic AI chatbot using Python."

    elif "computer" in text:
        return "A computer is an electronic device that processes data."

    elif "ai" in text or "artificial intelligence" in text:
        return "Artificial Intelligence is technology that allows machines to simulate human intelligence."

    elif "machine learning" in text:
        return "Machine Learning is a branch of AI where systems learn from data."

    elif "tell me something" in text  or "fact" in text:
        facts = [
            "The first computer programmer was Ada Lovelace.",
            "Python was created by Guido van Rossum.",
            "Computers work using binary numbers 0 and 1.",
            "Artificial Intelligence is one of the fastest growing technologies."
        ]
        return random.choice(facts)

    

    elif "bye" in text:
        return "Goodbye! Have a great day."
    
    else:
        return "Sorry, I didn't understand that."


# ---------------- SEND MESSAGE ----------------
def send_message(event=None):

    user_text = entry.get().strip()

    if user_text == "":
        entry.delete(0, tk.END)
        return

    entry.delete(0, tk.END)

    add_message(user_text, "user")

    response = get_response(user_text)

    def show_response():
        add_message(response, "bot")

    window.after(500, show_response)


# ---------------- ADD MESSAGE ----------------
def add_message(message, sender):

    msg_frame = tk.Frame(chat_frame, bg="#1e1e1e")

    if sender == "user":
        bubble = tk.Label(
            msg_frame,
            text=message,
            bg="#0078ff",
            fg="white",
            font=("Segoe UI", 11),
            wraplength=300,
            padx=10,
            pady=6
        )
        bubble.pack(anchor="e", padx=10, pady=3)

    else:
        bubble = tk.Label(
            msg_frame,
            text=message,
            bg="#333333",
            fg="white",
            font=("Segoe UI", 11),
            wraplength=300,
            padx=10,
            pady=6
        )
        bubble.pack(anchor="w", padx=10, pady=3)

    msg_frame.pack(fill="x")

    canvas.update_idletasks()
    canvas.yview_moveto(1.0)

    return msg_frame


# ---------------- MAIN WINDOW ----------------
window = tk.Tk()
window.title("Basic AI Chatbot")
window.geometry("500x650")
window.configure(bg="#1e1e1e")


# ---------------- HEADING ----------------
header = tk.Label(
    window,
    text="Basic AI Chatbot",
    bg="#121212",
    fg="white",
    font=("Segoe UI", 18, "bold"),
    pady=10
)
header.pack(fill="x")


# ---------------- CHAT AREA ----------------
chat_container = tk.Frame(window, bg="#1e1e1e")
chat_container.pack(fill="both", expand=True)

canvas = tk.Canvas(chat_container, bg="#1e1e1e", highlightthickness=0)
scrollbar = tk.Scrollbar(chat_container, command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

chat_frame = tk.Frame(canvas, bg="#1e1e1e")

chat_window = canvas.create_window((0, 0), window=chat_frame, anchor="nw")


def configure_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


def configure_canvas_width(event):
    canvas.itemconfig(chat_window, width=event.width)


chat_frame.bind("<Configure>", configure_scroll)
canvas.bind("<Configure>", configure_canvas_width)


# ---------------- INPUT AREA ----------------
input_frame = tk.Frame(window, bg="#2b2b2b")
input_frame.pack(fill="x")

entry = tk.Entry(
    input_frame,
    font=("Segoe UI", 12),
    bg="#3a3a3a",
    fg="white",
    insertbackground="white"
)

entry.pack(side="left", fill="x", expand=True, padx=10, pady=10)
entry.focus()

send_button = tk.Button(
    input_frame,
    text="Send",
    command=send_message,
    bg="#0078ff",
    fg="white",
    font=("Segoe UI", 10),
    padx=15
)

send_button.pack(side="right", padx=10)

entry.bind("<Return>", send_message)


# Welcome message
add_message(
    "Hi! I am basic AI chatbot 🤖. Tell me how can I help you?",
    "bot"
)

window.mainloop()