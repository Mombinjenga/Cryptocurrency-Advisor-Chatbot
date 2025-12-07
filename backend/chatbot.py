# backend/chatbot.py

import pandas as pd
from backend.dataset_handler import load_dataset, query_dataset  # Placeholder for future dataset functions

# Load dataset when module is imported
# For now, dataset loading is optional; you can replace this later
try:
    crypto_data = load_dataset()  # You will define this in dataset_handler.py
except Exception:
    crypto_data = None


def get_response(user_input: str) -> str:
    """
    Main function to process user input and return chatbot response.
    For now, returns a dummy response. Later, it will query crypto_data.
    """
    user_input = user_input.lower().strip()

    # Example of simple keyword response
    if "price" in user_input:
        return "Bot: I can tell you the price of any crypto once the dataset is connected."
    elif "help" in user_input:
        return "Bot: You can ask me about crypto prices, market trends, and recommendations."
    else:
        return "Bot: Sorry, I didn't understand that. Try asking about crypto prices or trends."


# Optional: additional helper functions for dataset queries
def get_crypto_price(coin_name: str) -> str:
    """
    Example function to query dataset for a specific coin's price.
    """
    if crypto_data is None:
        return "Bot: Dataset not loaded yet."

    coin_row = crypto_data[crypto_data['coin_name'].str.lower() == coin_name.lower()]
    if not coin_row.empty:
        price = coin_row['price'].values[0]
        return f"Bot: The current price of {coin_name} is ${price}"
    else:
        return f"Bot: I couldn't find data for {coin_name}"