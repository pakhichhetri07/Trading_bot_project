# 🤖 Binance Futures Testnet Trading Bot

Welcome! This is a simple, beginner-friendly trading bot built in Python.  
It connects to the **Binance Futures Testnet** and allows you to place trades (market, limit, stop-limit, and stop-market) using the command line.

Great for anyone learning algo trading, automation, or working on a crypto-related project.

---

## 🚀 What This Bot Can Do

✅ Connect to **Binance Futures Testnet** (no real money involved)  
✅ Place `BUY` or `SELL` orders  
✅ Support for `MARKET`, `LIMIT`, `STOP_LIMIT`, and `STOP_MARKET` orders  
✅ Accepts all input from the command line (no code editing needed)  
✅ Logs every action to a file for easy debugging  
✅ Clean, modular code in a Python class — ready to extend and reuse

---

## 🧱 Built With

- **Python 3.8+**
- [`python-binance`](https://github.com/sammchardy/python-binance) (official wrapper for Binance API)
- Standard Python libraries: `argparse`, `logging`

---

##  Before You Start

1. Sign up at the [Binance Futures Testnet](https://testnet.binancefuture.com)
2. Go to your profile → Create **API Key** and **Secret**
3. Keep them safe — they give full access to your test account

---

## Disclaimer
This bot is for educational and testing purposes only. It connects to the Binance Futures Testnet, so no real money is used or lost. Use responsibly.

---

## Author
Made by: Pakhi
Email: pakhichettri7@gmail.com" 

---

## 💻 How to Use It

###  Install the required Python package

```bash
pip install python-binance
pip install python-binance

# Place a Market Order
python trading_bot.py --api_key YOUR_API_KEY --api_secret YOUR_API_SECRET --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

# Place a Limit Order
python trading_bot.py --api_key YOUR_API_KEY --api_secret YOUR_API_SECRET --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 65000

# Place a Stop-Market Order
python trading_bot.py --api_key YOUR_API_KEY --api_secret YOUR_API_SECRET --symbol BTCUSDT --side BUY --type STOP_MARKET --stop_price 64000 --quantity 0.01

# Place a Stop-Limit Order
python trading_bot.py --api_key YOUR_API_KEY --api_secret YOUR_API_SECRET --symbol BTCUSDT --side SELL --type STOP_LIMIT --quantity 0.01 --stop_price 64000 --price 64500
'''

## Project Files
.
├── trading_bot.py      # Main script with bot logic
├── trading_bot.log     # Log file for orders and errors
└── README.md           # Project documentation

