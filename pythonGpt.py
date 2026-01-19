 # Install library
# !pip install google-generativeai --upgrade
import google.generativeai as ai  
import time
import os

#API
API_KEY=""
os.environ['API_KEY'] = API_KEY

# API config
ai.configure(api_key=API_KEY)

# Create the model
model = ai.GenerativeModel('gemini-pro')  
chat = model.start_chat()  

while True:
    message = input('You: ')
    if message.lower() == 'bye':
        print('Chatbot: Goodbye!')
        break

    try:
        response = chat.send_message(message) 
        print('Chatbot:', response.text) 
    except ai.errors.InternalServerError as e:
        print(f"Erro no server: {e}")
        print("Tentando de novo em 5 segundos...")
        time.sleep(5)  
