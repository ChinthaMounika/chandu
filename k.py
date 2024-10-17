import random

# A simple list of motivational quotes and affirmations
quotes = [
    "Believe in yourself! You are capable of great things.",
    "Keep pushing forward, no matter how tough it gets.",
    "Every day is a new opportunity to improve yourself.",
    "You are stronger than you think!",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Believe you can and you're halfway there.",
    "Stay positive, work hard, and make it happen.",
    "Dream it. Wish it. Do it.",
    "Success doesn't come from what you do occasionally, it comes from what you do consistently."
]

# A function to generate a response based on the user's input
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Check for certain keywords to give a related response
    if 'sad' in user_input:
        return "It's okay to feel sad sometimes. Just remember, tough times never last, but tough people do!"
    elif 'stressed' in user_input:
        return "Take a deep breath and relax. You’ve got this!"
    elif 'unmotivated' in user_input or 'lazy' in user_input:
        return "Even the best feel unmotivated sometimes. The important thing is to keep going. Small steps lead to big results!"
    elif 'happy' in user_input or 'good' in user_input:
        return "That's awesome! Keep up the positive energy!"
    elif 'help' in user_input:
        return "I'm here to motivate you! Try saying something like 'I feel sad' or 'I'm stressed'."
    else:
        # Provide a random motivational quote from the list if no specific keywords are detected
        return random.choice(quotes)

# Main chatbot loop
def motivational_chatbot():
    print("Hello! I'm your personal motivational chatbot. How can I help you today?")
    print("(Type 'quit' to exit)")

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit the loop if the user wants to quit
        if user_input.lower() == 'quit':
            print("Chatbot: Stay positive! Goodbye!")
            break
        
        # Get the chatbot's response and print it
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    motivational_chatbot()
