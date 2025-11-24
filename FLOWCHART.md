THIS IS AN OVERVIEW FLOWCHART OF HOW THE CHATBOT WORKS:

           ┌─────────────────────────────────────┐
           │             Program Starts           │
           └─────────────────────────────────────┘
                          │
                          ▼
       ┌────────────────────────────────────────────┐
       │   Load Chatbot Data (memory.json file)     │
       │     • Load known questions/answers         │
       │     • If file missing → start empty        │
       └────────────────────────────────────────────┘
                          │
                          ▼
        ┌─────────────────────────────────────────┐
        │        Load Chat History File           │
        │            chat_history.txt             │
        └─────────────────────────────────────────┘
                          │
                          ▼
      ┌────────────────────────────────────────────┐
      │            Show Main Tkinter GUI           │
      │  • Chat display (scrollable)               │
      │  • Chat history display                    │
      │  • Text entry box                          │
      │  • Send button                             │
      └────────────────────────────────────────────┘
                          │
                          ▼
      ┌─────────────────────────────────────────┐
      │          User Types a Message           │
      │       (press Enter or click Send)       │
      └─────────────────────────────────────────┘
                          │
                          ▼
      ┌─────────────────────────────────────────┐
      │     Message Added to Chat Window        │
      └─────────────────────────────────────────┘
                          │
                          ▼
   ┌─────────────────────────────────────────────────┐
   │       SimpleLearningChatbot.respond()           │
   │                                                 │
   │  1. Is bot waiting for a missing answer?        │
   │     → Yes → Save user reply as answer          │
   │                                                 │
   │  2. Is message in memory?                       │
   │     → Yes → Return stored answer               │
   │                                                 │
   │  3. Otherwise: unknown question                 │
   │     → Ask user: “What should I answer?”         │
   └─────────────────────────────────────────────────┘
                          │
                          ▼
      ┌─────────────────────────────────────────┐
      │       Bot Response Shown in Chat        │
      └─────────────────────────────────────────┘
                          │
                          ▼
     ┌──────────────────────────────────────────┐
     │     Save both messages to history file   │
     │             chat_history.txt             │
     └──────────────────────────────────────────┘
                          │
                          ▼
      ┌────────────────────────────────────────┐
      │      Wait for next user message        │
      └────────────────────────────────────────┘
                          │
                          ▼
             (Repeats infinitely until exit)
