import pandas as pd
import numpy as np
from lightfm import LightFM
from lightfm.data import Dataset
import joblib

# Load from parquet
df = pd.read_parquet("interactions.parquet")

dataset = Dataset()
dataset.fit(users=df["user_id"].unique(), items=df["post_id"].unique())

(interactions, _) = dataset.build_interactions([
    (row.user_id, row.post_id, row.event_score)
    for row in df.itertuples()
])

model = LightFM(loss="warp")
model.fit(interactions, epochs=10, num_threads=2)

joblib.dump(model, "model.pkl")
joblib.dump(dataset, "dataset.pkl")
