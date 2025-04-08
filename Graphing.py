import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python avg_accel_plot.py <folder_with_csvs>")
        sys.exit(1)

    csv_folder = sys.argv[1]

    # Find all CSV files
    csv_files = glob.glob(os.path.join(csv_folder, '*.csv'))
    if not csv_files:
        print("No CSV files found in the specified folder.")
        sys.exit(1)

    # Define columns to average
    accel_cols = [
        'Linear Acceleration x (m/s^2)',
        'Linear Acceleration y (m/s^2)',
        'Linear Acceleration z (m/s^2)',
        'Absolute acceleration (m/s^2)'
    ]

    # Store averages
    averages = {col: [] for col in accel_cols}

    for file in csv_files:
        try:
            df = pd.read_csv(file)
            for col in accel_cols:
                averages[col].append(df[col].mean())
        except Exception as e:
            print(f"Error reading {file}: {e}")

    # Final averages
    final_averages = {col: sum(vals)/len(vals) for col, vals in averages.items() if vals}

    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(final_averages.keys(), final_averages.values(), color=['red', 'green', 'blue', 'purple'])
    plt.title('Average Acceleration Across CSV Files')
    plt.ylabel('Average Acceleration (m/s²)')
    plt.xticks(rotation=15)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
