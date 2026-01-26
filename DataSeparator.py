import time
import FileIO as io
import numpy as np
import pandas as pd

def sep_accx(raw_data, output_dir):

    """
    acceleration in x - m/s^2

    :param raw_data:
    :param output_dir:
    :return:
    """

    # Select relevant columns
    df_acc_x = raw_data[['Time', 'Acceleration X']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_acc_x['Acceleration X'] = pd.to_numeric(df_acc_x['Acceleration X'], errors='coerce')

    # Drop any rows with NaN (from failed conversion)
    df_acc_x = df_acc_x.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_acc_x), "Acceleration_X", output_dir)


def sep_accy(raw_data, output_dir):

    """
    acceleration in y - m/s^2

    :param raw_data:
    :param output_dir:
    :return:
    """

    # Select relevant columns
    df_acc_y = raw_data[['Time', 'Acceleration Y']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_acc_y['Acceleration Y'] = pd.to_numeric(df_acc_y['Acceleration Y'], errors='coerce')

    # Drop any rows with NaN (from failed conversion)
    df_acc_y = df_acc_y.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_acc_y), "Acceleration_Y", output_dir)

def sep_accz(raw_data, output_dir):

    """
    acceleration in z - m/s^2

    :param raw_data:
    :param output_dir:
    :return:
    """

    # Select relevant columns
    df_acc_z = raw_data[['Time', 'Acceleration Z']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_acc_z['Acceleration Z'] = pd.to_numeric(df_acc_z['Acceleration Z'], errors='coerce')

    # Drop any rows with NaN (from failed conversion)
    df_acc_z = df_acc_z.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_acc_z), "Acceleration_Z", output_dir)

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
    """
    absolute acceleration - m/s^2

    :param raw_data:
    :param output_dir:
    :return:
    """

    data_abs = []

    for i in range(len(raw_data)):
        t = raw_data.iloc[i, raw_data.columns.get_loc('Time')]
        x = float(raw_data.iloc[i, raw_data.columns.get_loc('Acceleration X')]) - 1.0
        y = float(raw_data.iloc[i, raw_data.columns.get_loc('Acceleration Y')]) - 1.0
        z = float(raw_data.iloc[i, raw_data.columns.get_loc('Acceleration Z')]) - 1.0

        data_abs.append([t, int((np.sqrt(x**2 + y**2 + z**2)) * 1000 + 1e-12) / 1000])

    df_abs = pd.DataFrame(data_abs, columns=['Time', 'Absolute Acceleration'])

    return io.list_to_csv(df_abs, "Absolute_Acceleration", output_dir)



def sep_anvx(raw_data, output_dir):
    """
    angular velocity in x - degrees/s

    :param raw_data:
    :param output_dir:
    :return:
    """

    # Select relevant columns
    df_anv_x = raw_data[['Time', 'Angular velocity X']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_anv_x['Angular velocity X'] = pd.to_numeric(df_anv_x['Angular velocity X'], errors='coerce') * 1.00

    # Drop any rows with NaN (from failed conversion)
    df_anv_x = df_anv_x.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_anv_x), "Angular_Velocity_X", output_dir)

def sep_anvy(raw_data, output_dir):
    """
    angular velocity in y - degrees/s

    :param raw_data:
    :param output_dir:
    :return:
    """

    # Select relevant columns
    df_anv_y = raw_data[['Time', 'Angular velocity Y']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_anv_y['Angular velocity Y'] = pd.to_numeric(df_anv_y['Angular velocity Y'], errors='coerce') * 1.00

    # Drop any rows with NaN (from failed conversion)
    df_anv_y = df_anv_y.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_anv_y), "Angular_Velocity_Y", output_dir)

def sep_anvz(raw_data, output_dir):
    """
    angular velocity in z - degrees/s

    :param raw_data:
    :param output_dir:
    :return:
    """

    # Select relevant columns
    df_anv_z = raw_data[['Time', 'Angular velocity Z']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_anv_z['Angular velocity Z'] = pd.to_numeric(df_anv_z['Angular velocity Z'], errors='coerce') * 1.00

    # Drop any rows with NaN (from failed conversion)
    df_anv_z = df_anv_z.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_anv_z), "Angular_Velocity_Z", output_dir)

def gen_anvabs(raw_data, output_dir):
    """
    absolute angular velocity - degrees/s

    :param raw_data:
    :param output_dir:
    :return:
    """

    data_abs = []

    for i in range(len(raw_data)):
        t = raw_data.iloc[i, raw_data.columns.get_loc('Time')]
        x = float(raw_data.iloc[i, raw_data.columns.get_loc('Angular velocity X')])
        y = float(raw_data.iloc[i, raw_data.columns.get_loc('Angular velocity Y')])
        z = float(raw_data.iloc[i, raw_data.columns.get_loc('Angular velocity Z')])

        data_abs.append([t, int((np.sqrt(x**2 + y**2 + z**2)) * 1000 + 1e-12) / 1000])

    df_abs = pd.DataFrame(data_abs, columns=['Time', 'Absolute Angular Velocity'])

    return io.list_to_csv(df_abs, "Absolute_Angular_Velocity", output_dir)

def sep_angx(raw_data, output_dir):
    """
    angle in x - degrees

    :param raw_data:
    :param output_dir:
    :return:
    """

    # Select relevant columns
    df_ang_x = raw_data[['Time', 'Angle X']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_ang_x['Angle X'] = pd.to_numeric(df_ang_x['Angle X'], errors='coerce') * 1.00

    # Drop any rows with NaN (from failed conversion)
    df_ang_x = df_ang_x.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_ang_x), "Angle_X", output_dir)

def sep_angy(raw_data, output_dir):
    """
    angle in y - degrees

    :param raw_data:
    :param output_dir:
    :return:
    """

    # Select relevant columns
    df_ang_y = raw_data[['Time', 'Angle Y']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_ang_y['Angle Y'] = pd.to_numeric(df_ang_y['Angle Y'], errors='coerce') * 1.00

    # Drop any rows with NaN (from failed conversion)
    df_ang_y = df_ang_y.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_ang_y), "Angle_Y", output_dir)

def sep_angz(raw_data, output_dir):
    """
    angle in z - degrees

    :param raw_data:
    :param output_dir:
    :return:
    """

    # Select relevant columns
    df_ang_z = raw_data[['Time', 'Angle Z']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_ang_z['Angle Z'] = pd.to_numeric(df_ang_z['Angle Z'], errors='coerce') * 1.00

    # Drop any rows with NaN (from failed conversion)
    df_ang_z = df_ang_z.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_ang_z), "Angle_Z", output_dir)

def sep_magx(raw_data, output_dir):
    """
    magnetic field in x - micro teslas

    :param raw_data:
    :param output_dir:
    :return:
    """

    # Select relevant columns
    df_mag_x = raw_data[['Time', 'Magnetic field X']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_mag_x['Magnetic field X'] = pd.to_numeric(df_mag_x['Magnetic field X'], errors='coerce') * 1.00

    # Drop any rows with NaN (from failed conversion)
    df_mag_x = df_mag_x.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_mag_x), "Magnetic field X", output_dir)

def sep_magy(raw_data, output_dir):
    """
    magnetic field in y - micro teslas

    :param raw_data:
    :param output_dir:
    :return:
    """

    # Select relevant columns
    df_mag_y = raw_data[['Time', 'Magnetic field Y']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_mag_y['Magnetic field Y'] = pd.to_numeric(df_mag_y['Magnetic field Y'], errors='coerce') * 1.00

    # Drop any rows with NaN (from failed conversion)
    df_mag_y = df_mag_y.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_mag_y), "Magnetic field Y", output_dir)

def sep_magz(raw_data, output_dir):
    """
    magnetic field in z - micro teslas

    :param raw_data:
    :param output_dir:
    :return:
    """

    # Select relevant columns
    df_mag_z = raw_data[['Time', 'Magnetic field Z']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_mag_z['Magnetic field Z'] = pd.to_numeric(df_mag_z['Magnetic field Z'], errors='coerce') * 1.00

    # Drop any rows with NaN (from failed conversion)
    df_mag_z = df_mag_z.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_mag_z), "Magnetic field Z", output_dir)

def gen_magabs(raw_data, output_dir):
    """
    absolute magnetic field - micro teslas

    :param raw_data:
    :param output_dir:
    :return:
    """

    data_abs = []

    for i in range(len(raw_data)):
        t = raw_data.iloc[i, raw_data.columns.get_loc('Time')]
        x = float(raw_data.iloc[i, raw_data.columns.get_loc('Magnetic field X')])
        y = float(raw_data.iloc[i, raw_data.columns.get_loc('Magnetic field Y')])
        z = float(raw_data.iloc[i, raw_data.columns.get_loc('Magnetic field Z')])


        data_abs.append([t, int((np.sqrt(x**2 + y**2 + z**2)) * 1000 + 1e-12) / 1000])

    df_abs = pd.DataFrame(data_abs, columns=['Time', 'Absolute Magnetic Field'])

    return io.list_to_csv(df_abs, "Absolute_Magnetic_Field", output_dir)

def sep_temp(raw_data, output_dir):
    """
    temperature - degrees celsius

    :param raw_data:
    :param output_dir:
    :return:
    """

    # Select relevant columns
    df_temp = raw_data[['Time', 'Temperature']].copy()

    # Convert Acceleration X to float and multiply by 9.81
    df_temp['Temperature'] = pd.to_numeric(df_temp['Temperature'], errors='coerce') * 1.00

    # Drop any rows with NaN (from failed conversion)
    df_temp = df_temp.dropna().reset_index(drop=True)

    # Save to same directory
    return io.list_to_csv(pd.DataFrame(df_temp), "Temperature", output_dir)

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
        sep_accx(raw_data, output_dir)
        print("spot 3")
        sep_accy(raw_data, output_dir)
        print("spot 4")
        sep_accz(raw_data, output_dir)
        print("spot 5")
        gen_accabs(raw_data, output_dir)
        print("spot 6")
        sep_anvx(raw_data, output_dir)
        print("spot 7")
        sep_anvy(raw_data, output_dir)
        print("spot 8")
        sep_anvz(raw_data, output_dir)
        print("spot 9")
        gen_anvabs(raw_data, output_dir)
        print("spot 10")
        sep_angx(raw_data, output_dir)
        print("spot 11")
        sep_angy(raw_data, output_dir)
        print("spot 12")
        sep_angz(raw_data, output_dir)
        print("spot 13")
        sep_magx(raw_data, output_dir)
        print("spot 14")
        sep_magy(raw_data, output_dir)
        print("spot 15")
        sep_magz(raw_data, output_dir)
        print("spot 16")
        gen_magabs(raw_data, output_dir)
        print("spot 17")
        sep_temp(raw_data, output_dir)
        print("spot 18")

    except Exception as e:
        print(f"An error occurred: {e}")

    print("--- %s seconds ---" % (time.time() - star_time).__round__(2))


if __name__ == "__main__":
    main()
