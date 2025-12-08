import pandas as pd

class CryptoChatbot:
    def __init__(self):
        # Load dataset
        self.data = pd.read_csv("data/crypto_data.csv")

        # Normalize column names for consistency
        self.data.columns = [col.lower().strip() for col in self.data.columns]

        # Filter only BTC, ETH, ADA (if the dataset contains many coins)
        wanted = ["bitcoin", "btc", "ethereum", "eth", "cardano", "ada"]
        self.filtered = self.data[self.data['name'].str.lower().isin(wanted) |
                                  self.data['symbol'].str.lower().isin(wanted)]

    def get_response(self, user_input):
        user_input = user_input.lower()

        # Basic rule-based responses
        if "bitcoin" in user_input or "btc" in user_input:
            return self.get_coin_info("bitcoin")
        
        if "ethereum" in user_input or "eth" in user_input:
            return self.get_coin_info("ethereum")

        if "cardano" in user_input or "ada" in user_input:
            return self.get_coin_info("cardano")

        # fallback
        return "I can help with Bitcoin, Ethereum, and Cardano. Ask me about their trends, sustainability, or long-term performance!"

    def get_coin_info(self, coin):
        # Find the row
        row = self.filtered[self.filtered['name'].str.lower() == coin]
        if row.empty:
            return f"Sorry, I don’t have data for {coin}."

        row = row.iloc[0]  # take first match

        # Example values the dataset might have
        symbol = row.get("symbol", "N/A")
        market_cap = row.get("market_cap", "N/A")
        sustainability = row.get("sustainability", "N/A")
        long_term = row.get("long_term_rating", "N/A")

        return (
            f"{coin.capitalize()} ({symbol}) info:\n"
            f"- Market Cap: {market_cap}\n"
            f"- Sustainability: {sustainability}\n"
            f"- Long-term rating: {long_term}\n"
        )

# For frontend usage:
bot = CryptoChatbot()

def get_response(msg):
    return bot.get_response(msg)
