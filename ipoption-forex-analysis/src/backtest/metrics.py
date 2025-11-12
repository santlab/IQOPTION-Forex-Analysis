class Metrics:
    def __init__(self, returns):
        self.returns = returns

    def calculate_sharpe_ratio(self, risk_free_rate=0.0):
        excess_returns = self.returns - risk_free_rate
        return excess_returns.mean() / excess_returns.std()

    def calculate_max_drawdown(self):
        cumulative_returns = (1 + self.returns).cumprod()
        peak = cumulative_returns.cummax()
        drawdown = (cumulative_returns - peak) / peak
        return drawdown.min()

    def calculate_volatility(self):
        return self.returns.std()

    def calculate_return(self):
        return self.returns.sum()

    def summary(self):
        return {
            "sharpe_ratio": self.calculate_sharpe_ratio(),
            "max_drawdown": self.calculate_max_drawdown(),
            "volatility": self.calculate_volatility(),
            "total_return": self.calculate_return(),
        }