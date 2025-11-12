# CLI for IPOPTION Forex Analysis

import argparse
from src.analysis.ipoption_chart import plot_chart
from src.data.loader import load_market_data
from src.signals.signal_generator import generate_signals

def main():
    parser = argparse.ArgumentParser(description='IPOPTION Forex Analysis CLI')
    parser.add_argument('--symbol', type=str, required=True, help='Currency pair symbol (e.g., EUR/USD)')
    parser.add_argument('--start', type=str, required=True, help='Start date for analysis (YYYY-MM-DD)')
    parser.add_argument('--end', type=str, required=True, help='End date for analysis (YYYY-MM-DD)')
    parser.add_argument('--plot', action='store_true', help='Plot the IPOPTION chart')

    args = parser.parse_args()

    # Load market data
    market_data = load_market_data(args.symbol, args.start, args.end)

    # Generate trading signals
    signals = generate_signals(market_data)

    print(f"Generated signals for {args.symbol} from {args.start} to {args.end}:")
    print(signals)

    # Plot the IPOPTION chart if requested
    if args.plot:
        plot_chart(market_data, signals)

if __name__ == '__main__':
    main()