import matplotlib.pyplot as plt
import FileOrganization as FOrg

def main():
    print("To be plotted data:")
    total, output_dir = FOrg.csv_to_list()
    print("List the upper bound - this will be used for lower bound too:")
    print("If you don't want a cutoff, use '100'.")
    cutoff = float(input())

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
        if y_val >= cutoff or y_val <= -cutoff:
            break  # Stop adding once we hit or pass the cutoff
        filtered_data.append((x_val, y_val))

    print(filtered_data)
    if filtered_data:
        x, y = zip(*filtered_data)

        fig, ax = plt.subplots()
        ax.plot(x, y)
        plt.show()
    else:
        print("No valid data found to plot.")

if __name__ == "__main__":
    main()