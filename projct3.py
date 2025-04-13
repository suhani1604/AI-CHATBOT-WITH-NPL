






import nltk
import random
import string
from nltk.chat.util import Chat, reflections
from nltk.corpus import stopwords

# Download NLTK data if not already present
nltk.download('punkt')
nltk.download('stopwords')

# Define chatbot pairs (pattern, response)
pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["what is your name?", ["I'm your friendly chatbot."]],
    ["how are you?", ["I'm doing great, thanks!", "I'm fine. How about you?"]],
    ["what is nlp?", ["Natural Language Processing (NLP) is a field of AI focused on understanding human language."]],
    ["who created you?", ["I was created by a student during an internship at CodTech!"]],
    ["bye|goodbye", ["Goodbye!", "See you later!", "Bye!"]],
]

# Create and start the chatbot
def chatbot():
    print("Hi! I'm your AI Chatbot. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    chatbot()

