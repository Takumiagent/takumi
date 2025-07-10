from flask import Flask, request, jsonify
from takumi_ai.perception_layer import PerceptionLayer
from takumi_ai.emotion_engine import EmotionEngine
from takumi_ai.decision_engine import DecisionEngine

app = Flask(__name__)

# Initialize Takumi components
perception = PerceptionLayer()
emotion = EmotionEngine()
decision = DecisionEngine()

@app.route("/emotion", methods=["GET"])
def get_emotion():
    symbol = request.args.get("symbol", default="solana")
    data = perception.fetch_market_data()
    state = emotion.evaluate(data)
    return jsonify({
        "symbol": symbol,
        "emotion": state,
        "price": data.get("price"),
        "change_24h": data.get("change_24h"),
        "volume_24h": data.get("volume_24h")
    })

@app.route("/trade_decision", methods=["GET"])
def get_trade_decision():
    symbol = request.args.get("symbol", default="solana")
    data = perception.fetch_market_data()
    state = emotion.evaluate(data)
    action = decision.decide(state)
    return jsonify({
        "symbol": symbol,
        "emotion": state,
        "decision": action
    })

if __name__ == "__main__":
    app.run(debug=True)
