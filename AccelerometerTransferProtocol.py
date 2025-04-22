import FileIO as io
import plotting as plt

# Import files from computer, csv_to_list - use total and output_dir
print("Input Data:")
total_data, output_dir_data, output_filename_data = io.csv_to_list()
print("""(0) Plot Properties File
      (1) Input properties""")
try:
    plot_properties_opt = int(input())
except ValueError:
    plot_properties_opt = 1 #default as user input
match plot_properties_opt:
    case 0:
        print("Plot Properties:")
        properties, output_dir_properties, output_properties = io.csv_to_list()
    case 1:
        total, plot_type, upper_cutoff, lower_cutoff, window_size, max_freq, time_cutoff = plt.user_input()
        properties = []

# Make the final plot be in Graphs dir
output_filename = output_filename_data.split(".")
filename = output_dir_data + "\\Graphs\\" + output_filename[0] + ".png"

# Use plotting to analyze
if len(properties) == 6:
    plot_type = 0
    if properties[0] is not None or -1 < int(properties[0]) < 4:
        plot_type = int(properties[0])
    upper_cutoff = 100
    if properties[1] is not None:
        upper_cutoff = float(properties[1])
    lower_cutoff = -100
    if properties[2] is not None:
        lower_cutoff = float(properties[2])
    window_size = 3
    if properties[3] is not None or int(properties[3]) >= 2:
        window_size = int(properties[3])
    max_freq = 500
    if properties[4] is not None or float(properties[4]) > 0:
        max_freq = float(properties[4])
    time_cutoff = -1
    if properties[5] is not None or float(properties[5]) > 0:
        time_cutoff = float(properties[5])
else:
    print("Properties file has unexpected format, setting default values")
    plot_type = 0
    upper_cutoff = 100
    lower_cutoff = -100
    window_size = 3
    max_freq = 500
    time_cutoff = -1

filtered_data = plt.data_things(total_data, upper_cutoff, lower_cutoff, time_cutoff)
plot = plt.match_plot(filtered_data, plot_type, window_size, max_freq, filename)
