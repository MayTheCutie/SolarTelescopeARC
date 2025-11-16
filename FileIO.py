import csv
import os
import numpy as np
import pandas as pd


# transforms a list into a csv file and returns the resulting path
# parameters include the original data-list, the final data-list, the header field,
#   the directory the original data-list was in, and (OPT) an additional header specifier
#   to add to the filename
"""
def list_to_csv(raw_data, data_list, field=None, output_dir="SolarTelescopeARC\\", specific_name=""):
    if specific_name == "" and field is not None:
        header = raw_data[0][field]  # Extract correct header
    else:
        header = specific_name
    filename = header.replace(" ", "_").replace("(m/s^2)", "") + '.csv'
    output_path = os.path.join(output_dir, filename)  # Save in same folder as Raw Data.csv

    with open(output_path, 'w', newline='') as csvfile:
        data_writer = csv.writer(csvfile)
        data_writer.writerow([raw_data[0][0], header])  # Write headers
        data_writer.writerows(data_list)

    print(f"File saved: {output_path}")
    return output_path
"""
# list_to_csv
# inputs a pd.DataFrame (2D list), and saves a csv of the DataFrame to the parent directory of the raw_data file
# parameters:
#   df: pd.DataFrame - DataFrame type, the 2D data list you choose to turn into a csv. does not include header, is only data
#   data_type: str - the name of the data from the header - raw_data[0][#]
#   output_dir - the parent directory of the original raw_data file
def list_to_csv(df: pd.DataFrame, data_type: str, output_dir=".\\Data\\misc\\"):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Full path for the output file
    filename = os.path.join(output_dir, data_type + ".csv")

    # Save DataFrame to CSV with header and no index column
    df.to_csv(filename, index=False, header=["Time Lapsed", data_type])

    return filename  # Return the full path for reference


# transforms a csv file to a list, where it asks the user for a relative path of the csv
def csv_to_list(filename=None):
    """
        Load a CSV file, keeping only rows where all values are present (no NaN, None, or empty strings).

        Returns:
            cleaned_data: DataFrame with complete rows
            output_dir: directory of the CSV
            output_filename: name of the CSV
        """
    if filename is None:
        filename = input("State the relative path of the file:\n")

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return None, None, None

    output_dir = os.path.dirname(filename)
    output_filename = os.path.basename(filename)
    print(f"Loading file: {output_filename}")

    try:
        if not output_filename.lower().endswith(".csv"):
            print("Your file does not follow guidelines, applying defaults")
            return None, None, None

        # Define expected columns
        cols = ['Time', 'Acceleration X', 'Acceleration Y', 'Acceleration Z',
                   'Angular velocity X', 'Angular velocity Y', 'Angular velocity Z',
                   'Angle X', 'Angle Y', 'Angle Z',
                   'Magnetic field X', 'Magnetic field Y', 'Magnetic field Z',
                   'Temperature']

        # Load CSV without skipping header
        raw_data = pd.read_csv(filename, skipinitialspace=True, header=None, names=cols)
        raw_data.columns = [str(c).strip() for c in raw_data.columns]

        # Fix Unnamed: 0 if present
        if 'Unnamed 0' in raw_data.columns:
            raw_data = raw_data.rename(columns={'Unnamed 0': 'Time'})

        # Strip whitespace from all cells
        raw_data = raw_data.applymap(lambda x: x.strip() if isinstance(x, str) else x)

        # Keep only rows where all values are present (not empty and not NaN)
        empty_mask = raw_data.applymap(lambda x: x == "" if isinstance(x, str) else False)
        nan_mask = raw_data.isna()
        invalid_mask = empty_mask | nan_mask
        cleaned_data = raw_data[~invalid_mask.any(axis=1)].reset_index(drop=True)

        removed_rows = len(raw_data) - len(cleaned_data)
        if removed_rows > 0:
            print(f"Removed {removed_rows} rows with missing or empty values.")
        else:
            print("All rows are complete. No missing values found.")

        print(f"Columns after cleaning: {list(cleaned_data.columns)}")
        return cleaned_data, output_dir, output_filename

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None

# Concept - main file that refers to io and plotting and datasep, finds file requested based on
#   terminal input info. Could refer to accelanalyzer as well if needed.