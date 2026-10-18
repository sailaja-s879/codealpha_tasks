
def chatbot():
    print("Welcome to Basic Chatbot!")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hi! How can I help you?")
        elif user_input in ["how are you", "how are you?"]:
            print("Bot: I'm fine, thanks!")
        elif user_input in ["bye", "goodbye", "exit"]:
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
