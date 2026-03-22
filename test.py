from rag_pipeline import RAGChatbot

bot = RAGChatbot("test.pdf")

print("Processing PDF...")
bot.load_and_process()

while True:
    query = input("\nAsk something (type exit to quit): ")
    if query.lower() == "exit":
        break

    answer = bot.ask(query)
    print("Answer:", answer)