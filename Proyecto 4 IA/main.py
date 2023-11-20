from chatGPT import ChatGPT

if __name__ == "__main__":
    api_key = "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"
    chatbot = ChatGPT(api_key)
    chatbot.chat_loop()