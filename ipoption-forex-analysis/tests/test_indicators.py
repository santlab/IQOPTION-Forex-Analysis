import pytest
from src.analysis.indicators import MovingAverage, RSI

def test_moving_average():
    prices = [1, 2, 3, 4, 5]
    ma = MovingAverage(window=3)
    result = ma.calculate(prices)
    expected = [None, None, 2.0, 3.0, 4.0]  # First two values are None due to window size
    assert result == expected

def test_rsi():
    prices = [44, 48, 43, 42, 45, 47, 46, 49, 50, 48]
    rsi = RSI(window=14)
    result = rsi.calculate(prices)
    expected = [None] * 14  # RSI will not be available until enough data points
    assert result == expected  # Adjust expected based on actual RSI calculation logic

# Add more tests as needed for other indicators and edge cases