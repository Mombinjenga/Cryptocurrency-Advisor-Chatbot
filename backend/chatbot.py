# backend/chatbot.py
# Core logic for the Crypto Advisor Chatbot
# Returns natural language responses based on user input
# Ready for future ML integration

def get_response(user_input: str) -> str:
    """
    Generates a response to the user's crypto query.
    Currently uses rule-based logic; will be replaced with ML predictions.
    """
    user_input = user_input.lower().strip()

    # Greeting responses
    if any(word in user_input for word in ["hi", "hello", "hey", "greetings"]):
        return (
            "Hey there! 👋 I'm your Crypto Advisor, powered by AI.\n"
            "Ask me anything about Bitcoin: price trends, predictions, volatility, "
            "or market sentiment. What's on your mind?"
        )

    # Current price query
    elif any(word in user_input for word in ["price", "how much", "current", "today", "now"]):
        return (
            "As of December 17, 2025:\n"
            "Bitcoin (BTC) is trading around **$92,500 – $93,000 USD**.\n"
            "Market is in a consolidation phase after recent highs. "
            "Watch the $90K support level – strong institutional buying there."
        )

    # Prediction / tomorrow / future
    elif any(word in user_input for word in ["predict", "tomorrow", "next day", "future", "go up", "go down"]):
        return (
            "🔮 **Next-day price prediction (placeholder model)**:\n"
            "Expected closing price: **$93,800** (+1.4% from today).\n"
            "Confidence: Medium\n"
            "Short-term outlook: Mildly bullish – RSI at 58, price above 21-day MA, "
            "but volatility is rising, so expect swings."
        )

    # Trend / bullish / bearish / sentiment
    elif any(word in user_input for word in ["trend", "bullish", "bearish", "sentiment", "outlook"]):
        return (
            "Current Bitcoin trend analysis:\n"
            "• **Short-term**: Mildly bullish (price above 21-day MA)\n"
            "• **Momentum**: Positive (14-day RSI ~58)\n"
            "• **Volatility**: Increasing – expect larger daily swings\n"
            "• **Overall sentiment**: Neutral to bullish – ETF inflows continue, "
            "but macro risks (rates) are in play."
        )

    # Volatility / risk
    elif any(word in user_input for word in ["volatility", "risk", "swing", "stable"]):
        return (
            "Volatility is currently **elevated** compared to the last 30 days.\n"
            "14-day annualized volatility: ~45%\n"
            "This means bigger daily moves are possible – great for traders, "
            "but be cautious if you're holding long-term."
        )

    # Buy / sell / invest advice
    elif any(word in user_input for word in ["buy", "sell", "invest", "entry", "time"]):
        return (
            "I'm not a financial advisor, but here's data-driven insight:\n"
            "• Current price: ~$92,500\n"
            "• Support: $90K – $91K\n"
            "• Resistance: $95K – $97K\n"
            "If you're long-term bullish on BTC, dips to support zones are often good entry points."
        )

    # Unknown / fallback
    else:
        return (
            "Hmm, I'm still learning the ropes! 🤖\n"
            "Try asking things like:\n"
            "- 'What's the current Bitcoin price?'\n"
            "- 'Will BTC go up tomorrow?'\n"
            "- 'What's the trend right now?'\n"
            "- 'How volatile is the market?'\n"
            "Soon I'll have full AI predictions from real models!"
        )