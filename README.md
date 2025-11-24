# LEARNING-CHATBOT
This is a chatbot that learns from your inputs and increases its knowledge base and data acquired. Hence, it is able to provide answers which are more personalised , authentic and unique.


🔷 GENERAL OVERVIEW

The code creates a simple chatbot using Python’s built-in Tkinter GUI library.

The chatbot learns new question–answer pairs from the user.

The chatbot saves its knowledge to a file called memory.json.

The chat history is saved to a file called chat_history.txt.

Chat history is reloaded every time the program starts.

The user interface contains a chat display, a history display, and an input section.

The program is divided into two main classes:

SimpleLearningChatbot

ChatGUI

🔷 PART 1 — SimpleLearningChatbot Class (The Bot Logic)

This class handles how the bot learns and responds.

It loads memory from a JSON file when the program starts.

If the file doesn’t exist, it starts with an empty dictionary.

If the JSON file is corrupted, it safely returns an empty dictionary.

The bot remembers the last question it couldn’t answer.

The respond() method controls all bot behaviors.

If the bot is waiting for an answer, the user’s message becomes the answer.

The bot then stores that new question–answer pair in memory.

After saving, it resets awaiting_question to None.

If the user asks a known question, the bot answers immediately.

If the question is unknown, the bot asks the user to teach it.

The bot never forgets what it learns because memory is saved to a file.

save_memory() writes all learned data back to memory.json.

The chatbot logic stays completely separate from the graphical interface.

🔷 PART 2 — ChatGUI Class (The Graphical User Interface)

This class creates and manages the Tkinter window.

It initializes the bot logic when the GUI starts.

The window title is set as “Learning Chatbot”.

The window size is set to 520×700 pixels.

Grid layout is used to handle resizing of widgets.

Three main rows are defined using grid_rowconfigure().

The first row contains the chat area.

The second row contains the chat history area.

The third row contains the user input section.

Chat area uses a ScrolledText widget to display messages.

Chat display is read-only by disabling text editing.

A label “Chat” is placed above the chat window.

Chat history also uses a ScrolledText widget.

A label “Chat History (Saved)” sits above the history area.

The history display loads previous chat messages at startup.

The bottom frame holds the input box and send button.

The input field is a Tkinter Entry widget.

self.entry.focus() ensures the user can always type immediately.

The Return (Enter) key triggers message sending.

A Send button allows clicking instead of pressing Enter.

When a message is sent, it is displayed in the chat area.

The message is then passed to the chatbot logic.

The bot’s reply is also shown in the chat area.

Both user and bot messages are also written to chat history.

History updates instantly in the history area.

Message areas auto-scroll as new messages appear.

The run() method starts the Tkinter event loop.

The code ensures a responsive layout that scales with the window.

Putting everything together, this program creates a learning chatbot with an expandable GUI and persistent memory.
