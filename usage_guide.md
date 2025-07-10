# ⚙️ Takumi Usage Guide

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/takumi-ai.git
cd takumi-ai
pip install -r requirements.txt
python takumi_ai/main.py
```

## Configuration

You can modify:
- Emotional thresholds in `emotion_engine.py`
- Simulated trade behavior in `execution_layer.py`
- Data source preferences in `perception_layer.py`

## Next Steps

- Connect to real DEX APIs (e.g., Jupiter or Phoenix on Solana)
- Enable Telegram/Twitter scraping for true social sentiment
- Swap mock strategies for real portfolio logic
