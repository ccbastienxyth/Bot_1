import openai
import pyttsx3

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.strip()
if __name__ == "__main__":
    engine = pyttsx3.init()
    while True:
        user_input = input("You: ") 
        if user_input .lower() in ["quit", "exit", "bye"]:
            break
        
        response = chat_with_gpt(user_input)
        print("Chatbot:", response) 
        
        engine.say(response)
        engine.runAndWait()