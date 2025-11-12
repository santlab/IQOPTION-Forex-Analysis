import unittest
from src.signals.signal_generator import generate_signals
from src.signals.performance import evaluate_performance

class TestSignalGeneration(unittest.TestCase):

    def setUp(self):
        # Sample market data for testing
        self.market_data = [
            {'timestamp': '2023-01-01', 'price': 1.1000},
            {'timestamp': '2023-01-02', 'price': 1.1050},
            {'timestamp': '2023-01-03', 'price': 1.1020},
            {'timestamp': '2023-01-04', 'price': 1.1080},
            {'timestamp': '2023-01-05', 'price': 1.1070},
        ]

    def test_generate_signals(self):
        signals = generate_signals(self.market_data)
        self.assertIsInstance(signals, list)
        self.assertGreater(len(signals), 0)

    def test_evaluate_performance(self):
        signals = generate_signals(self.market_data)
        performance_metrics = evaluate_performance(signals)
        self.assertIn('win_rate', performance_metrics)
        self.assertIn('roi', performance_metrics)

if __name__ == '__main__':
    unittest.main()