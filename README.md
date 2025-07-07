# Stock_Watchlist_V1
A simple Flask-based stock watchlist app that lets you add tickers and view live data like price, change %, high, low, and volume using Yahoo Finance. Uses SQLite with SQLAlchemy to store your list. Lightweight, easy to run, and built for quick local use.
## 🔧 Features

- Add/remove stocks by ticker (e.g., AAPL, TSLA)
- Real-time price, high, low, volume, etc.
- SQLite backend with SQLAlchemy ORM

## 🚀 Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
