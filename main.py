from takumi_ai.perception_layer import PerceptionLayer
from takumi_ai.emotion_engine import EmotionEngine
from takumi_ai.decision_engine import DecisionEngine
from takumi_ai.execution_layer import ExecutionLayer
from takumi_ai.reflection_loop import ReflectionLoop

def run_cycle():
    perception = PerceptionLayer()
    emotion = EmotionEngine()
    decision = DecisionEngine()
    execution = ExecutionLayer()
    reflection = ReflectionLoop()

    data = perception.fetch_market_data()
    print(f"Market Data: {data}")

    emotion_state = emotion.evaluate(data)
    action = decision.decide(emotion_state)
    trade = execution.execute(action)
    reflection.reflect(emotion_state, action)

if __name__ == "__main__":
    run_cycle()
