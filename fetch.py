import yfinance as yf
from datetime import datetime

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    # Handle missing or invalid data gracefully
    price = info.get('regularMarketPrice')
    change = info.get('regularMarketChange')
    change_pct = info.get('regularMarketChangePercent')
    high = info.get('dayHigh')
    low = info.get('dayLow')
    volume = info.get('volume')
    market_time = info.get('regularMarketTime')

    # Convert market_time to readable format if available
    if market_time:
        date_time = datetime.fromtimestamp(market_time).strftime('%Y-%m-%d %H:%M:%S')
    else:
        date_time = "N/A"

    return {
        'ticker': ticker,
        'price': price if price is not None else 0,
        'change': change if change is not None else 0,
        'change_pct': change_pct if change_pct is not None else 0,
        'high': high if high is not None else 0,
        'low': low if low is not None else 0,
        'volume': volume if volume is not None else 0,
        'date_time': date_time
    }
