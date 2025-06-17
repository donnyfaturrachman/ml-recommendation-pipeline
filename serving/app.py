from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")
dataset = joblib.load("dataset.pkl")

user_id_map, _, item_id_map, _ = dataset.mapping()
reverse_item_map = {v: k for k, v in item_id_map.items()}

@app.get("/recommend/{user_id}")
def recommend(user_id: str):
    if user_id not in user_id_map:
        return {"error": "Unknown user"}
    
    user_index = user_id_map[user_id]
    n_items = len(item_id_map)
    scores = model.predict(user_index, np.arange(n_items))
    top_items = np.argsort(-scores)[:5]
    recommended_post_ids = [reverse_item_map[i] for i in top_items]
    
    return {"user_id": user_id, "recommended_posts": recommended_post_ids}
