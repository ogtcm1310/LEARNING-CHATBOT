import tkinter as tk
from tkinter import scrolledtext
import json
import os


class SimpleLearningChatbot:
    def __init__(self, memory_file="memory.json"):
        self.memory_file = memory_file
        self.memory = self.load_memory()
        self.awaiting_question = None

    def load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r") as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_memory(self):
        with open(self.memory_file, "w") as f:
            json.dump(self.memory, f, indent=4)

    def respond(self, message):
        message = message.strip()

        if self.awaiting_question:
            self.memory[self.awaiting_question] = message
            self.save_memory()
            taught = self.awaiting_question
            self.awaiting_question = None
            return f"Thanks! I will remember the answer to: \"{taught}\""

        if message in self.memory:
            return self.memory[message]

        self.awaiting_question = message
        return "I don't know this question. What should I answer?"


class ChatGUI:
    def __init__(self):
        self.bot = SimpleLearningChatbot()

        self.window = tk.Tk()
        self.window.title("Learning Chatbot")
        self.window.geometry("520x700")

        # REAL FIX: ensure resizing works properly
        self.window.grid_rowconfigure(0, weight=3)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_rowconfigure(2, weight=0)
        self.window.grid_columnconfigure(0, weight=1)

        # CHAT AREA
        tk.Label(self.window, text="Chat", font=("Arial", 14, "bold")).grid(row=0, column=0, sticky="nw", padx=10)

        self.chat_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, font=("Arial", 13))
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.grid(row=0, column=0, sticky="nsew", padx=10, pady=(30, 10))

        # HISTORY AREA
        tk.Label(self.window, text="Chat History (Saved)", font=("Arial", 14, "bold")).grid(row=1, column=0, sticky="nw", padx=10)

        self.history_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, font=("Arial", 12), height=8)
        self.history_area.config(state=tk.DISABLED)
        self.history_area.grid(row=1, column=0, sticky="nsew", padx=10, pady=(30, 10))

        self.load_history()

        # INPUT FRAME
        bottom = tk.Frame(self.window)
        bottom.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
        bottom.grid_columnconfigure(0, weight=1)

        self.entry = tk.Entry(bottom, font=("Arial", 14))
        self.entry.grid(row=0, column=0, sticky="ew")
        self.entry.focus()  # FIX: makes typing always work
        self.entry.bind("<Return>", self.send_message)

        send_btn = tk.Button(bottom, text="Send", font=("Arial", 12, "bold"), command=self.send_message)
        send_btn.grid(row=0, column=1, padx=10)


    def send_message(self, event=None):
        user_msg = self.entry.get().strip()
        if not user_msg:
            return

        self.entry.delete(0, tk.END)
        self.add_chat("You", user_msg)

        bot_reply = self.bot.respond(user_msg)
        self.add_chat("Bot", bot_reply)

        self.save_history("You", user_msg)
        self.save_history("Bot", bot_reply)


    def add_chat(self, sender, msg):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"{sender}: {msg}\n\n")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)

    def save_history(self, sender, message):
        with open("chat_history.txt", "a", encoding="utf-8") as f:
            f.write(f"{sender}: {message}\n")

        self.history_area.config(state=tk.NORMAL)
        self.history_area.insert(tk.END, f"{sender}: {message}\n")
        self.history_area.config(state=tk.DISABLED)
        self.history_area.see(tk.END)

    def load_history(self):
        if os.path.exists("chat_history.txt"):
            with open("chat_history.txt", "r", encoding="utf-8") as f:
                history = f.read()
                self.history_area.config(state=tk.NORMAL)
                self.history_area.insert(tk.END, history)
                self.history_area.config(state=tk.DISABLED)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    ChatGUI().run()
