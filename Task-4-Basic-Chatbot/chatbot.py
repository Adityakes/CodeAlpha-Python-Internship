# ==========================================================
# Project Name : Basic Rule-Based Chatbot
# Description  : This chatbot responds to user messages
#                using predefined responses.
#
# Concepts Used:
# - Dictionary
# - Functions
# - Loops
# - Input / Output
# ==========================================================

import random
from datetime import datetime

# ==========================================================
# Dictionary containing chatbot responses
# ==========================================================

chatbot_responses = {

    "hello": [
        "Hello! Nice to meet you.",
        "Hi there! How can I help you?",
        "Hello! Hope you're having a great day."
    ],

    "hi": [
        "Hi!",
        "Hello!",
        "Hey! Nice to see you."
    ],

    "hey": [
        "Hey!",
        "Hello!",
        "Hi! How are you?"
    ],

    "how are you": [
        "I'm doing great! Thanks for asking.",
        "I'm fine. Hope you're doing well too!",
        "Everything is going well!"
    ],

    "what is your name": [
        "My name is Python Chatbot.",
        "You can call me ChatBot."
    ],

    "who created you": [
        "I was created by Aditya using Python."
    ],

    "what can you do": [
        "I can answer simple questions, tell the date, time and chat with you."
    ],

    "thank you": [
        "You're welcome!",
        "Happy to help!",
        "Anytime!"
    ],

    "thanks": [
        "You're welcome!",
        "Glad I could help!"
    ],

    "help": [
        """
Available Commands

- hello
- hi
- hey
- how are you
- what is your name
- who created you
- what can you do
- date
- time
- thank you
- thanks
- joke
- bye
        """
    ],

    "joke": [
        "Why do programmers prefer Python? Because it's easy to understand!",
        "Debugging: Being the detective in a crime movie where you're also the criminal.",
        "Why don't programmers like nature? It has too many bugs."
    ],

    "bye": [
        "Goodbye! Have a wonderful day!",
        "Bye! Take care.",
        "See you again!"
    ]
}


# ==========================================================
# Function : Display Welcome Message
# ==========================================================

def display_welcome():

    print("=" * 60)
    print("            BASIC RULE-BASED CHATBOT")
    print("=" * 60)

    print("\nHello! I am your Python Chatbot.")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit the chatbot.\n")


# ==========================================================
# Function : Return Current Date
# ==========================================================

def get_current_date():

    today = datetime.now()
    return today.strftime("%d-%m-%Y")


# ==========================================================
# Function : Return Current Time
# ==========================================================

def get_current_time():

    current_time = datetime.now()
    return current_time.strftime("%I:%M:%S %p")


# ==========================================================
# Function : Generate Chatbot Response
# ==========================================================

def chatbot_reply(user_message):

    user_message = user_message.lower().strip()

    if user_message == "date":
        return f"Today's Date is {get_current_date()}"

    elif user_message == "time":
        return f"Current Time is {get_current_time()}"

    elif user_message in chatbot_responses:
        return random.choice(chatbot_responses[user_message])

    else:
        return "Sorry! I don't understand that. Type 'help' to see available commands."


# ==========================================================
# Main Function
# ==========================================================

def start_chatbot():

    display_welcome()

    while True:

        user_input = input("You : ")

        response = chatbot_reply(user_input)

        print("Bot :", response)

        if user_input.lower() == "bye":
            print("\nChatbot Closed Successfully.")
            break


# ==========================================================
# Driver Code
# ==========================================================

if __name__ == "__main__":
    start_chatbot()