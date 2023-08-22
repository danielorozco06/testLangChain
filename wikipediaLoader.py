from langchain.document_loaders import WikipediaLoader

docs = WikipediaLoader(query="Colombia", lang="es", load_max_docs=2 ).load()
print(len(docs))

print(docs[0].page_content)
