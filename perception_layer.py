import requests

class PerceptionLayer:
    def __init__(self):
        self.api_url = "https://api.coingecko.com/api/v3/simple/price"

    def fetch_market_data(self):
        try:
            response = requests.get(self.api_url, params={
                "ids": "solana",
                "vs_currencies": "usd",
                "include_24hr_change": "true",
                "include_24hr_vol": "true"
            })
            result = response.json().get("solana", {})
            price = result.get("usd", 0)
            change = result.get("usd_24h_change", 0)
            volume = result.get("usd_24h_vol", 0)
        except Exception as e:
            price = 0
            change = 0
            volume = 0
            print(f"Error fetching market data: {e}")

        sentiment = "bullish" if change > 5 else "bearish" if change < -5 else "neutral"

        return {
            "price": price,
            "change_24h": change,
            "volume_24h": volume,
            "social_sentiment": sentiment,
        }
