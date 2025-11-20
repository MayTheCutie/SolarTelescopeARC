import time
import FileIO as io
import numpy as np
import pandas as pd

# acceleration in x - m/s^2
def sep_accx(raw_data, output_dir):

    """
    :param raw_data:
    :param output_dir:
    :return:
    """


    # Select relevant columns
    df_acc_x = raw_data[['Time', 'Acceleration X']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_acc_x['Acceleration X'] = pd.to_numeric(df_acc_x['Acceleration X'], errors='coerce') * 9.81

    # Drop any rows with NaN (from failed conversion)
    df_acc_x = df_acc_x.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_acc_x), "Acceleration_X", output_dir)


# acceleration in y - m/s^2
def sep_accy(raw_data, output_dir):

    """
    :param raw_data:
    :param output_dir:
    :return:
    """

    # Select relevant columns
    df_acc_x = raw_data[['Time', 'Acceleration Y']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_acc_x['Acceleration Y'] = pd.to_numeric(df_acc_x['Acceleration Y'], errors='coerce') * 9.81

    # Drop any rows with NaN (from failed conversion)
    df_acc_x = df_acc_x.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_acc_x), "Acceleration_Y", output_dir)

# acceleration in z - m/s^2
def sep_accz(raw_data, output_dir):
    """
    :param raw_data:
    :param output_dir:
    :return:
    """

    # Select relevant columns
    df_acc_x = raw_data[['Time', 'Acceleration Z']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_acc_x['Acceleration Z'] = pd.to_numeric(df_acc_x['Acceleration Z'], errors='coerce') * 9.81

    # Drop any rows with NaN (from failed conversion)
    df_acc_x = df_acc_x.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_acc_x), "Acceleration_Z", output_dir)

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

    for i in range(len(raw_data)):
        t = raw_data.iloc[i, raw_data.columns.get_loc('Time')]
        x = float(raw_data.iloc[i, raw_data.columns.get_loc('Acceleration X')*9.81])
        y = float(raw_data.iloc[i, raw_data.columns.get_loc('Acceleration Y')*9.81])
        z = float(raw_data.iloc[i, raw_data.columns.get_loc('Acceleration Z')*9.81])

        data_abs.append([t, np.sqrt(x**2 + y**2 + z**2)])

    df_abs = pd.DataFrame(data_abs, columns=['Time', 'Absolute Acceleration'])

    return io.list_to_csv(df_abs, "Absolute_Acceleration", output_dir)



# angular velocity in x - degrees/s
def sep_anvx(raw_data, output_dir):
    """
        :param raw_data:
        :param output_dir:
        :return:
        """

    # Select relevant columns
    df_acc_x = raw_data[['Time', 'Angular velocity X']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_acc_x['Angular velocity X'] = pd.to_numeric(df_acc_x['Angular velocity X'], errors='coerce') * 1.00

    # Drop any rows with NaN (from failed conversion)
    df_acc_x = df_acc_x.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_acc_x), "Angular_Velocity_X", output_dir)

# angular velocity in y - degrees/s
def sep_anvy(raw_data, output_dir):
    """
            :param raw_data:
            :param output_dir:
            :return:
            """

    # Select relevant columns
    df_acc_x = raw_data[['Time', 'Angular velocity Y']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_acc_x['Angular velocity Y'] = pd.to_numeric(df_acc_x['Angular velocity Y'], errors='coerce') * 1.00

    # Drop any rows with NaN (from failed conversion)
    df_acc_x = df_acc_x.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_acc_x), "Angular_Velocity_Y", output_dir)

# angular velocity in z - degrees/s
def sep_anvz(raw_data, output_dir):
    """
            :param raw_data:
            :param output_dir:
            :return:
            """

    # Select relevant columns
    df_acc_x = raw_data[['Time', 'Angular velocity Z']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_acc_x['Angular velocity Z'] = pd.to_numeric(df_acc_x['Angular velocity Z'], errors='coerce') * 1.00

    # Drop any rows with NaN (from failed conversion)
    df_acc_x = df_acc_x.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_acc_x), "Angular_Velocity_Z", output_dir)

# absolute angular velocity - degrees/s
def gen_anvabs(raw_data, output_dir):

    data_abs = []

    for i in range(len(raw_data)):
        t = raw_data.iloc[i, raw_data.columns.get_loc('Time')]
        x = float(raw_data.iloc[i, raw_data.columns.get_loc('Angular velocity X')])
        y = float(raw_data.iloc[i, raw_data.columns.get_loc('Angular velocity Y')])
        z = float(raw_data.iloc[i, raw_data.columns.get_loc('Angular velocity Z')])

        data_abs.append([t, np.sqrt(x**2 + y**2 + z**2)])

    df_abs = pd.DataFrame(data_abs, columns=['Time', 'Absolute Angular Velocity'])

    return io.list_to_csv(df_abs, "Absolute_Angular_Velocity", output_dir)


# angle in x - degrees
def sep_angx(raw_data, output_dir):
    """
                :param raw_data:
                :param output_dir:
                :return:
                """

    # Select relevant columns
    df_acc_x = raw_data[['Time', 'Angle X']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_acc_x['Angle X'] = pd.to_numeric(df_acc_x['Angle X'], errors='coerce') * 1.00

    # Drop any rows with NaN (from failed conversion)
    df_acc_x = df_acc_x.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_acc_x), "Angle_X", output_dir)

# angle in y - degrees
def sep_angy(raw_data, output_dir):
    """
                    :param raw_data:
                    :param output_dir:
                    :return:
                    """

    # Select relevant columns
    df_acc_x = raw_data[['Time', 'Angle Y']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_acc_x['Angle Y'] = pd.to_numeric(df_acc_x['Angle Y'], errors='coerce') * 1.00

    # Drop any rows with NaN (from failed conversion)
    df_acc_x = df_acc_x.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_acc_x), "Angle_Y", output_dir)

# angle in z - degrees
def sep_angz(raw_data, output_dir):
    """
                    :param raw_data:
                    :param output_dir:
                    :return:
                    """

    # Select relevant columns
    df_acc_x = raw_data[['Time', 'Angle Z']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_acc_x['Angle Z'] = pd.to_numeric(df_acc_x['Angle Z'], errors='coerce') * 1.00

    # Drop any rows with NaN (from failed conversion)
    df_acc_x = df_acc_x.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_acc_x), "Angle_Z", output_dir)


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

        # Extract the raw Time column and compute corrected time
        raw_data['Time'] = timestep_fix(raw_data['Time'])

        # Ensure all columns are still present
        print("Rebuilt columns:", raw_data.columns.tolist())

        # Now pass the full dataframe to the next function
        sep_accx(raw_data, output_dir)

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
