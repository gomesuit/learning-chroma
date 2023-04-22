# https://docs.trychroma.com/getting-started
import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    # https://github.com/chroma-core/chroma/issues/338
    persist_directory=".chromadb"
))

collection = client.get_or_create_collection(name="save_and_load")

# requiered for the first run
# collection.add(
#     documents=["This is a document", "This is another document"],
#     metadatas=[{"source": "my_source"}, {"source": "my_source"}],
#     ids=["id1", "id2"]
# )

results = collection.query(
    query_texts=["This is a query document"],
    n_results=2
)

print(results)
