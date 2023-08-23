"""
This file contains an example usage of the WikipediaLoader class from the langchain package.
It loads the content of the Wikipedia page for "X" in X language and prints it to the console.
"""

from langchain.document_loaders import WikipediaLoader

docs = WikipediaLoader(
    query="Colombia",
    lang="es",
    load_max_docs=1,
).load()

print(docs[0].page_content)
