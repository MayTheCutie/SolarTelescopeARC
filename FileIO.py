import csv
import os

# transforms a list into a csv file and returns the resulting path
# parameters include the original data-list, the final data-list, the header field,
#   the directory the original data-list was in, and (OPT) an additional header specifier
#   to add to the filename
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

# transforms a csv file to a list, where it asks the user for a relative path of the csv
def csv_to_list(filename=None):
    if filename is None:
        filename = input('State the full path of the file:\n')

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
            with open(filename, newline='') as csvfile:
                raw_data = list(csv.reader(csvfile, delimiter=','))

                # Null/Empty/None check
                has_nulls = False
                for row_idx, row in enumerate(raw_data):
                    for col_idx, val in enumerate(row):
                        if val is None or val.strip() == "":
                            print(f"Null/empty value found at row {row_idx + 1}, column {col_idx + 1}")
                            has_nulls = True

                if has_nulls:
                    print(
                        "Warning: Null or empty values were found in the data. Please clean or handle them before plotting.")
                else:
                    print("File successfully loaded with no null values!")

                print("File successfully loaded!")
        elif output_filename.lower().endswith(".txt"):
            with open(filename, "r") as txtfile:
                for line in txtfile:
                    raw_data = line.strip().split(',')
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