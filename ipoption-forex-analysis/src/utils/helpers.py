def calculate_moving_average(data, window_size):
    """Calculate the moving average of a given data set."""
    if len(data) < window_size:
        return []
    return [sum(data[i:i + window_size]) / window_size for i in range(len(data) - window_size + 1)]

def normalize_data(data):
    """Normalize the data to a range of 0 to 1."""
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def log_message(message):
    """Log a message to the console."""
    print(f"[LOG] {message}")

def save_to_csv(data, filename):
    """Save data to a CSV file."""
    import csv
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def load_from_csv(filename):
    """Load data from a CSV file."""
    import csv
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        return [row for row in reader]