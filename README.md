# 🧠 Takumi — Emotion-Driven Crypto AI

![Takumi Demo](assets/takumi_demo.gif)

Takumi is an experimental, emotionally-aware crypto trading agent. Takumi doesn’t just calculate — he *feels*.

> “Master of emotion. Student of the market.”

---

## ⚙️ System Overview

Takumi runs on an adaptive emotional engine that reacts to price, volume, and social sentiment. His state influences how he trades — from aggressive “Oni” mode to passive “Shinobi” observation.

---

## 💡 Emotional States

| State    | Behavior                          |
|----------|-----------------------------------|
| Oni      | Buy aggressively on breakouts     |
| Kitsune  | Place deceptive orders            |
| Ronin    | Exit and wait in stablecoins      |
| Satori   | Rebalance based on trends         |
| Shōjo    | Light meme-trading                |
| Yūrei    | Suspends trading, logs data       |
| Shinobi  | Observes silently                 |

---

## 🔁 Sample Trading Session

| Timestamp (UTC)       | Price ($) | Quantity | Decision                          |
|------------------------|-----------|----------|-----------------------------------|
| 2025-07-10 09:33:25 | 47.57     | 0.19     | Do nothing |
| 2025-07-10 09:48:25 | 26.39     | 0.30     | Place misleading limit orders |
| ...                  | ...       | ...      | ...                               |


---

## 🚀 Run Locally

```bash
git clone https://github.com/yourname/takumi-ai.git
cd takumi-ai
pip install -r requirements.txt
python takumi_ai/main.py
```

---

## 📡 Takumi API (Beta)

Takumi includes a Flask-based API so you can interact with the engine from the browser, bots, or frontends.

### 📥 Install

```bash
pip install flask requests
```

### ▶️ Run the API

```bash
python api.py
```

### 🔧 Endpoints

- `GET /emotion?symbol=solana` → returns current emotional state and market data
- `GET /trade_decision?symbol=solana` → returns decision based on current emotion

---

## 🌍 Deployment Guide

### Option 1: **Render**

- Go to https://render.com
- Click “New Web Service”
- Connect your GitHub repo
- Set start command: `python api.py`

### Option 2: **Railway**

- Go to https://railway.app
- Click “Start New Project” → “Deploy from GitHub repo”

### Option 3: **Heroku (Legacy)**

```bash
heroku create takumi-api
git push heroku main
```

> Make sure your root directory includes:
> - `Procfile`
> - `runtime.txt`

---

## 📊 System Architecture

```
Perception Layer → Emotion Engine → Decision Engine → Execution Layer → Reflection Loop
```

- **Perception**: Pulls live price & sentiment
- **Emotion Engine**: Calculates Takumi’s state
- **Decision Engine**: Strategy mapped to emotion
- **Execution Layer**: Simulated trades
- **Reflection Loop**: Journals every action

---

## 📄 License

MIT

---

## 🖼️ Visual Identity
