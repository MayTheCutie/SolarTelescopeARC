import matplotlib.pyplot as plt
import FileOrganization as FOrg
from scipy import interpolate as ip
import numpy as np

def main():
    print("To be plotted data:")
    total, output_dir = FOrg.csv_to_list()

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
    print("Plot types:")
    print("0 - Raw Data")
    print("1 - Analysed through Cubic Splines / Interpolated")
    print("2 - Moving Average")
    try:
        plot_type = int(input())
        if plot_type < 0 or plot_type > 2:
            plot_type = 0
        if plot_type == 2:
            print("What window size do you want? (integer)")
            window_size = int(input())
            if window_size <= 0:
                window_size = 3
    except ValueError or TypeError:
        plot_type = 0
        window_size = 3


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
    filtered_data = []
    for x_val, y_val in data:
        if upper_cutoff >= y_val >= lower_cutoff and not y_val is None:
            filtered_data.append((x_val, y_val))  # If the y_value is part of the conditions, append
        # Do nothing otherwise

        # This will make the process take longer as it is moving through the entire set
        # rather than stopping once the values hit the cutoff, but will provide data
        # from the entire dataset except.

    #print(filtered_data)
    if filtered_data:
        x_raw, y_raw = zip(*filtered_data)
        match plot_type:
            case 0:
                fig, ax = plt.subplots()
                ax.plot(x_raw, y_raw)
                plt.show()
            case 1:
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

                y_smooth = cs(x_raw)

                # Plot original points and the smoothed curve
                fig, ax = plt.subplots()
                ax.plot(x_raw, y_raw, 'o', label='Original Data')
                ax.plot(x_raw, y_smooth, '-', label='Cubic Spline Interpolation')
                ax.legend()
                plt.show()
            case 2:
                if len(y_raw) < window_size:
                    print(f"Not enough data for window size {window_size}")
                else:
                    kernel = np.ones(window_size) / window_size
                    y_avg = np.convolve(y_raw, kernel, mode='valid')

                    half = window_size // 2
                    if window_size % 2 == 0:
                        x_avg = x_raw[half - 1: -(half)]
                    else:
                        x_avg = x_raw[half: -half]

                    fig, ax = plt.subplots()
                    ax.plot(x_raw, y_raw, 'o', alpha=0.3, label='Original')
                    ax.plot(x_avg, y_avg, '-', color='orange', linewidth=2, label=f'{window_size}-Point Average')
                    ax.legend()
                    ax.set_xlabel("Time")
                    ax.set_ylabel("Value")
                    plt.title(f"{window_size}-Point Moving Average")
                    plt.show()
    else:
        print("No valid data found to plot.")




if __name__ == "__main__":
    main()