from langchain.chat_models import ChatOpenAI
import os

openai_api_key = os.environ["OPENAI_API_KEY"]
chat_model = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-3.5-turbo")

text = "What would be a good company name for a company that makes colorful socks?"

output = chat_model.predict(text)
print(output)
