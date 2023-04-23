# https://docs.trychroma.com/usage-guide#querying-a-collection

import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="my_collection")

sample_data = {
    "id1": {"document": "This is a document", "metadata": {"source": "my_source"}},
    "id2": {"document": "This is another document", "metadata": {"source": "my_source"}},
}

for id, data in sample_data.items():
    collection.add(
        documents=data["document"],
        metadatas=data["metadata"],
        ids=id
    )

results = collection.query(
    query_texts=["This is a query document"],
    n_results=2
)

print(results)
