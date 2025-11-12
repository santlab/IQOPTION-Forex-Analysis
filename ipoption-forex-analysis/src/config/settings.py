# Configuration settings for the IPOPTION Forex analysis application

# API settings
API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"

# Data source settings
DATA_SOURCE = "your_data_source_here"

# Analysis settings
TIMEFRAME = "1h"  # Options: "1m", "5m", "15m", "1h", "1d"
INDICATORS = ["SMA", "EMA", "RSI"]  # List of indicators to use

# Signal generation settings
SIGNAL_THRESHOLD = 0.05  # Threshold for generating buy/sell signals

# Backtesting settings
BACKTEST_START_DATE = "2022-01-01"
BACKTEST_END_DATE = "2023-01-01"
INITIAL_CAPITAL = 10000  # Starting capital for backtesting

# Logging settings
LOG_LEVEL = "INFO"  # Options: "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
LOG_FILE = "application.log"  # Log file name