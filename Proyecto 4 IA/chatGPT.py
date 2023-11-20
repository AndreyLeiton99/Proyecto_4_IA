import openai
import time
import json


# OpenAI charges you for the prompt and the output text at a rate of $0.002/1000 tokens
# which is roughly 750 words.

# https://platform.openai.com/account/billing/overview 

# Formula para saber el costo por cantidad de pruebas esperadas 
# Costo =  (0,002/1000) * 100 * Cantidad de pruebas con 20 palabras 

# SUGERENCIAS:

# Chats, historial con el nombre/titulo de chats o algun identificador del chat
# Interfaz grafica?

class ChatGPT:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        openai.api_key = api_key
        self.model = model
        self.chat_history = []
        self.user_input = ""

    def prompt_user(self):
        self.user_input = input("You: ")
        return self.user_input

    def add_user_message(self, message):
        self.chat_history.append({"role": "user", "content": message})

    def generate_response(self):
        question = self.user_input

        with open("knowledge_base.json", "r") as f:
            knowledge_base = json.load(f)

        for question_item in knowledge_base["questions"]:
            if question_item["question"] == question:
                return question_item["answer"]

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.chat_history,
            max_tokens=150,
        )
        return response['choices'][0]['message']['content'] if 'choices' in response and response['choices'] else 'Lo sentimos, no podemos contestar a tu pregunta en este momento'

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

# Load the knowledge base from the .txt file
# with open('knowledge_base.txt', 'r') as knowledge_base_file:
#     knowledge_base = knowledge_base_file.read()
#
# # Split the knowledge base into a list of question-answer pairs
# knowledge_base_pairs = knowledge_base.split('\n')
#
# # Search the knowledge base for a match to the user's question
# for pair in knowledge_base_pairs:
#     question, answer = pair.split('?')
#     if question.lower() == user_input.lower():
#         return answer
#
# # If no match is found, use the OpenAI API to generate a response
# return openai.ChatCompletion.create(
#     model=self.model,
#     messages=self.chat_history,
#     max_tokens=150,
# )
