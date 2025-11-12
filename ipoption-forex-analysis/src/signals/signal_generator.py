# Signal Generator for Forex Trading

import numpy as np
import pandas as pd

class SignalGenerator:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def generate_signals(self):
        self.data['Signal'] = 0
        self.data['Signal'] = np.where(self.data['Close'] > self.data['Close'].shift(1), 1, 0)
        self.data['Signal'] = np.where(self.data['Close'] < self.data['Close'].shift(1), -1, self.data['Signal'])
        return self.data

    def backtest_signals(self):
        self.data['Returns'] = self.data['Close'].pct_change()
        self.data['Strategy_Returns'] = self.data['Returns'] * self.data['Signal'].shift(1)
        self.data['Cumulative_Strategy_Returns'] = (1 + self.data['Strategy_Returns']).cumprod()
        return self.data[['Cumulative_Strategy_Returns']]

    def performance_metrics(self):
        total_return = self.data['Cumulative_Strategy_Returns'].iloc[-1] - 1
        win_rate = (self.data['Signal'] == 1).sum() / (self.data['Signal'] != 0).sum()
        return {
            'Total Return': total_return,
            'Win Rate': win_rate
        }