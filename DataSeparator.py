import time
import FileIO as io
import numpy as np
import pandas as pd

# acceleration in x - m/s^2
def sep_accx(raw_data, output_dir):

    """
    we want to use the first ROW. but because of pandas, the first ROW is labelled as a COLUMN - all COLUMNS of ROW 1

    :param raw_data:
    :param output_dir:
    :return:
    """


    # Select relevant columns
    df_acc_x = raw_data[['Time', 'Acceleration X']].copy()
    print("spot A")
    # Convert Acceleration X to float and multiply by 9.81
    df_acc_x['Acceleration X'] = pd.to_numeric(df_acc_x['Acceleration X'], errors='coerce') * 9.81
    print("spot B")
    # Drop any rows with NaN (from failed conversion)
    df_acc_x = df_acc_x.dropna().reset_index(drop=True)
    print("spot C")
    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_acc_x), "Acceleration_X", output_dir)


# acceleration in y - m/s^2
def sep_accy(raw_data, output_dir):
    # 1. Clean column names
    raw_data.columns = [str(c).strip() for c in raw_data.columns]

    # 2. Convert first two columns to numeric, invalid entries become NaN
    raw_data.iloc[:, 0] = pd.to_numeric(raw_data.iloc[:, 0], errors='coerce')
    raw_data.iloc[:, 1] = pd.to_numeric(raw_data.iloc[:, 1], errors='coerce')

    # 3. Drop rows where either column is NaN
    clean_data = raw_data.dropna(subset=[raw_data.columns[0], raw_data.columns[1]])

    # 4. Multiply second column by 9.81
    clean_data.iloc[:, 1] = clean_data.iloc[:, 1] * 9.81

    # 5. Create the output DataFrame with the two columns
    df_out = clean_data.iloc[:, [0, 1]].reset_index(drop=True)

    # 6. Export to CSV
    return io.list_to_csv(df_out, "Acceleration_in_Y", output_dir)

# acceleration in z - m/s^2
def sep_accz(raw_data, output_dir):
    data_z = []
    for i in range(1, len(raw_data)):
        temp_z = [raw_data[i][0], raw_data[i][3] * 9.81]
        data_z.append(temp_z)
    return io.list_to_csv(pd.DataFrame(data_z), "Acceleration_in_Z", output_dir)

# absolute acceleration - m/s^2
# only for use with the data before the 2025-26 academic year
def sep_accabs(raw_data, output_dir):
    data_abs = []
    for i in range(1, len(raw_data)):
        temp_abs = [raw_data[i][0], raw_data[i][4]]
        data_abs.append(temp_abs)
    return io.list_to_csv(pd.DataFrame(data_abs), "Absolute_Acceleration", output_dir)

# absolute acceleration - m/s^2
def gen_accabs(raw_data, output_dir):
    data_abs = []
    for i in range(1, len(raw_data)):
        x = float(raw_data[i][1])
        y = float(raw_data[i][2])
        z = float(raw_data[i][3])
        temp_abs = [raw_data[i][0], str(np.sqrt(x**2+y**2+z**2))]
        data_abs.append(temp_abs)
    return io.list_to_csv(pd.DataFrame(data_abs), "Absolute_Acceleration", output_dir)

# angular velocity in x - degrees/s
def sep_anvx(raw_data, output_dir):
    data_x = []
    for i in range(1, len(raw_data)):
        temp_x = [raw_data[i][0], raw_data[i][4]]
        data_x.append(temp_x)
    return io.list_to_csv(pd.DataFrame(data_x), "Angular_Velocity_in_X", output_dir)

# angular velocity in y - degrees/s
def sep_anvy(raw_data, output_dir):
    data_y = []
    for i in range(1, len(raw_data)):
        temp_y = [raw_data[i][0], raw_data[i][5]]
        data_y.append(temp_y)
    return io.list_to_csv(pd.DataFrame(data_y), "Angular_Velocity_in_Y", output_dir)

# angular velocity in z - degrees/s
def sep_anvz(raw_data, output_dir):
    data_z = []
    for i in range(1, len(raw_data)):
        temp_z = [raw_data[i][0], raw_data[i][6]]
        data_z.append(temp_z)
    return io.list_to_csv(pd.DataFrame(data_z), "Angular_Velocity_in_Z", output_dir)

# absolute angular velocity - degrees/s
def gen_anvabs(raw_data, output_dir):
    data_abs = []
    for i in range(1, len(raw_data)):
        x = float(raw_data[i][4])
        y = float(raw_data[i][5])
        z = float(raw_data[i][6])
        temp_abs = [raw_data[i][0], str(np.sqrt(x**2+y**2+z**2))]
        data_abs.append(temp_abs)
    return io.list_to_csv(pd.DataFrame(data_abs), "Absolute_Angular_Velocity", output_dir)


# angle in x - degrees
def sep_angx(raw_data, output_dir):
    data_x = []
    for i in range(1, len(raw_data)):
        temp_x = [raw_data[i][0], raw_data[i][7]]
        data_x.append(temp_x)
    return io.list_to_csv(pd.DataFrame(data_x), "Angular_Velocity_in_X", output_dir)

# angle in y - degrees
def sep_angy(raw_data, output_dir):
    data_y = []
    for i in range(1, len(raw_data)):
        temp_y = [raw_data[i][0], raw_data[i][8]]
        data_y.append(temp_y)
    return io.list_to_csv(pd.DataFrame(data_y), "Angular_Velocity_in_Y", output_dir)

# angle in z - degrees
def sep_angz(raw_data, output_dir):
    data_z = []
    for i in range(1, len(raw_data)):
        temp_z = [raw_data[i][0], raw_data[i][9]]
        data_z.append(temp_z)
    return io.list_to_csv(pd.DataFrame(data_z), "Angular_Velocity_in_Z", output_dir)


# magnetic field in x - micro teslas
def sep_magx(raw_data, output_dir):
    data_x = []
    for i in range(1, len(raw_data)):
        temp_x = [raw_data[i][0], raw_data[i][10]]
        data_x.append(temp_x)
    return io.list_to_csv(pd.DataFrame(data_x), "Magnetic_Field_in_X", output_dir)

# magnetic field in y - micro teslas
def sep_magy(raw_data, output_dir):
    data_y = []
    for i in range(1, len(raw_data)):
        temp_y = [raw_data[i][0], raw_data[i][11]]
        data_y.append(temp_y)
    return io.list_to_csv(pd.DataFrame(data_y), "Magnetic_Field_in_Y", output_dir)

# magnetic field in z - micro teslas
def sep_magz(raw_data, output_dir):
    data_z = []
    for i in range(1, len(raw_data)):
        temp_z = [raw_data[i][0], raw_data[i][12]]
        data_z.append(temp_z)
    return io.list_to_csv(pd.DataFrame(data_z), "Magnetic_Field_in_Z", output_dir)

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
    return io.list_to_csv(pd.DataFrame(data_abs), "Absolute_Magnetic_Field", output_dir)

# temperature - degrees celsius
def sep_temp(raw_data, output_dir):
    data_t = []
    for i in range(1, len(raw_data)):
        temp_t = [raw_data[i][0], raw_data[i][13]]
        data_t.append(temp_t)
    return io.list_to_csv(pd.DataFrame(data_t), "Temperature", output_dir)

# time step fixer
def timestep_fix(time: pd.Series):
    if time[0].isdigit():
        return time
    else:
        # HHMMSS.SSS
        fixed = [] # total in seconds
        initial_time = 0
        start = 0
        before_midnight = 0
        for i in range(1, len(time)):
            temp = time[i].replace(':','')
            temp_sec = float(temp[5:]) # SS.SSS
            temp_min = float(temp[3:5]) * 60 # MM to S
            temp_hr = float(temp[:3]) * 3600 # HH to S
            fixed_time = temp_sec + temp_min + temp_hr
            #print(temp, temp_sec, temp_min, temp_hr, fixed_time)

            # at start
            if i == 1:
                initial_time = fixed_time
                start = temp
                #print(temp, temp_sec, temp_min, temp_hr, fixed_time)

            # while temp is between the start time and before the last millisecond of the day
            if float(start) <= float(temp) < 235959.999:
                before_midnight = fixed_time
                fixed_time -= initial_time


            # while temp is before start
            if float(temp) < float(start):
                fixed_time += (before_midnight - initial_time)

            truncated = int(fixed_time * 1000 + 1e-12) / 1000
            #print(truncated)
            fixed.append(f"{truncated:.3f}")
        return pd.Series(fixed)

def main():
    raw_data, output_dir, filename = io.csv_to_list()
    star_time = time.time()
    raw_data = pd.DataFrame(raw_data)
    try:
        data = raw_data.iloc[:,1]

        time_delta = timestep_fix(raw_data.iloc[:,0])

        print("spot 1")
        raw_data = pd.DataFrame([time_delta, data])
        print("spot 2")

        # Generate and save new CSV files in the same directory
        sep_accx(raw_data, output_dir) #@TODO: errors occur in the funcs
                                       # our crude attempt at implementing pandas went poorly :(
        print("spot 3")
        sep_accy(raw_data, output_dir)
        print("spot 4")
        sep_accz(raw_data, output_dir)
        print("spot 5")
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
