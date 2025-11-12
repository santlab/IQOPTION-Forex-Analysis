class PerformanceEvaluator:
    def __init__(self, signals):
        self.signals = signals

    def calculate_win_rate(self):
        total_signals = len(self.signals)
        if total_signals == 0:
            return 0
        winning_signals = sum(1 for signal in self.signals if signal['result'] == 'win')
        return winning_signals / total_signals

    def calculate_return_on_investment(self):
        total_return = sum(signal['return'] for signal in self.signals)
        total_investment = sum(signal['investment'] for signal in self.signals)
        if total_investment == 0:
            return 0
        return total_return / total_investment

    def evaluate_performance(self):
        win_rate = self.calculate_win_rate()
        roi = self.calculate_return_on_investment()
        return {
            'win_rate': win_rate,
            'return_on_investment': roi
        }