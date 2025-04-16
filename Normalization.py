import FileOrganization as FOrg

def avg_list(separated_data, output_dir):
    av_list = []
    #averaged_list = np.array(av_list)
    for i in range(1, len(separated_data) - 1):
        #temp_list = [separated_data[i - 1], separated_data[i], separated_data[i + 1]]
        av_list.append((separated_data[i - 1] + separated_data[i] + separated_data[i + 1])/3)
    return FOrg.list_to_csv(separated_data, av_list, 1, output_dir, "Average")

def main():
    separated_data, output_dir = FOrg.csv_to_list()
    try:
        avg_list(separated_data, output_dir)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()