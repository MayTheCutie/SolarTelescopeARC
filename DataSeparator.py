import csv
import os
import time


def sep_x(raw_data, output_dir):
    data_x = []
    for i in range(1, len(raw_data)):  # Skip header row
        temp_x = [raw_data[i][0], raw_data[i][1]]
        data_x.append(temp_x)
    return list_to_csv(raw_data, data_x, 1, output_dir)


def sep_y(raw_data, output_dir):
    data_y = []
    for i in range(1, len(raw_data)):
        temp_y = [raw_data[i][0], raw_data[i][2]]
        data_y.append(temp_y)
    return list_to_csv(raw_data, data_y, 2, output_dir)


def sep_z(raw_data, output_dir):
    data_z = []
    for i in range(1, len(raw_data)):
        temp_z = [raw_data[i][0], raw_data[i][3]]
        data_z.append(temp_z)
    return list_to_csv(raw_data, data_z, 3, output_dir)


def sep_abs(raw_data, output_dir):
    data_abs = []
    for i in range(1, len(raw_data)):
        temp_abs = [raw_data[i][0], raw_data[i][4]]
        data_abs.append(temp_abs)
    return list_to_csv(raw_data, data_abs, 4, output_dir)


def list_to_csv(raw_data, data_list, field, output_dir):
    header = raw_data[0][field]  # Extract correct header
    filename = header.replace(" ", "_").replace("(m/s^2)", "") + '.csv'
    output_path = os.path.join(output_dir, filename)  # Save in same folder as Raw Data.csv

    with open(output_path, 'w', newline='') as csvfile:
        data_writer = csv.writer(csvfile)
        data_writer.writerow([raw_data[0][0], header])  # Write headers
        data_writer.writerows(data_list)

    print(f"File saved: {output_path}")
    return output_path


def main():
    star_time = time.time()
    filename = input('State the full path of the RAW_DATA file:\n')

    # Ensure that 'SolarTelescopeARC\\' exists in the path
    index = filename.find('SolarTelescopeARC\\')
    if index == -1:
        print("Error: The path does not contain 'SolarTelescopeARC\\'. Please provide a correct path.")
        return

    find_path = filename[index:]  # Correct slicing

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return

    output_dir = os.path.dirname(filename)  # Get directory of Raw Data.csv

    try:
        with open(filename, newline='') as csvfile:
            raw_data = list(csv.reader(csvfile, delimiter=','))
            print("File successfully loaded!")

        # Generate and save new CSV files in the same directory
        sep_x(raw_data, output_dir)
        sep_y(raw_data, output_dir)
        sep_z(raw_data, output_dir)
        sep_abs(raw_data, output_dir)

    except Exception as e:
        print(f"An error occurred: {e}")

    print("--- %s seconds ---" % (time.time() - star_time).__round__(2))


if __name__ == "__main__":
    main()
