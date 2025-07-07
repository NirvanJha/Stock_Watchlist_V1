from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Stock
from fetch import fetch_stock_data
import os

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///watchlist.db'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Home Page: Show watchlist and handle ticker addition
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticker = request.form['ticker'].strip().upper()
        if not ticker:
            flash('Ticker cannot be empty.', 'warning')
            return redirect(url_for('index'))
        if not Stock.query.filter_by(ticker=ticker).first():
            new_stock = Stock(ticker=ticker)
            db.session.add(new_stock)
            db.session.commit()
            flash(f'Added {ticker} to watchlist!', 'success')
        else:
            flash(f'{ticker} is already in your watchlist.', 'info')
        return redirect(url_for('index'))

    stocks = []
    for stock in Stock.query.all():
        try:
            data = fetch_stock_data(stock.ticker)
            if data:
                stocks.append(data)
            else:
                flash(f'No data found for {stock.ticker}.', 'error')
        except Exception as e:
            flash(f'Failed to fetch {stock.ticker}: {e}', 'error')
    return render_template('index.html', stocks=stocks)

# Remove Ticker: Use POST for better security
@app.route('/remove/<ticker>', methods=['POST'])
def remove(ticker):
    stock = Stock.query.filter_by(ticker=ticker.upper()).first()
    if stock:
        db.session.delete(stock)
        db.session.commit()
        flash(f'{ticker.upper()} removed from watchlist.', 'success')
    else:
        flash(f'{ticker.upper()} not found in watchlist.', 'error')
    return redirect(url_for('index'))

# Initialize database and run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
