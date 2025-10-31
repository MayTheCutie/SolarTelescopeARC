import time
import FileIO as io
import numpy as np

# acceleration in x - m/s^2
def sep_accx(raw_data, output_dir):
    data_x = []
    for i in range(1, len(raw_data)):  # Skip header row
        temp_x = [raw_data[i][0], raw_data[i][1]]
        data_x.append(temp_x)
    return io.list_to_csv(raw_data, data_x, 1, output_dir)

# acceleration in y - m/s^2
def sep_accy(raw_data, output_dir):
    data_y = []
    for i in range(1, len(raw_data)):
        temp_y = [raw_data[i][0], raw_data[i][2]]
        data_y.append(temp_y)
    return io.list_to_csv(raw_data, data_y, 2, output_dir)

# acceleration in z - m/s^2
def sep_accz(raw_data, output_dir):
    data_z = []
    for i in range(1, len(raw_data)):
        temp_z = [raw_data[i][0], raw_data[i][3]]
        data_z.append(temp_z)
    return io.list_to_csv(raw_data, data_z, 3, output_dir)

# absolute acceleration - m/s^2
# only for use with the data before the 2025-26 academic year
def sep_accabs(raw_data, output_dir):
    data_abs = []
    for i in range(1, len(raw_data)):
        temp_abs = [raw_data[i][0], raw_data[i][4]]
        data_abs.append(temp_abs)
    return io.list_to_csv(raw_data, data_abs, 4, output_dir)

# absolute acceleration - m/s^2
def gen_accabs(raw_data, output_dir):
    data_abs = []
    for i in range(1, len(raw_data)):
        x = float(raw_data[i][2])
        y = float(raw_data[i][3])
        z = float(raw_data[i][4])
        temp_abs = [raw_data[i][0], str(np.sqrt(x**2+y**2+z**2))]
        data_abs.append(temp_abs)
    return io.list_to_csv(raw_data, data_abs, 0, output_dir, specific_name="AbsoluteAcceleration")

# angular velocity in x - degrees/s
def sep_anvx(raw_data, output_dir):
    data_x = []
    for i in range(1, len(raw_data)):
        temp_x = [raw_data[i][0], raw_data[i][4]]
        data_x.append(temp_x)
    return io.list_to_csv(raw_data, data_x, 4, output_dir)

# angular velocity in y - degrees/s
def sep_anvy(raw_data, output_dir):
    data_y = []
    for i in range(1, len(raw_data)):
        temp_y = [raw_data[i][0], raw_data[i][5]]
        data_y.append(temp_y)
    return io.list_to_csv(raw_data, data_y, 5, output_dir)

# angular velocity in z - degrees/s
def sep_anvz(raw_data, output_dir):
    data_z = []
    for i in range(1, len(raw_data)):
        temp_z = [raw_data[i][0], raw_data[i][6]]
        data_z.append(temp_z)
    return io.list_to_csv(raw_data, data_z, 6, output_dir)

# angular velocity in z - degrees/s
def gen_anvabs(raw_data, output_dir):
    data_abs = []
    for i in range(1, len(raw_data)):
        x = float(raw_data[i][5])
        y = float(raw_data[i][6])
        z = float(raw_data[i][7])
        temp_abs = [raw_data[i][0], str(np.sqrt(x**2+y**2+z**2))]
        data_abs.append(temp_abs)
    return io.list_to_csv(raw_data, data_abs, 0, output_dir, specific_name="AbsoluteAngularVelocity")

# angle in x - degrees
def sep_angx(raw_data, output_dir):
    data_x = []
    for i in range(1, len(raw_data)):
        temp_x = [raw_data[i][0], raw_data[i][7]]
        data_x.append(temp_x)
    return io.list_to_csv(raw_data, data_x, 7, output_dir)

# angular velocity in y - degrees
def sep_angy(raw_data, output_dir):
    data_y = []
    for i in range(1, len(raw_data)):
        temp_y = [raw_data[i][0], raw_data[i][8]]
        data_y.append(temp_y)
    return io.list_to_csv(raw_data, data_y, 8, output_dir)

# absolute angular velocity - degrees
def sep_angz(raw_data, output_dir):
    data_z = []
    for i in range(1, len(raw_data)):
        temp_z = [raw_data[i][0], raw_data[i][9]]
        data_z.append(temp_z)
    return io.list_to_csv(raw_data, data_z, 9, output_dir)

# magnetic field in x - micro teslas
def sep_magx(raw_data, output_dir):
    data_x = []
    for i in range(1, len(raw_data)):
        temp_x = [raw_data[i][0], raw_data[i][10]]
        data_x.append(temp_x)
    return io.list_to_csv(raw_data, data_x, 10, output_dir)

# magnetic field in y - micro teslas
def sep_magy(raw_data, output_dir):
    data_y = []
    for i in range(1, len(raw_data)):
        temp_y = [raw_data[i][0], raw_data[i][11]]
        data_y.append(temp_y)
    return io.list_to_csv(raw_data, data_y, 11, output_dir)

# magnetic field in z - micro teslas
def sep_magz(raw_data, output_dir):
    data_z = []
    for i in range(1, len(raw_data)):
        temp_z = [raw_data[i][0], raw_data[i][12]]
        data_z.append(temp_z)
    return io.list_to_csv(raw_data, data_z, 12, output_dir)

# absolute magnetic field - micro teslas
def gen_magabs(raw_data, output_dir):
    data_abs = []
    x, y, z = 0, 0 ,0
    for i in range(1, len(raw_data)):
        x = float(raw_data[i][10])
        y = float(raw_data[i][11])
        z = float(raw_data[i][12])
        temp_abs = [raw_data[i][0], str(np.sqrt(x**2+y**2+z**2))]
        data_abs.append(temp_abs)
    return io.list_to_csv(raw_data, data_abs, 0, output_dir, specific_name="AbsoluteMagneticField")

# temperature - degrees celsius
def sep_temp(raw_data, output_dir):
    data_t = []
    for i in range(1, len(raw_data)):
        temp_t = [raw_data[i][0], raw_data[i][13]]
        data_t.append(temp_t)
    return io.list_to_csv(raw_data, data_t, 13, output_dir)


def main():
    raw_data, output_dir, filename = io.csv_to_list()
    star_time = time.time()
    try:

        # Generate and save new CSV files in the same directory
        sep_accx(raw_data, output_dir)
        sep_accy(raw_data, output_dir)
        sep_accz(raw_data, output_dir)
        gen_accabs(raw_data, output_dir)
        sep_anvx(raw_data, output_dir)
        sep_anvy(raw_data, output_dir)
        sep_anvz(raw_data, output_dir)
        gen_anvabs(raw_data, output_dir)
        sep_angx(raw_data, output_dir)
        sep_angy(raw_data, output_dir)
        sep_angz(raw_data, output_dir)
        sep_magx(raw_data, output_dir)
        sep_magy(raw_data, output_dir)
        sep_magz(raw_data, output_dir)
        gen_magabs(raw_data, output_dir)
        sep_temp(raw_data, output_dir)

    except Exception as e:
        print(f"An error occurred: {e}")

    print("--- %s seconds ---" % (time.time() - star_time).__round__(2))


if __name__ == "__main__":
    main()
