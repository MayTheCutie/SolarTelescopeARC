import time
import FileIO as io


def sep_x(raw_data, output_dir):
    data_x = []
    for i in range(1, len(raw_data)):  # Skip header row
        temp_x = [raw_data[i][0], raw_data[i][1]]
        data_x.append(temp_x)
    return io.list_to_csv(raw_data, data_x, 1, output_dir)


def sep_y(raw_data, output_dir):
    data_y = []
    for i in range(1, len(raw_data)):
        temp_y = [raw_data[i][0], raw_data[i][2]]
        data_y.append(temp_y)
    return io.list_to_csv(raw_data, data_y, 2, output_dir)


def sep_z(raw_data, output_dir):
    data_z = []
    for i in range(1, len(raw_data)):
        temp_z = [raw_data[i][0], raw_data[i][3]]
        data_z.append(temp_z)
    return io.list_to_csv(raw_data, data_z, 3, output_dir)


def sep_abs(raw_data, output_dir):
    data_abs = []
    for i in range(1, len(raw_data)):
        temp_abs = [raw_data[i][0], raw_data[i][4]]
        data_abs.append(temp_abs)
    return io.list_to_csv(raw_data, data_abs, 4, output_dir)


def main():
    star_time = time.time()
    raw_data, output_dir, filename = io.csv_to_list()
    try:

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
