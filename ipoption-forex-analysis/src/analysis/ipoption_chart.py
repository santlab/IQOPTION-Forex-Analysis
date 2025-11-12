import matplotlib.pyplot as plt
import pandas as pd

def plot_ipoption_chart(data, title='IPOPTION Chart', xlabel='Time', ylabel='Price'):
    plt.figure(figsize=(12, 6))
    plt.plot(data['time'], data['price'], label='Price', color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.legend()
    plt.show()

def visualize_signals(data, signals):
    plt.figure(figsize=(12, 6))
    plt.plot(data['time'], data['price'], label='Price', color='blue')
    plt.scatter(data['time'][signals == 1], data['price'][signals == 1], label='Buy Signal', marker='^', color='green')
    plt.scatter(data['time'][signals == -1], data['price'][signals == -1], label='Sell Signal', marker='v', color='red')
    plt.title('IPOPTION Chart with Trading Signals')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.grid()
    plt.legend()
    plt.show()