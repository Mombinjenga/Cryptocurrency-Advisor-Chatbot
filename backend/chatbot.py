# Temporary placeholder until we finish the full ML logic in Colab
def get_response(user_input: str) -> str:
    """
    This is a dummy response for testing the Streamlit frontend.
    We'll replace it later with real ML predictions and advice.
    """
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hey there! 👋 I'm your Crypto Advisor. Ask me about Bitcoin price, trends, or predictions!"
    
    elif "price" in user_input or "how much" in user_input:
        return "As of December 16, 2025, Bitcoin is trading around **$92,500**.\n\nShort-term trend: Slightly bearish due to market correction, but strong support at $90K. 🚀"
    
    elif "predict" in user_input or "tomorrow" in user_input:
        return "🔮 **Next-day prediction (placeholder)**:\nClosing price expected around **$93,200** (+0.8%).\nModel confidence: Medium.\n\nVolatility is moderate — good entry point for long-term holders."
    
    elif "bullish" in user_input or "bearish" in user_input:
        return "Current indicators:\n• Price above 21-day MA → **Mildly bullish**\n• RSI at 55 → Not overbought\n• Volatility increasing slightly\n\nOverall: Neutral to bullish short-term."
    
    else:
        return ("I'm still learning! 🤖\n\nFor now, try asking:\n• 'What's the current Bitcoin price?'\n• 'Will it go up tomorrow?'\n• 'Is the trend bullish?'\n\n"
                "Full AI predictions coming soon after we train the model in Colab!")