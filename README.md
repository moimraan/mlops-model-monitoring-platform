# MLOps Model Monitoring Platform

End to end MLOps platform for machine learning lifecycle management including model training, experiment tracking, deployment, monitoring, and drift detection.

This project demonstrates production machine learning engineering practices including automated pipelines and model observability.

---

## System Overview

Training Pipeline  
→ Model Registry  
→ Model Deployment API  
→ Prediction Logging  
→ Data Drift Monitoring  

---

## Key Features

Experiment tracking using MLflow  
Model versioning and registry  
Automated training pipeline  
Prediction API for inference  
Data drift detection using Evidently  
Monitoring and evaluation workflows  

---

## Tech Stack

Python  
Scikit-learn  
MLflow  
FastAPI  
Pandas  
Evidently AI  

---

## Project Structure
mlops-model-monitoring-platform
│
├── training
│ ├── train_model.py
│
├── monitoring
│ ├── drift_detection.py
│
├── serving
│ ├── inference_api.py
│
├── pipelines
│ ├── training_pipeline.py
│
└── README.md
