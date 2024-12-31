import ccxt

# Initialize MEXC with your API credentials
exchange = ccxt.mexc({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_API_SECRET',
    'enableRateLimit': True,
})

# Specify the coin, amount, and the address to send to
coin = 'BTC'  # Example: Bitcoin (BTC)
amount = 0.01  # Amount of BTC you want to send
address = 'YOUR_DESTINATION_ADDRESS'  # The address to send the funds to
tag = None  # Some coins (e.g., XRP, EOS) may require a tag or memo, otherwise leave it as None

# Withdrawal request
try:
    withdrawal = exchange.withdraw(
        code=coin,  # The cryptocurrency you want to withdraw
        amount=amount,  # The amount to withdraw
        address=address,  # The destination address
        tag=tag  # Optional, only for certain coins like XRP or EOS
    )
    print("Withdrawal successful:", withdrawal)
except Exception as e:
    print("Error with withdrawal:", str(e))
