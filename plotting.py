import matplotlib.pyplot as plt
import FileIO as io
from scipy import interpolate as ip
from scipy import fftpack
from scipy import fft
import numpy as np

def moving_average(data, window_size):
    kernel = np.ones(window_size) / window_size
    return np.convolve(data, kernel, mode='valid')

def user_input():
    print("""Do you want to input data?
          (0) Yes
          (1) No - if asked before, select. no dupes plz""")
    try:
        input_data_option = int(input())
    except ValueError:
        input_data_option = 1
    match input_data_option:
        case 0:
            print("To be plotted data:")
            total, output_dir, output_filename = io.csv_to_list()
            print(total)
            if total is None:
                print("There's no data, doing nothing")
                return None, 0, 100, -100, 10, 500, -1

        case 1:
            print("No input data added")
            total = None

    # Cutoff is for the y_val - original cutoff stopped gathering data after
    # x time period. As we want to cover the entire dataset BUT only exclude data
    # points that are above and below some number, the cutoff will only apply to
    # those points.
    print("List the upper bound:")
    print("If you don't want a cutoff, use '100'.")
    try:
        upper_cutoff = float(input())
    except ValueError:
        upper_cutoff = 100
    print("List the lower bound:")
    print("If you don't want a cutoff, use '-100'.")
    try:
        lower_cutoff = float(input())
    except ValueError:
        lower_cutoff = -100
    print("List the lower bound:")
    print("If you don't want a cutoff, use '-100'.")
    try:
        time_cutoff = float(input())
    except ValueError:
        time_cutoff = -1
    print("""Plot types:
                 0 - Raw Data
                 1 - Analysed through Cubic Splines / Interpolated
                 2 - Moving Average
                 3 - Fourier Transform""")
    try:
        plot_type = int(input())
        if plot_type not in [0, 1, 2, 3]:
            plot_type = 0
    except ValueError:
        plot_type = 0

    # Set defaults
    window_size = 3
    max_freq = 500

    # Get additional input depending on plot type
    if plot_type == 2:
        try:
            print("Enter window size (default = 3):")
            ws = int(input())
            if ws > 0:
                window_size = ws
        except ValueError:
            pass

    if plot_type == 3:
        try:
            print("Enter max frequency to plot (default = 500 Hz):")
            mf = float(input())
            if mf > 0:
                max_freq = mf
        except ValueError:
            pass

    return total, plot_type, upper_cutoff, lower_cutoff, window_size, max_freq, time_cutoff

def data_things(total, upper_cutoff, lower_cutoff, time_cutoff):

    if total is None:
        print("There's no data, doing nothing")
        return None

    data = []
    for row in total[1:]:  # Skip header
        if not row or len(row) < 2:
            continue  # Skip empty or short rows
        try:
            x_val = float(row[0].strip())
            y_val = float(row[1].strip())
            data.append((x_val, y_val))
        except (ValueError, IndexError):
            continue  # Skip rows with non-numeric values or unexpected issues

    # Filter the data BEFORE zipping
    #print(data)
    filtered_data = []
    print(time_cutoff)
    if time_cutoff is not None and 0.0 < time_cutoff < data[-1][0]:
        time_cutoff_index = next((i for i, row in enumerate(data) if row[0] > time_cutoff), len(data))
        #print(data)
        print(time_cutoff_index)
        data = data[:time_cutoff_index]
    else:
        data = data[:]

    for x_val, y_val in data:
        if upper_cutoff >= y_val >= lower_cutoff and not y_val is None:
            filtered_data.append((x_val, y_val))  # If the y_value is part of the conditions, append
        # Do nothing otherwise


    return filtered_data

def filename_input(filename, plot_name):
    output_filename = filename.split('.')
    return output_filename[0] + plot_name + '.' + output_filename[1]

def match_plot(filtered_data, plot_type, window_size, max_freq, filename):

    #print(filtered_data)
    #plot = plt.Figure()
    if filtered_data:
        x_raw, y_raw = zip(*filtered_data)
        match plot_type:
            case 0:  # raw data
                raw_data_plot(x_raw, y_raw, filename)
                #plot = pickle.load(open('FigureObject.fig.pickle', 'rb'))

            case 1:  # cubic spline
                cubic_spline_plot(x_raw, y_raw, filename)
                #plot = pickle.load(open('FigureObject.fig.pickle', 'rb'))

            case 2:  # moving avg
                moving_avg_plot(x_raw, y_raw, window_size, filename)
                #plot = pickle.load(open('FigureObject.fig.pickle', 'rb'))

            case 3:  # fourier transform
                fourier_plot(x_raw, y_raw, max_freq, filename)
                #plot = pickle.load(open('FigureObject.fig.pickle', 'rb'))
    else:
        print("No valid data found to plot.")


def raw_data_plot(x_raw, y_raw, filename):
    fig, ax = plt.subplots()
    ax.plot(x_raw, y_raw)
    fig.savefig(filename_input(filename, "raw-data-plot"))


def cubic_spline_plot(x_raw, y_raw, filename):
    # Convert to NumPy arrays for interpolation
    x_raw = np.array(x_raw)
    y_raw = np.array(y_raw)

    # Sort by x values (just in case)
    sorted_indices = np.argsort(x_raw)
    x_raw = x_raw[sorted_indices]
    y_raw = y_raw[sorted_indices]

    # Remove duplicate x values
    _, unique_indices = np.unique(x_raw, return_index=True)
    x_raw = x_raw[unique_indices]
    y_raw = y_raw[unique_indices]

    # Create the cubic spline interpolator
    cs = ip.CubicSpline(x_raw, y_raw)

    # Only smooth out the y data as x data is time
    y_smooth = cs(x_raw)

    # Plot original points and the smoothed curve
    fig, ax = plt.subplots()
    ax.plot(x_raw, y_raw, 'o', label='Original Data')
    ax.plot(x_raw, y_smooth, '-', label='Cubic Spline Interpolation')
    ax.legend()
    fig.savefig(filename_input(filename, "cubic-spline-plot"))

def moving_avg_plot(x_raw, y_raw, window_size, filename):
    if len(y_raw) < window_size:
        print(f"Not enough data for window size {window_size}")
    else:
        y_avg = moving_average(y_raw, window_size)

        half = window_size // 2
        if window_size % 2 == 0:
            x_avg = x_raw[half - 1: -half]
        else:
            x_avg = x_raw[half: -half]

        fig, ax = plt.subplots()
        ax.plot(x_raw, y_raw, 'o', alpha=0.3, label='Original')
        ax.plot(x_avg, y_avg, '-', color='orange', linewidth=2, label=f'{window_size}-Point Average')
        ax.legend()
        ax.set_xlabel("Time")
        ax.set_ylabel("Value")
        ax.set_title(f"{window_size}-Point Moving Average")
        fig.savefig(filename_input(filename, "moving-avg-plot"))

def fourier_plot(x_raw, y_raw, max_freq, filename):
    # Make sure x_raw is a NumPy array
    x_raw = np.array(x_raw)
    y_raw = np.array(y_raw)

    # Estimate sample spacing from time data
    dt = np.mean(np.diff(x_raw))  # Average time difference between samples

    num_samples = len(y_raw)
    yf = fft.fft(y_raw)
    xf = fftpack.fftfreq(num_samples, dt)[:num_samples // 2]  # Only keep positive frequencies
    amplitudes = 2.0 / num_samples * np.abs(yf[:num_samples // 2])  # Normalize and get amplitude

    print("Max amplitude:", np.max(amplitudes))
    print("First few frequencies:", xf[:3])
    print("First few amplitudes:", amplitudes[:3])

    mask = xf <= max_freq

    fig, ax = plt.subplots()
    ax.plot(xf[mask], amplitudes[mask])
    ax.set_xlabel("Frequency [Hz]")
    ax.set_ylabel("Amplitude")
    ax.set_title("Fourier Transform (Zoomed In)")
    ax.grid(True)
    fig.tight_layout()
    fig.savefig(filename_input(filename, "fourier-plot"))
