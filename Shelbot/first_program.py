import sys
from transformers import pipeline

chatbot = pipeline("text-generation")

print("Olá! Como posso lhe ajudar hoje?")
while 1:
    user_input = input("You: ")
    if user_input.lower() in ["goodbye", "bye"]:
        print("Bye! Thank you :D")
        break
    response = chatbot(user_input)
    bot_responde = response[0]['generated_text'].split("Chatbot")
    print(f"Chatbot: {bot_responde}")