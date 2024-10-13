import sys
from transformers import pipeline

chatbot = pipeline("text-generation")

print("Olá! Como posso lhe ajudar hoje?")
while 1:
    user_input = input("You: ")
    if user_input.lower() in ["tchau", "adeus"]:
        print("Adeus! Continuação de um bom dia :D")
        break
    if user_input.upper() in ["Tchau", "Adeus"]:
        print("Adeus! Continuação de um bom dia :D")
        break
    response = chatbot(user_input)
    print(f"Chatbot: {response}")