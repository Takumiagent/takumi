class EmotionEngine:
    def __init__(self):
        self.state = "Shinobi"

    def evaluate(self, data):
        price = data["price"]
        change = data["change_24h"]
        volume = data["volume_24h"]
        sentiment = data["social_sentiment"]

        if change > 8 and volume > 1e9 and sentiment == "bullish":
            self.state = "Oni"
        elif change < -5 and sentiment == "bearish":
            self.state = "Ronin"
        elif abs(change) < 1 and sentiment == "neutral":
            self.state = "Shinobi"
        elif sentiment == "bullish" and volume > 5e8:
            self.state = "Shōjo"
        elif change > 2 and sentiment == "bearish":
            self.state = "Kitsune"
        elif change > 3 and sentiment == "neutral":
            self.state = "Satori"
        else:
            self.state = "Yūrei"

        return self.state
