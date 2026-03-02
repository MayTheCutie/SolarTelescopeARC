# hai
import FileIO as io
import matplotlib.pyplot as plt
import scipy.fft as fft
import numpy as np



# .\Data\11_5_2025_evening_trial\Acceleration_X.csv

# loop files
while True:
    try:
        filepath = input("Please enter the name of the file: ")
        if filepath == "":
            break

        index = 0
        filestart = 0
        fileend = 0
        for char in filepath:
            index += 1
            if char == '\\':
                filestart = index
            if char == '.':
                fileend = index - 1

        filename = filepath[filestart:fileend]
        print(filename)

        data, output_dir, output_filename = io.csv_to_list(filepath)

        raw = plt.plot(data.iloc[:,0],data.iloc[:,1])
        plt.savefig(f"{filename}_raw.png")
        plt.show()

        time = data.iloc[:, 0].to_numpy()
        signal = data.iloc[:, 1].to_numpy()

        n = len(signal)

        dt = time[1] - time[0]  # sampling interval

        fft_values = fft.fft(signal)
        freq = fft.fftfreq(n, d=dt)

        upperthreshold = 0.5  # choose your value

        mask = (freq >= 0) & (upperthreshold > np.abs(fft_values))

        frequencies = freq[mask]
        amplitudes = np.abs(fft_values[mask])

        plt.figure()
        plt.plot(frequencies,amplitudes)
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.title("FFT")
        plt.savefig(f"{filename}_fft.png")
        plt.show()

    except EOFError:
        break




