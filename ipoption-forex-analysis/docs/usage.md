# Usage Documentation for IPOPTION Forex Analysis

## Overview

The IPOPTION Forex Analysis project provides tools for market analysis and signal generation specifically for Forex trading. This documentation outlines how to use the application effectively.

## Installation

To get started, ensure you have Python installed on your machine. Clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd ipoption-forex-analysis
pip install -r requirements.txt
```

## Running the Application

### Command-Line Interface

The application can be run from the command line using the `cli.py` file. You can access various functionalities by executing:

```bash
python src/cli.py --help
```

This command will display a list of available commands and options.

### Main Entry Point

The main entry point of the application is `main.py`. You can run the analysis process directly by executing:

```bash
python src/main.py
```

## Features

### Data Loading

Market data can be loaded using the data loader. The `loader.py` file handles data fetching from various sources. You can specify the data source in the configuration settings.

### Technical Indicators

The application includes several technical indicators implemented in `indicators.py`. You can use these indicators to analyze market trends and make informed trading decisions.

### Signal Generation

Trading signals are generated based on the analysis of market data. The `signal_generator.py` file contains the logic for generating buy/sell signals based on predefined criteria.

### Performance Evaluation

The performance of generated signals can be evaluated using the `performance.py` file. This module provides metrics such as win rate and return on investment.

### Backtesting

You can backtest your trading strategies using historical data with the backtesting framework implemented in `backtester.py`. This allows you to assess the effectiveness of your strategies before deploying them in live trading.

## Examples

### Generating Signals

To generate trading signals, you can run the following command:

```bash
python src/cli.py generate-signals --data <data-source>
```

Replace `<data-source>` with the path to your market data file.

### Evaluating Performance

To evaluate the performance of your trading signals, use:

```bash
python src/cli.py evaluate-performance --signals <signals-file>
```

Replace `<signals-file>` with the path to your generated signals file.

## Conclusion

This documentation provides a brief overview of how to use the IPOPTION Forex Analysis project. For more detailed information on each module and functionality, please refer to the source code and comments within the files. Happy trading!