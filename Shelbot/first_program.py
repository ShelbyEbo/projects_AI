import sys
from transformers import pipeline

chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

print("Olá! Como posso lhe ajudar hoje?")
while 1:
    user_input = input("You: ")
    if user_input.lower() in ["goodbye", "bye"]:
        print("Bye! Thank you :D")
        break
    response = chatbot(user_input)
    print(f"Chatbot: {response.generated_responses[-1]}")