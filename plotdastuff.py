# hai
import FileIO as io
import matplotlib.pyplot as plt
import numpy.fft as fft
import fileinput

# .\Data\11_5_2025_evening_trial\Acceleration_X.csv

# loop files
while True:
    try:
        filename = input("Please enter the name of the file: ")

        data = io.csv_to_list(filename)

        raw = plt.plot(data)
        plt.show()
        plt.savefig("")
        fft = plt.plot(fft.fft(data, axis=0))
        plt.show()
        plt.savefig()

    except EOFError:
        break




