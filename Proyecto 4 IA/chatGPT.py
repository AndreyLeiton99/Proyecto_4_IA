import openai
import time
# OpenAI charges you for the prompt and the output text at a rate of $0.002/1000 tokens
# which is roughly 750 words.

# https://platform.openai.com/account/billing/overview 

# Formula para saber el costo por cantidad de pruebas esperadas 
# Costo =  (0,002/1000) * 100 * Cantidad de pruebas con 20 palabras 

# SUGERENCIAS:

# Chats, historial con el nombre/titulo de chats o algun identificador del chat
# Interfaz grafica?
# 

class ChatGPT:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        openai.api_key = api_key
        self.model = model
        self.chat_history = []

    def prompt_user(self):
        user_input = input("You: ")
        return user_input

    def add_user_message(self, message):
        self.chat_history.append({"role": "user", "content": message})

    def generate_response(self):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.chat_history,
            max_tokens=150,
        )

        return response['choices'][0]['message']['content'] if 'choices' in response and response['choices'] else ''

    def chat_loop(self):
        while True:
            user_input = self.prompt_user()

            if user_input.lower() == "exit":
                break

            self.add_user_message(user_input)
            assistant_reply = self.generate_response()

            while not assistant_reply:
                # Espera a que el modelo genere una respuesta, para que siempre pueda mostrar algo.
                time.sleep(1)
                assistant_reply = self.generate_response()

            print(f"GPT: {assistant_reply}")
            self.add_user_message(assistant_reply)