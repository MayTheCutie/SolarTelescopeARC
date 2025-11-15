import time
import FileIO as io
import numpy as np
import pandas as pd

# acceleration in x - m/s^2
def sep_accx(raw_data, output_dir):
    data_x = pd.DataFrame()
    for i in range(1, len(raw_data)):  # Skip header row
        temp_x = [raw_data[i][0], raw_data[i][1] * 9.81]
        data_x.append(temp_x)
    return io.list_to_csv(data_x, "Acceleration_in_X", output_dir)

# acceleration in y - m/s^2
def sep_accy(raw_data, output_dir):
    data_y = pd.DataFrame()
    for i in range(1, len(raw_data)):
        temp_y = [raw_data[i][0], raw_data[i][2] * 9.81]
        data_y.append(temp_y)
    return io.list_to_csv(data_y, "Acceleration_in_Y", output_dir)

# acceleration in z - m/s^2
def sep_accz(raw_data, output_dir):
    data_z = pd.DataFrame()
    for i in range(1, len(raw_data)):
        temp_z = [raw_data[i][0], raw_data[i][3] * 9.81]
        data_z.append(temp_z)
    return io.list_to_csv(data_z, "Acceleration_in_Z", output_dir)

# absolute acceleration - m/s^2
# only for use with the data before the 2025-26 academic year
def sep_accabs(raw_data, output_dir):
    data_abs = pd.DataFrame()
    for i in range(1, len(raw_data)):
        temp_abs = [raw_data[i][0], raw_data[i][4]]
        data_abs.append(temp_abs)
    return io.list_to_csv(data_abs, "Absolute_Acceleration", output_dir)

# absolute acceleration - m/s^2
def gen_accabs(raw_data, output_dir):
    data_abs = pd.DataFrame()
    for i in range(1, len(raw_data)):
        x = float(raw_data[i][1])
        y = float(raw_data[i][2])
        z = float(raw_data[i][3])
        temp_abs = [raw_data[i][0], str(np.sqrt(x**2+y**2+z**2))]
        data_abs.append(temp_abs)
    return io.list_to_csv(data_abs, "Absolute_Acceleration", output_dir)

# angular velocity in x - degrees/s
def sep_anvx(raw_data, output_dir):
    data_x = pd.DataFrame()
    for i in range(1, len(raw_data)):
        temp_x = [raw_data[i][0], raw_data[i][4]]
        data_x.append(temp_x)
    return io.list_to_csv(data_x, "Angular_Velocity_in_X", output_dir)

# angular velocity in y - degrees/s
def sep_anvy(raw_data, output_dir):
    data_y = pd.DataFrame()
    for i in range(1, len(raw_data)):
        temp_y = [raw_data[i][0], raw_data[i][5]]
        data_y.append(temp_y)
    return io.list_to_csv(data_y, "Angular_Velocity_in_Y", output_dir)

# angular velocity in z - degrees/s
def sep_anvz(raw_data, output_dir):
    data_z = pd.DataFrame()
    for i in range(1, len(raw_data)):
        temp_z = [raw_data[i][0], raw_data[i][6]]
        data_z.append(temp_z)
    return io.list_to_csv(data_z, "Angular_Velocity_in_Z", output_dir)

# absolute angular velocity - degrees/s
def gen_anvabs(raw_data, output_dir):
    data_abs = pd.DataFrame()
    for i in range(1, len(raw_data)):
        x = float(raw_data[i][4])
        y = float(raw_data[i][5])
        z = float(raw_data[i][6])
        temp_abs = [raw_data[i][0], str(np.sqrt(x**2+y**2+z**2))]
        data_abs.add(temp_abs)
    return io.list_to_csv(data_abs, "Absolute_Angular_Velocity", output_dir)


# angle in x - degrees
def sep_angx(raw_data, output_dir):
    data_x = pd.DataFrame()
    for i in range(1, len(raw_data)):
        temp_x = [raw_data[i][0], raw_data[i][7]]
        data_x.append(temp_x)
    return io.list_to_csv(data_x, "Angular_Velocity_in_X", output_dir)

# angle in y - degrees
def sep_angy(raw_data, output_dir):
    data_y = pd.DataFrame()
    for i in range(1, len(raw_data)):
        temp_y = [raw_data[i][0], raw_data[i][8]]
        data_y.append(temp_y)
    return io.list_to_csv(data_y, "Angular_Velocity_in_Y", output_dir)

# angle in z - degrees
def sep_angz(raw_data, output_dir):
    data_z = pd.DataFrame()
    for i in range(1, len(raw_data)):
        temp_z = [raw_data[i][0], raw_data[i][9]]
        data_z.append(temp_z)
    return io.list_to_csv(data_z, "Angular_Velocity_in_Z", output_dir)


# magnetic field in x - micro teslas
def sep_magx(raw_data, output_dir):
    data_x = pd.DataFrame()
    for i in range(1, len(raw_data)):
        temp_x = [raw_data[i][0], raw_data[i][10]]
        data_x.append(temp_x)
    return io.list_to_csv(data_x, "Magnetic_Field_in_X", output_dir)

# magnetic field in y - micro teslas
def sep_magy(raw_data, output_dir):
    data_y = pd.DataFrame()
    for i in range(1, len(raw_data)):
        temp_y = [raw_data[i][0], raw_data[i][11]]
        data_y.append(temp_y)
    return io.list_to_csv(data_y, "Magnetic_Field_in_Y", output_dir)

# magnetic field in z - micro teslas
def sep_magz(raw_data, output_dir):
    data_z = pd.DataFrame()
    for i in range(1, len(raw_data)):
        temp_z = [raw_data[i][0], raw_data[i][12]]
        data_z.append(temp_z)
    return io.list_to_csv(data_z, "Magnetic_Field_in_Z", output_dir)

# absolute magnetic field - micro teslas
def gen_magabs(raw_data, output_dir):
    data_abs = pd.DataFrame()
    x, y, z = 0, 0 ,0
    for i in range(1, len(raw_data)):
        x = float(raw_data[i][10])
        y = float(raw_data[i][11])
        z = float(raw_data[i][12])
        temp_abs = [raw_data[i][0], str(np.sqrt(x**2+y**2+z**2))]
        data_abs.append(temp_abs)
    return io.list_to_csv(data_abs, "Absolute_Magnetic_Field", output_dir)

# temperature - degrees celsius
def sep_temp(raw_data, output_dir):
    data_t = pd.DataFrame()
    for i in range(1, len(raw_data)):
        temp_t = [raw_data[i][0], raw_data[i][13]]
        data_t.append(temp_t)
    return io.list_to_csv(data_t, "Temperature", output_dir)

# time step fixer
def timestep_fix(time: pd.Series):
    if time[0].is_digit():
        return time
    else:
        # HHMMSS.SSS
        fixed = pd.Series() # total in seconds
        initial_time = 0
        for i in range(1, len(time)):
            time[i].remove(":")
            temp_sec = float((time[i])[4:]) # SS.SSS
            temp_min = float((time[i])[2:4]) * 60 # MM to S
            temp_hr = float((time[i])[:2]) * 3600 # HH to S
            fixed_time = temp_sec + temp_min + temp_hr

            if i == 1:
                initial_time = fixed_time
            else:
                fixed_time -= initial_time

            fixed.add(fixed_time)
        return fixed

def main():
    raw_data, output_dir, filename = io.csv_to_list()
    star_time = time.time()
    try:
        data = raw_data.iloc[:,1]

        time_delta = timestep_fix(raw_data.iloc[:,0])

        raw_data = time_delta.concat(data)

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
