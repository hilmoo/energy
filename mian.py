import csv, os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz
from scipy.signal import butter, filtfilt
from send2trash import send2trash

INPUT_AXIS = 'y'
INPUT_ACCE_CSV = 'Zacce1.csv'
DATA_SMOOTHING = 0
OUTPUT_DIRECTORY = f'{INPUT_AXIS}_Axis_Result'
OUTPUT_ACCE_IMG = f'{OUTPUT_DIRECTORY}\\acce.png'
OUTPUT_ACCES_CSV = f'{OUTPUT_DIRECTORY}\\acceS.csv'
OUTPUT_ACCES_IMG = f'{OUTPUT_DIRECTORY}\\acceS.png'
OUTPUT_VELO_CSV = f'{OUTPUT_DIRECTORY}\\velo.csv'
OUTPUT_VELO_IMG = f'{OUTPUT_DIRECTORY}\\velo.png'
OUTPUT_DISP_CSV = f'{OUTPUT_DIRECTORY}\\disp.csv'
OUTPUT_DISP_IMG = f'{OUTPUT_DIRECTORY}\\disp.png'

if not os.path.exists(OUTPUT_DIRECTORY):
    os.mkdir(OUTPUT_DIRECTORY)

df = pd.read_csv(INPUT_ACCE_CSV)
t = df['time']
a = df[f'a{INPUT_AXIS}']

plt.plot(t, a)
plt.savefig(OUTPUT_ACCE_IMG)
plt.close()

def butterworth_lowpass(data, cutoff_frequency, sampling_rate, order=6):
    nyquist_frequency = 0.5 * sampling_rate
    normal_cutoff = cutoff_frequency / nyquist_frequency
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    smoothed_data = filtfilt(b, a, data)
    return smoothed_data

cutoff_frequency = 0.1  # Adjust this value according to your requirements
sampling_rate = 200.0  # Replace with your actual sampling rate
order = 6  # You can adjust the filter order as needed

smoothed_acceleration = butterworth_lowpass(a.values, cutoff_frequency, sampling_rate, order)

if bool(DATA_SMOOTHING):
    t_data = []
    with open(INPUT_ACCE_CSV, mode='r') as input_file, open(OUTPUT_ACCES_CSV, mode='w', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        header = next(reader)
        writer.writerow(['time'] + [f'a{INPUT_AXIS}s'])
        for row in reader:
            t_data.append(float(row[0]))
        for t, acceS in zip(t_data, smoothed_acceleration):
            writer.writerow([t, acceS])

    df = pd.read_csv(OUTPUT_ACCES_CSV)
    x = df['time']
    y = df[f'a{INPUT_AXIS}s']

    plt.plot(x, y)
    plt.savefig(OUTPUT_ACCES_IMG)
    plt.close()
else:
    if os.path.exists(OUTPUT_ACCES_CSV):
        send2trash(OUTPUT_ACCES_CSV)
    if os.path.exists(OUTPUT_ACCES_IMG):
        send2trash(OUTPUT_ACCES_IMG)
    OUTPUT_ACCES_CSV=INPUT_ACCE_CSV


t_data = []
x_data = []
with open(OUTPUT_ACCES_CSV, mode='r') as input_file, open(OUTPUT_VELO_CSV, mode='w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    header = next(reader)
    writer.writerow(['time'] + ['velocity'])
    for row in reader:
        t_data.append(float(row[0]))
        x_data.append(float(row[1]))
    
    acc_integral = cumtrapz(x_data, x=t_data, initial=0)

    for tv, velocity in zip(t_data, acc_integral):
        writer.writerow([tv, velocity])

df = pd.read_csv(OUTPUT_VELO_CSV)
x = df['time']
y = df['velocity']

plt.plot(x, y)
plt.savefig(OUTPUT_VELO_IMG)
plt.close()

t_data = []
x_data = []
with open(OUTPUT_VELO_CSV, mode='r') as input_file, open(OUTPUT_DISP_CSV, mode='w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    header = next(reader)
    writer.writerow(['time'] + ['displacement'])
    for row in reader:
        t_data.append(float(row[0]))
        x_data.append(float(row[1]))
    
    acc_integral = cumtrapz(x_data, x=t_data, initial=0)

    for td, displacement in zip(t_data, acc_integral):
        writer.writerow([td, displacement])

df = pd.read_csv(OUTPUT_DISP_CSV)
x = df['time']
y = df['displacement']

plt.plot(x, y)
ax = plt.gca()
plt.savefig(OUTPUT_DISP_IMG)
plt.close()


