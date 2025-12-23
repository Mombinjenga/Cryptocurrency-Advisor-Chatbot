# backend/chatbot.py
import joblib
import pandas as pd
import numpy as np
from datetime import datetime

# Load the trained model (adjust path if needed)
model = joblib.load('models/btc_randomforest_model.pkl')

# Latest features template (we'll fill this with current data)
feature_columns = ['open', 'high', 'low', 'close', 'volume', 'market_cap',
                   'close_ratio', 'spread', 'returns', 'log_returns',
                   'ma_7', 'ma_21', 'ma_50', 'momentum_7', 'momentum_14',
                   'volatility_14', 'volatility_30', 'rsi_14']

def get_real_time_features():
    # In future: fetch live data via yfinance or CoinGecko
    # For now: use last known row as placeholder
    # We'll replace this later with live fetch
    latest = {
        'open': 92000, 'high': 93500, 'low': 91500, 'close': 92500,
        'volume': 3.5e10, 'market_cap': 1.8e12,
        'close_ratio': 0.6, 'spread': 2000,
        'returns': 0.01, 'log_returns': 0.01,
        'ma_7': 91000, 'ma_21': 90000, 'ma_50': 88000,
        'momentum_7': 0.03, 'momentum_14': 0.05,
        'volatility_14': 0.04, 'volatility_30': 0.035,
        'rsi_14': 55
    }
    return pd.DataFrame([latest])[feature_columns]

def get_response(user_input: str) -> str:
    user_input = user_input.lower()

    if any(word in user_input for word in ["predict", "tomorrow", "next", "future", "price"]):
        try:
            features = get_real_time_features()
            pred_price = model.predict(features)[0]
            current_price = features['close'].iloc[0]
            change = pred_price - current_price
            pct_change = change / current_price * 100

            direction = "up" if change > 0 else "down"
            confidence = "high" if abs(pct_change) > 2 else "moderate"

            return (
                f"🔮 **Next-day Bitcoin Prediction**\n"
                f"Predicted closing price: **${pred_price:,.0f}**\n"
                f"Change: {'+' if change > 0 else ''}{pct_change:+.2f}% ({direction})\n"
                f"Confidence: {confidence}\n\n"
                f"Based on current price ~${current_price:,.0f} and latest indicators."
            )
        except Exception as e:
            return "Model prediction temporarily unavailable. Try again soon! 🤖"

    elif any(word in user_input for word in ["trend", "bullish", "bearish"]):
        rsi = get_real_time_features()['rsi_14'].iloc[0]
        if rsi > 70:
            trend = "Overbought – possible pullback"
        elif rsi < 30:
            trend = "Oversold – potential bounce"
        else:
            trend = "Neutral"
        return f"Current short-term trend: {trend} (RSI = {rsi:.1f})"

    else:
        return "Ask me to 'predict tomorrow's price' or about the 'trend'! 🚀"