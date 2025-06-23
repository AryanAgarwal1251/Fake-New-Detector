# Fake-New-Detector
Fake news detector using hugging face model (fine tuned BERT). Utilizes streamlit for deployment.
Key Features
AI-Powered Detection: Utilizes a pre-trained and fine-tuned BERT model from Hugging Face for superior classification accuracy.
Intuitive User Interface: A Streamlit front-end allows users to easily input news articles and receive instant predictions.
Robust API Backend: FastAPI provides a high-performance, asynchronous API for model inference, ensuring fast and scalable predictions.
Modular Architecture: Clear separation between front-end (Streamlit), back-end (FastAPI), and machine learning model.
Containerized Deployment: Dockerfiles are provided for both the Streamlit app and FastAPI backend, enabling easy local setup and cloud deployment.

Real-time Inference: Get predictions on news articles in real-time.
Technologies Used
Python: The core programming language for the entire application.
Machine Learning & NLP:
Hugging Face Transformers: For accessing and utilizing the BERT model.
PyTorch / TensorFlow (specify which one your BERT model uses): The underlying deep learning framework for the model.
Scikit-learn: For data preprocessing and potentially additional utility functions.
Web Frameworks:
Streamlit: For building the interactive front-end web application.
FastAPI: For creating the RESTful API to serve the ML model.
Uvicorn / Gunicorn: ASGI server to run FastAPI.

#HUGGING FACE MODEL USED: jy46604790/Fake-News-Bert-Detect
