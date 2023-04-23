# https://docs.trychroma.com/usage-guide#querying-a-collection

import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="amazon_reviews_100")

import pandas as pd

datafile_path = "data/reviews_100.csv"

df = pd.read_csv(datafile_path)

df["Id"] = df["Id"].astype(str)

# print(df.head())

sample_data = {}

# for index, row in df.iterrows():
#     sample_data[row["Id"]] = {
#         "document": row["Text"],
#         "metadata": {
#             "product_id": row["ProductId"],
#             "user_id": row["UserId"],
#             "score": row["Score"],
#         },
#     }

collection.add(
    documents=df["Text"].values.tolist(),
    metadatas=df[["ProductId", "UserId", "Score"]].to_dict(orient="records"),
    ids=df["Id"].values.tolist(),
)

# for id, data in sample_data.items():
#     collection.add(
#         documents=data["document"],
#         metadatas=data["metadata"],
#         ids=id
#     )

results = collection.query(
    query_texts=["This is a query document"],
    n_results=2
)

print(results)
