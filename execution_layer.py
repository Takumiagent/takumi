from datetime import datetime
import random

class ExecutionLayer:
    def __init__(self):
        self.mock_trades = []

    def execute(self, decision):
        timestamp = datetime.utcnow().isoformat()
        trade_result = {
            "timestamp": timestamp,
            "decision": decision,
            "price": round(random.uniform(25, 55), 2),
            "quantity": round(random.uniform(0.1, 2.0), 2),
            "status": "executed"
        }
        self.mock_trades.append(trade_result)
        print(f"[MOCK TRADE] {trade_result}")
        return trade_result
