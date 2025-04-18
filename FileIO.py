import csv
import os

# transforms a list into a csv file and returns the resulting path
# parameters include the original data-list, the final data-list, the header field,
#   the directory the original data-list was in, and (OPT) an additional header specifier
#   to add to the filename
def list_to_csv(raw_data, data_list, field, output_dir, specific_name=""):
    if specific_name == "":
        header = raw_data[0][field]  # Extract correct header
    else:
        header = specific_name + "_" + raw_data[0][field]
    filename = header.replace(" ", "_").replace("(m/s^2)", "") + '.csv'
    output_path = os.path.join(output_dir, filename)  # Save in same folder as Raw Data.csv

    with open(output_path, 'w', newline='') as csvfile:
        data_writer = csv.writer(csvfile)
        data_writer.writerow([raw_data[0][0], header])  # Write headers
        data_writer.writerows(data_list)

    print(f"File saved: {output_path}")
    return output_path

# transforms a csv file to a list, where it asks the user for a path, checks if it
#   exists, checks if it is in the SolarTelescopeARC directory, then creates the list
def csv_to_list():
    filename = input('State the full path of the file:\n')

    # Ensure that 'SolarTelescopeARC\\' exists in the path
    index = filename.find('SolarTelescopeARC\\')
    if index == -1:
        print("Error: The path does not contain 'SolarTelescopeARC\\'. Please provide a correct path.")
        return

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return

    output_dir = os.path.dirname(filename)  # Get directory of Raw Data.csv

    try:
        with open(filename, newline='') as csvfile:
            raw_data = list(csv.reader(csvfile, delimiter=','))
            print("File successfully loaded!")
        return raw_data, output_dir

    except Exception as e:
        print(f"An error occurred: {e}")

# Concept - main file that refers to io and plotting and datasep, finds file requested based on
#   terminal input info. Could refer to accelanalyzer as well if needed.
