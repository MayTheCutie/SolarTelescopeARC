import FileIO as io
import plotting as plt
from AccelerometerAnalyzer import extract_plot_properties

# Import files from computer, csv_to_list - use total and output_dir
print("Input Data:")
total_data, output_dir_data, output_filename_data = io.csv_to_list()
print("Plot Properties: (Absolute Path)")
properties, output_dir_properties, output_properties = io.csv_to_list()

# Make the final plot be in Graphs dir
output_filename = output_filename_data.split(".")
filename = output_dir_data + "\\Graphs\\" + output_filename[0] + ".png"

# Use plotting to analyze
plot_type, upper_cutoff, lower_cutoff, window_size, max_freq, starter_time_cutoff, end_time_cutoff = extract_plot_properties(properties, 0)

filtered_data = plt.data_things(total_data, upper_cutoff, lower_cutoff, starter_time_cutoff, end_time_cutoff)
plot = plt.match_plot(filtered_data, plot_type, window_size, max_freq, filename)
