# Takumi API

This is a Flask-based API interface for Takumi, the emotion-driven crypto AI.

## 🧪 Endpoints

- `/emotion?symbol=solana` – Get Takumi's current emotional state
- `/trade_decision?symbol=solana` – Get the trading decision based on emotion

## 🚀 Local Setup

```bash
pip install -r requirements.txt
python api.py
```

## 🌍 Deployment Guide (Render / Railway / Heroku)

### 1. **Render**
- Go to https://render.com
- Click “New Web Service”
- Connect your GitHub repo
- Set start command: `python api.py`

### 2. **Railway**
- Go to https://railway.app
- Click “Start New Project” → “Deploy from GitHub repo`
- Follow the prompts

### 3. **Heroku (Legacy)**
- Install Heroku CLI
- Run:

```bash
heroku create takumi-api
git push heroku main
```

Ensure `Procfile` and `runtime.txt` are in your root directory.

## ✅ Notes
- Requires Python 3.10+
- Easily extendable for dashboards or X bots
