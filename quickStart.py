from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI(openai_api_key="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")

text = "What would be a good company name for a company that makes colorful socks?"

output = chat_model.predict(text)
print(output)
