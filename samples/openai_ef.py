# https://docs.trychroma.com/embeddings#openai
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
import os

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.environ["OPENAI_API_KEY"],
    # https://platform.openai.com/docs/guides/embeddings/embedding-models
    model_name="text-embedding-ada-002",
)

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="openai_ef",
    embedding_function=openai_ef,
)

collection.add(
    documents=["This is a document", "This is another document"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
)

results = collection.query(
    query_texts=["This is a query document"],
    n_results=2
)

print(results)
