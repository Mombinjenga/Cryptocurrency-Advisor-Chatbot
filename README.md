# ₿ Cryptocurrency Advisor Chatbot

An intelligent, AI-powered **web chatbot** that analyzes Bitcoin historical data, predicts next-day price movements, evaluates short-term trends, and provides data-driven insights.

## 📌 Project Overview
The **Cryptocurrency Advisor Chatbot** is an intelligent system that analyzes Bitcoin historical data, predicts next-day price movements, evaluates short-term trends, and generates data-driven insights for users. It combines machine learning, time-series analysis, and a modern **interactive web interface** built with Streamlit.

### Key Features
- Sleek, dark-mode web chat interface with avatars and message bubbles
- Conversational AI advisor for Bitcoin trends and predictions
- Next-day price forecasting (in development)
- Technical indicator analysis and natural language advice
- Fully responsive and easy to run locally

---

## 📊 Dataset Description
The dataset contains daily Bitcoin historical price data, including:

- `date`  
- `open`, `high`, `low`, `close`  
- `volume`  
- `market cap`  
- `close_ratio`  
- `spread`  
- `ranknow`  

It supports:

- Price trend analysis  
- Price prediction  
- Volatility insights  
- Direction forecasting  

(Data processing, feature engineering, and model training are handled in Google Colab.)

---

## 🤖 Machine Learning Tasks (In Development – Google Colab)

### 1️⃣ Bitcoin Price Prediction
Predicts the next-day closing price using **RandomForest** or **LSTM**.

### 2️⃣ Historical Trend Analysis
Computes indicators such as:

- Moving averages  
- Volatility  
- Returns  
- Momentum  
- Spread %  

### 3️⃣ Data-Driven Advice Generation
Outputs insights like:

- “Short-term bullish trend detected.”  
- “Volatility is increasing.”  
- “Neutral movement expected.”

Full ML model integration into the chatbot backend is in progress.

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.9+
- Virtual environment (recommended)

### Setup & Run
```bash
git clone https://github.com/Mombinjenga/Cryptocurrency-Advisor-Chatbot.git
cd Cryptocurrency-Advisor-Chatbot

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py

### Project Structure

Cryptocurrency-Advisor-Chatbot/
├── app.py                        # Main Streamlit web interface
├── backend/
│   └── chatbot.py                # Core response logic (placeholder → full ML soon)
├── CryptoChatbot.ipynb           # Google Colab notebook – dataset loading, exploration, feature engineering, model training & experiments
├── data/                         # (Ignored in Git – data processed in Colab)
├── assets/                       # Optional: images, logos, icons
├── requirements.txt
├── README.md
└── .gitignore