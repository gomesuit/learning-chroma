# https://docs.trychroma.com/getting-started

import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="my_collection")

collection.add(
    documents=["This is a document", "This is another document"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
)

# collection.add(
#     embeddings=[[1.2, 2.3, 4.5], [6.7, 8.2, 9.2]],
#     documents=["This is a document", "This is another document"],
#     metadatas=[{"source": "my_source"}, {"source": "my_source"}],
#     ids=["id1", "id2"]
# )

results = collection.query(
    query_texts=["This is a query document"],
    n_results=2
)

print(results)
# {'ids': [['id1', 'id2']], 'embeddings': None, 'documents': [['This is a document', 'This is another document']], 'metadatas': [[{'source': 'my_source'}, {'source': 'my_source'}]], 'distances': [[0.7111215591430664, 1.0109777450561523]]}

results = collection.query(
    query_texts=["This is a query another document"],
    n_results=2
)

print(results)
# {'ids': [['id2', 'id1']], 'embeddings': None, 'documents': [['This is another document', 'This is a document']], 'metadatas': [[{'source': 'my_source'}, {'source': 'my_source'}]], 'distances': [[0.7669920921325684, 0.8128967881202698]]}
