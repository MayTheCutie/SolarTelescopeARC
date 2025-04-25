import random
import FileIO as io
import plotting as plt
import os
import matplotlib.pyplot as mpl

data_list = []
properties_list = []
data_names = []
option = 0

# This initial section will
print("Input Data: (Absolute Path)")
initial_data, output_dir_data, output_filename_data = io.csv_to_list()
data_list.append(initial_data)
data_names.append(output_filename_data.split("_.")[0].replace("_", " "))
print("Plot Properties: (Absolute Path)")
properties, output_dir_properties, output_properties = io.csv_to_list()
properties_list.append(properties)
while True:
    print("Input Data: (Absolute Path)")
    added_data, o_d_d_temp, o_f_d_temp = io.csv_to_list()
    data_list.append(added_data)
    data_names.append(o_f_d_temp.split("_.")[0].replace("_", " "))
    print("Plot Properties: (Absolute Path)")
    properties, o_d_p_temp, o_f_p_temp = io.csv_to_list()
    properties_list.append(properties)
    try:
        option = int(input("""Do you want to input more data?
                             (0) Yes
                             (1) No\n"""))
        if option == 1:
            break
    except ValueError:
        print("Invalid input, stopping input loop.")
        break

plot_number = 2
if properties_list[0][3] is not None and int(properties_list[0][3]) >= 2:
    kernel_size = int(properties_list[0][3])
else: kernel_size = 3
max_freq = 500

# Make the final plot be in Graphs dir
output_filename = output_filename_data.split(".")
filename = os.path.join(output_dir_data, "Graphs", f"All_{output_filename[0]}.png")

def extract_plot_properties(props, index):
    """
    Extracts and validates plot configuration values from a list.
    Returns:
        plot_type, upper_cutoff, lower_cutoff, window_size, max_freq, start_cutoff, end_cutoff
    """

    # Default values
    plot_type = 0
    upper_cutoff = 100
    lower_cutoff = -100
    window_size = 3
    max_freq = 500
    start_cutoff = -1
    end_cutoff = -1

    if len(props) >= 7:
        try:
            if props[0] is not None and -1 < int(props[0]) < 4:
                plot_type = int(props[0])
        except ValueError:
            pass
        try:
            if props[1] is not None:
                upper_cutoff = float(props[1])
        except ValueError:
            pass
        try:
            if props[2] is not None:
                lower_cutoff = float(props[2])
        except ValueError:
            pass
        try:
            if props[3] is not None and int(props[3]) >= 2:
                window_size = int(props[3])
        except ValueError:
            pass
        try:
            if props[4] is not None and float(props[4]) > 0:
                max_freq = float(props[4])
        except ValueError:
            pass
        try:
            if props[5] is not None:
                start_cutoff = float(props[5])
        except ValueError:
            pass
        try:
            if props[6] is not None:
                end_cutoff = float(props[6])
        except ValueError:
            pass
    else:
        print(f"⚠️ Properties file {index+1} has unexpected format, using defaults.")

    return plot_type, upper_cutoff, lower_cutoff, window_size, max_freq, start_cutoff, end_cutoff


# Use plotting to analyze
i = 0
filtered_data = []
for idx, (plot_properties, data) in enumerate(zip(properties_list, data_list)):
    print(f"Processing dataset {idx+1}...")
    plot_type, upper_cutoff, lower_cutoff, window_size, max_freq, starter_time_cutoff, end_time_cutoff = extract_plot_properties(plot_properties, idx)

    filtered_data.append(plt.data_things(data, upper_cutoff, lower_cutoff, starter_time_cutoff, end_time_cutoff))

def get_cmap(n, name='hsv'):
    """Returns a function that maps each index in 0, 1, ..., n-1 to a distinct RGB color."""
    return mpl.colormaps[name]

def generate_random_colors(n, cmap_name='tab20'):
    cmap = mpl.colormaps[cmap_name].resampled(n)
    colors = [cmap(k / n) for k in range(n)]
    random.shuffle(colors)
    return colors

def overlay_moving_avg_plots(data_lists, window, fn):
    fig, ax = mpl.subplots()
    colors = generate_random_colors(len(data_lists))

    for j, data_temp in enumerate(data_lists):
        x_raw = [pt[0] for pt in data_temp]
        y_raw = [pt[1] for pt in data_temp]

        x_avg, y_avg = plt.moving_avg(x_raw, y_raw, window)
        if x_avg is None or y_avg is None:
            continue

        label = data_names[j] if data_names and j < len(data_names) else f'Dataset {j + 1}'

        ax.plot(x_avg, y_avg, '-', linewidth=2, color=colors[j], label=label)

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Acceleration (m/s²)")
    ax.set_title(f"{window}-Point Moving Average Overlays")
    ax.legend()
    fig.savefig(plt.filename_input(fn, "stacked-moving-avg"))

overlay_moving_avg_plots(filtered_data, kernel_size, filename)
