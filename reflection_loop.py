class ReflectionLoop:
    def __init__(self):
        self.logs = []

    def reflect(self, emotion_state, decision):
        entry = f"Emotion: {emotion_state}, Decision: {decision}"
        self.logs.append(entry)
        print(f"[JOURNAL] {entry}")
