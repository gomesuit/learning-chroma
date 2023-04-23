# https://docs.trychroma.com/usage-guide#querying-a-collection
import os
import chromadb

from chromadb.utils import embedding_functions

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.environ["OPENAI_API_KEY"],
    # https://platform.openai.com/docs/guides/embeddings/embedding-models
    model_name="text-embedding-ada-002",
)

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(
    name="amazon_reviews_100",
    # embedding_function=openai_ef,
)

import pandas as pd

datafile_path = "data/reviews_100.csv"

df = pd.read_csv(datafile_path)

df["Id"] = df["Id"].astype(str)

sample_data = {}

collection.add(
    documents=df["Text"].values.tolist(),
    metadatas=df[["ProductId", "UserId", "Score"]].to_dict(orient="records"),
    ids=df["Id"].values.tolist(),
)

results = collection.query(
    query_texts=["This is a query document"],
    n_results=2,
)

print(results)

results = collection.query(
    query_texts=["delicious"],
    where={"Score": 1},
    n_results=2,
)

print(results)

# https://docs.trychroma.com/usage-guide#using-where-filters
results = collection.query(
    query_texts=["delicious"],
    where_document={"$contains":"candy"},
    n_results=2,
)

print(results)

results = collection.get(
    where={"Score": 3}
)

print(results)

results = collection.get(
    ids=['1']
)

print(results)
