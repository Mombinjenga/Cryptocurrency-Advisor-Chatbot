# CryptoBuddy Chatbot
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def crypto_advisor(query):
    query = query.lower()  # Convert query to lowercase for easier matching
    print("CryptoBuddy: Thinking... 🤔")

    # Rule 1: Recommend based on sustainability
    if "sustainable" in query or "eco-friendly" in query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return (f"Invest in {recommend}! 🌱 It’s eco-friendly with a sustainability score of "
                f"{crypto_db[recommend]['sustainability_score']*10}/10!\n"
                f"Disclaimer: Crypto is risky—always do your own research!")

    # Rule 2: Recommend based on price trend (rising)
    elif "trending" in query or "rising" in query:
        trending_coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        if trending_coins:
            return (f"Hot picks! 🚀 {', '.join(trending_coins)} are trending up!\n"
                    f"Disclaimer: Crypto is risky—always do your own research!")
        else:
            return "No coins are trending up right now. 😕 Check back later!\nDisclaimer: Crypto is risky—always do your own research!"

    # Rule 3: Recommend for long-term growth (rising trend + high/medium market cap)
    elif "buy" in query or "long-term" in query:
        best_coin = None
        for coin in crypto_db:
            if (crypto_db[coin]["price_trend"] == "rising" and
                crypto_db[coin]["market_cap"] in ["high", "medium"]):
                best_coin = coin
                break
        if best_coin:
            return (f"For long-term growth, go with {best_coin}! 🚀 It’s trending up and has a solid market cap.\n"
                    f"Disclaimer: Crypto is risky—always do your own research!")
        else:
            return "No strong long-term picks right now. 😕 Maybe consider sustainability!\nDisclaimer: Crypto is risky—always do your own research!"

    # Default response for unrecognized queries
    else:
        return ("I’m not sure what you mean. 😅 Try asking about trending coins, sustainable options, or what to buy!\n"
                "Disclaimer: Crypto is risky—always do your own research!")

# Test the chatbot
print("Welcome to CryptoBuddy! Ask me about crypto trends, sustainability, or what to buy! 🚀")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("CryptoBuddy: Catch you later! 🚀")
        break
    response = crypto_advisor(user_input)
    print(response)