from typing import List

class TechnicalIndicators:
    def __init__(self, data: List[float]):
        self.data = data

    def moving_average(self, period: int) -> List[float]:
        """Calculate the moving average of the data."""
        if period <= 0:
            raise ValueError("Period must be a positive integer.")
        if period > len(self.data):
            raise ValueError("Period must not be greater than the length of the data.")
        
        return [sum(self.data[i:i + period]) / period for i in range(len(self.data) - period + 1)]

    def rsi(self, period: int) -> List[float]:
        """Calculate the Relative Strength Index (RSI) of the data."""
        if period <= 0:
            raise ValueError("Period must be a positive integer.")
        if period > len(self.data):
            raise ValueError("Period must not be greater than the length of the data.")

        gains = []
        losses = []
        
        for i in range(1, len(self.data)):
            change = self.data[i] - self.data[i - 1]
            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(-change)

        avg_gain = sum(gains[:period]) / period
        avg_loss = sum(losses[:period]) / period

        rsi_values = []
        for i in range(period, len(self.data)):
            gain = gains[i - 1]
            loss = losses[i - 1]

            avg_gain = (avg_gain * (period - 1) + gain) / period
            avg_loss = (avg_loss * (period - 1) + loss) / period

            rs = avg_gain / avg_loss if avg_loss != 0 else 0
            rsi = 100 - (100 / (1 + rs))
            rsi_values.append(rsi)

        return [None] * period + rsi_values  # Prepend None for the initial periods without RSI value