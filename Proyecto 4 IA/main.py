from chatGPT import ChatGPT

if __name__ == "__main__":
    api_key = "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"
    chatbot = ChatGPT(api_key)
    chatbot.chat_loop()