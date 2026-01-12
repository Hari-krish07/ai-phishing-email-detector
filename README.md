# 🛡️ AI Phishing Email Detector
A Machine Learning–based phishing email detection system that classifies emails as Safe or Phishing using Natural Language Processing (NLP) and Logistic Regression.
The project includes a live web interface built with Streamlit and is fully deployed online.

👉 [Click here to try the app](https://ai-phishing-email-detector-egnzxheou47l4znecn95n4.streamlit.app/)
(Paste any email content to instantly check if it is phishing or safe.)

##  Project Overview
Phishing emails are one of the most common attack vectors used in social engineering attacks.
This project aims to automatically detect phishing emails by analyzing email text using machine learning techniques.
The system:
- Learns patterns from real phishing and legitimate emails
- Converts text into numerical features using TF-IDF
- Uses Logistic Regression for classification
- Provides predictions with confidence scores
- Offers a web-based UI for easy testing

## 🎯 Key Features
Detects phishing vs safe emails  
High accuracy (96.24%)  
High phishing recall (97%) — important for security use cases  
Confidence score for each prediction  
Clean and professional Streamlit UI  
Deployed and accessible via browser  

##  How It Works (Pipeline)
### Dataset
Trained on 18,000+ emails  
Labels: Safe Email, Phishing Email  

### Text Preprocessing
Lowercasing  
Removing special characters  
Tokenization  
Stopword removal  
Cleaning noisy text  

### Feature Extraction
TF-IDF Vectorization  
Converts email text into numerical features  

### Model Training
Logistic Regression (final model)  
Naive Bayes used for comparison  
Logistic Regression selected due to better phishing recall  

### Prediction
New email text → TF-IDF → ML model → classification  
Output: Safe / Phishing + confidence  

## 📊 Model Performance
**Metric** | **Value**
--- | ---
Accuracy | 96.24%
Phishing Recall | 97%
Safe Precision | 98%

High recall for phishing ensures fewer malicious emails are missed — critical in SOC environments.

## Web Interface (Streamlit)
The streamlit UI allows users to:
- Paste full email content
- Click Analyze Email
- View prediction result
- See confidence score
- Understand model decision clearly

Designed to resemble a SOC internal security tool, not a toy demo.

## Tech Stack
- **Programming Language**: Python
- **ML / NLP**: scikit-learn, TF-IDF
- **Data Handling**: pandas
- **Model Persistence**: joblib
- **Web UI**: Streamlit
- **Deployment**: Streamlit Community Cloud
- **Version Control**: Git & GitHub

## 📂 Project Structure

ai-phishing-email-detector/
│
├── app.py # Streamlit web app 
├── requirements.txt # Project dependencies
├── README.md # Project documentation
│
├── data/
│ └── cleaned_phishing.csv # 18K cleaned email dataset
│
├── models/
│ ├── phishing_model.joblib # 96.24% Logistic Regression model
│ └── vectorizer.joblib # TF-IDF vectorizer
│
├── src/
│ ├── preprocess_data.py # Data cleaning pipeline
│ ├── feature_extraction.py # TF-IDF feature extraction
│ ├── train_model.py # Model training script
│ └── predict_email.py # CLI prediction script
│
└── .gitignore # Python/git ignores
⚠️ Limitations & Future Improvements

-Some highly sophisticated phishing emails may bypass detection

-Model relies mainly on textual patterns


**Planned improvements:

-Add more real-world phishing samples

-Include rule-based checks (URLs, urgency keywords, formatting)

-Use advanced NLP models (e.g., transformers)

-Integrate email header analysis

In real SOC environments, ML models are combined with rules and continuous retraining.

📌 Use Cases
-SOC analyst phishing triage

-Security awareness training

-Educational ML/NLP project

-Portfolio demonstration for cybersecurity roles

👤 Author
Hari Krishnan
Aspiring SOC Analyst | Cybersecurity 
🔗 GitHub : https://github.com/Hari-krish07

⭐ Final Note
This project demonstrates:

-End-to-end ML pipeline

-Security-focused thinking

-Real-world applicability

-Deployment & production mindset

If you find this useful, feel free to ⭐ the repository.
