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
    filename = data_type + ".csv"
    header = pd.DataFrame(["Time Lapsed", data_type])

    return header.concat(df).to_csv(filename, index=False)


# transforms a csv file to a list, where it asks the user for a relative path of the csv
def csv_to_list(filename=None):
    if filename is None:
        # Relative Path refers to the main directory, SolarTelescopeARC, as just a period.
        #   .\Data\10_29_2025_midnight_trial\soltel.csv
        # From the main dir, just say where the csv file is that you're looking for, and then that output dir is the
        # same that where your csv file is.
        #   output_dir = "10_29_2025_midnight_trial\\"
        filename = input('State the relative path of the file:\n')

    # using relative paths we dont have to worry about this
    """
    # Ensure that 'SolarTelescopeARC\\' exists in the path
    index = filename.find('SolarTelescopeARC\\')
    if index == -1:
        print("Error: The path does not contain 'SolarTelescopeARC\\'. Please provide a correct path.")
        return None
    """

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return None

    output_dir = os.path.dirname(filename)  # Get directory of Raw Data.csv
    output_filename = filename[filename.rfind('\\') + 1:]

    try:
        if output_filename.lower().endswith(".csv"):

            raw_data = pd.read_csv(filename, header=None)

            # Create a mask of empty/null cells
            # Mask for cells that are None or NaN
            null_mask = raw_data.isna() | raw_data.isnull()  # catches NaN

            # Mask for cells that are empty or whitespace strings
            empty_str_mask = raw_data.apply(lambda x: isinstance(x, str) and x.strip() == "")

            # Combine both masks
            empty_mask = null_mask | empty_str_mask

            if empty_mask.any().any():  # check if any True exists in the DataFrame
                has_nulls = True
                # Find the indices of empty/null cells
                null_positions = empty_mask.stack()[lambda x: x].index  # MultiIndex of (row_idx, col_name)

                for row_idx, col_name in null_positions:
                    col_idx = raw_data.columns.get_loc(col_name)  # get numeric column index
                    print(f"Null/empty value found at row {row_idx + 1}, column {col_idx + 1}")

                print(
                    "Warning: Null or empty values were found in the data. Please clean or handle them before plotting."
                )
            else:
                has_nulls = False
                print("File successfully loaded with no null values!")

            print("File successfully loaded!")
        else:
            raw_data = None
            print("Your file does not follow guidelines, applying defaults")
        #print(raw_data)
        return raw_data, output_dir, output_filename

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None


# Concept - main file that refers to io and plotting and datasep, finds file requested based on
#   terminal input info. Could refer to accelanalyzer as well if needed.