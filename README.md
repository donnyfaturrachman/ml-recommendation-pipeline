📦 Text Content Recommendation System — ML Pipeline
End-to-end Machine Learning Pipeline for a recommendation system using Scala (ETL) and Python (Model Training & Serving).

📌 Project Overview
This project builds an end-to-end recommendation system for a text-based content platform (like Twitter/X). It covers the full ML lifecycle:

✅ Data ingestion & transformation (Scala + Spark)

✅ Model training & evaluation (Python + LightFM)

✅ API for model inference (FastAPI)

✅ Ready for containerized deployment (Docker, Kubernetes)

🧱 Project Structure
ml-recommendation-pipeline/
├── etl-scala-spark/         # Scala Spark job to read and clean raw data
│   └── ETLJob.scala
├── training-python/         # Python training pipeline using LightFM
│   ├── train_model.py
│   ├── predict.py
│   └── requirements.txt
├── model_registry/          # Stores trained model.pkl and dataset.pkl
├── serving/                 # FastAPI app for serving predictions
│   └── app.py
├── docker/                  # Optional Dockerfiles
│   ├── Dockerfile.etl
│   └── Dockerfile.api
└── README.md

🔁 Workflow
1. ETL (Scala + Spark)
Load event data (clicks, views, comments) from S3 / logical DB

Transform and normalize actions into numerical "interaction score"

Save to Parquet format

2. Training (Python)
Read Parquet using pandas

Fit recommendation model using LightFM (WARP)

Save trained model (model.pkl) and mappings (dataset.pkl)

3. Serving (FastAPI)
Load model + user/item mappings

Provide /recommend/{user_id} API that returns top-N post recommendations

🧪 Example: Training & Serving Locally
Train Model:
cd training-python
python train_model.py

Serve Model:
cd serving
uvicorn app:app --reload --port 8000

Test API:
curl http://localhost:8000/recommend/user_1

🛠️ Tech Stack
Component	Technology
ETL Processing	Scala + Apache Spark
Model Training	Python + LightFM
Model Serving	FastAPI
Storage	S3 / Parquet
Orchestration	Kubernetes (optional)
Model Registry	joblib / MLflow (optional)

🧠 Model Info
Uses LightFM with WARP loss (Weighted Approximate-Rank Pairwise)

Supports hybrid recommendations using both implicit feedback and metadata features (can be extended)

📦 Docker Support (Optional)
You can containerize the pipeline for cloud deployment:

# Build and run serving container
cd docker
docker build -f Dockerfile.api -t rec-api .
docker run -p 8000:8000 rec-api

⚡ To Do (Next Steps)
 Add evaluation metrics (precision@k, recall@k)

 Integrate MLflow for experiment tracking

 Deploy via Kubernetes (e.g. Helm chart)

 Add user/post metadata features

🤝 Contributing
Feel free to fork and adapt for your own recommendation system. PRs and feedback welcome.

📝 License
MIT License.