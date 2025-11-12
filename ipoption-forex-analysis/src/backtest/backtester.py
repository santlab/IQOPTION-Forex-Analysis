class Backtester:
    def __init__(self, data, strategy):
        self.data = data
        self.strategy = strategy
        self.results = []

    def run_backtest(self):
        for index in range(len(self.data)):
            if self.strategy.should_enter(index):
                self.enter_trade(index)
            elif self.strategy.should_exit(index):
                self.exit_trade(index)

    def enter_trade(self, index):
        entry_price = self.data[index]['close']
        self.results.append({'entry_index': index, 'entry_price': entry_price})

    def exit_trade(self, index):
        if self.results:
            exit_price = self.data[index]['close']
            trade = self.results[-1]
            trade['exit_index'] = index
            trade['exit_price'] = exit_price
            trade['profit'] = exit_price - trade['entry_price']

    def get_results(self):
        return self.results

    def calculate_performance_metrics(self):
        total_profit = sum(trade['profit'] for trade in self.results if 'profit' in trade)
        total_trades = len(self.results)
        win_trades = len([trade for trade in self.results if trade.get('profit', 0) > 0])
        win_rate = win_trades / total_trades if total_trades > 0 else 0
        return {
            'total_profit': total_profit,
            'total_trades': total_trades,
            'win_rate': win_rate
        }