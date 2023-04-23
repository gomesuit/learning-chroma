# https://github.com/openai/openai-cookbook/blob/main/examples/Semantic_text_search_using_embeddings.ipynb

import pandas as pd
# import numpy as np

datafile_path = "data/reviews_100.csv"

df = pd.read_csv(datafile_path)
# df["embedding"] = df.embedding.apply(eval).apply(np.array)

print(df.head())

sample_data = {}

for index, row in df.iterrows():
    sample_data[row["Id"]] = {
        "document": row["Text"],
        "metadata": {
            "product_id": row["ProductId"],
            "user_id": row["UserId"],
            "score": row["Score"],
        },
    }
