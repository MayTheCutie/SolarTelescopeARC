import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import argparse
import glob
import os

def load_data(file_paths):
    """Load data from multiple Excel or CSV files."""
    all_data = []
    
    for file_path in file_paths:
        print(f"Loading data from {file_path}...")
        if file_path.endswith('.xlsx'):
            xls = pd.ExcelFile(file_path)
            sheet_name = xls.sheet_names[0]  # Assume first sheet contains the data
            df = pd.read_excel(xls, sheet_name=sheet_name)
        elif file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            print(f"Skipping unsupported file: {file_path}")
            continue
        
        df["Source_File"] = os.path.basename(file_path)  # Add filename column for reference
        all_data.append(df)

    if not all_data:
        raise ValueError("No valid data files found.")

    return pd.concat(all_data, ignore_index=True)

def process_data(df):
    """Extract relevant columns and clean data."""
    df = df.rename(columns={df.columns[0]: "Time", df.columns[1]: "Accel_X", df.columns[2]: "Accel_Y", df.columns[3]: "Accel_Z"})
    df = df.dropna()
    return df

def plot_acceleration(df):
    """Plot accelerometer data over time from multiple files."""
    plt.figure(figsize=(10, 5))

    for file in df["Source_File"].unique():
        subset = df[df["Source_File"] == file]
        plt.plot(subset["Time"], subset["Accel_X"], label=f"{file} - X", alpha=0.8)
        plt.plot(subset["Time"], subset["Accel_Y"], label=f"{file} - Y", alpha=0.8)
        plt.plot(subset["Time"], subset["Accel_Z"], label=f"{file} - Z", alpha=0.8)

    plt.xlabel("Time")
    plt.ylabel("Acceleration")
    plt.title("Accelerometer Data from Multiple Files")
    plt.grid()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Process accelerometer data from multiple files.")
    parser.add_argument("files", type=str, nargs='+', help="Path(s) to the .xlsx or .csv file(s) (wildcards not supported).")
    args = parser.parse_args()

    # Expand wildcards manually
    file_paths = []
    for pattern in args.files:
        file_paths.extend(glob.glob(pattern))

    if not file_paths:
        print("No valid files found!")
        return

    print("Loading data...")
    df = load_data(file_paths)
    print("Data loaded successfully!")

    print("Processing data...")
    df = process_data(df)
    print("Data processed successfully!")

    print("Plotting data...")
    plot_acceleration(df)
    print("Script finished running!")

if __name__ == "__main__":
    main()

#USE THIS PROMPT TO PARSE THE DATA
#   python "C:\Users\Mario Gutierrez\Desktop\CS225\AccelerometerAnalyzer.py" "C:\Users\Mario Gutierrez\Desktop\CS225\TelescopeData\*.xlsx"