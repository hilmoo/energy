'''
#                      Pengolah Data Akselerasi
#               	Dibuat untuk Memenuhi Tugas UTS
# 				(c) Hilmi Musyaffa
'''

import csv, os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz
from scipy.signal import butter, filtfilt
from send2trash import send2trash

INPUT_AXIS = 'T'
YOUR_MASS = 50
INPUT_ACCE_CSV = 'example.csv'
DATA_SMOOTHING = 1  #1 for filter the data, 0 for not
OUTPUT_DIRECTORY = f'{INPUT_AXIS}_Axis_Result'
FINAL_RESULT = f'{OUTPUT_DIRECTORY}\\Zfinal.txt'
ENERGY = f'{OUTPUT_DIRECTORY}\\Zenergy.txt'


OUTPUT_ACCE_IMG = f'{OUTPUT_DIRECTORY}\\acce.png'
OUTPUT_ACCES_CSV = f'{OUTPUT_DIRECTORY}\\acceS.csv'
OUTPUT_ACCES_IMG = f'{OUTPUT_DIRECTORY}\\acceS.png'
OUTPUT_VELO_CSV = f'{OUTPUT_DIRECTORY}\\velo.csv'
OUTPUT_VELO_IMG = f'{OUTPUT_DIRECTORY}\\velo.png'
OUTPUT_DISP_CSV = f'{OUTPUT_DIRECTORY}\\disp.csv'
OUTPUT_DISP_IMG = f'{OUTPUT_DIRECTORY}\\disp.png'
OUTPUT_FORCE_CSV = f'{OUTPUT_DIRECTORY}\\force.csv'     
OUTPUT_FORCE_IMG = f'{OUTPUT_DIRECTORY}\\force.png'
OUTPUT_DIFO_CSV = f'{OUTPUT_DIRECTORY}\\difo.csv'
OUTPUT_DIFO_IMG = f'{OUTPUT_DIRECTORY}\\difo.png'
OUTPUT_ENERGY_CSV = f'{OUTPUT_DIRECTORY}\\energy.csv'
OUTPUT_ENERGY_IMG = f'{OUTPUT_DIRECTORY}\\energy.png'


CUTOFF_FREQUENCY = 0.00355  # Adjust this value according to your requirements
SAMPLING_RATE = 200.0  # Replace with your actual sampling rate
FILTER_ORDER = 4  # You can adjust the filter order as needed

if INPUT_AXIS == 'x':
    COLOR_LINE = '#FF3333'
    INPUT_AXIS_T = 'X Axis'
if INPUT_AXIS == 'y':
    COLOR_LINE = '#009900'
    INPUT_AXIS_T = 'Y Axis'
if INPUT_AXIS == 'z':
    COLOR_LINE = '#009900'
    INPUT_AXIS_T = 'Z Axis'
if INPUT_AXIS == 'T':
    COLOR_LINE = '#000000'
    INPUT_AXIS_T = 'Total'

if not os.path.exists(OUTPUT_DIRECTORY):
    os.mkdir(OUTPUT_DIRECTORY)

df = pd.read_csv(INPUT_ACCE_CSV)
t = df['time']
a = df[f'a{INPUT_AXIS}']

plt.plot(t, a, color = COLOR_LINE)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
plt.title(f'{INPUT_AXIS_T} Acceleration Changes Over Time')
plt.xlabel('time (s)')
plt.ylabel(r'$a_%s \ (m/s^2)$' % (INPUT_AXIS))
plt.savefig(OUTPUT_ACCE_IMG)
plt.close()

def butterworth_lowpass(data, CUTOFF_FREQUENCY, SAMPLING_RATE, FILTER_ORDER):
    nyquist_frequency = 0.5 * SAMPLING_RATE
    normal_cutoff = CUTOFF_FREQUENCY / nyquist_frequency
    b, a = butter(FILTER_ORDER, normal_cutoff, btype='low', analog=False)
    smoothed_data = filtfilt(b, a, data)
    return smoothed_data

smoothed_acceleration = butterworth_lowpass(a.values, CUTOFF_FREQUENCY, SAMPLING_RATE, FILTER_ORDER)


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


    plt.plot(x, y, color = COLOR_LINE)
    plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    plt.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
    plt.ylim(y.min()-y.min()/100, y.max()+y.max()/100)
    plt.title(f'{INPUT_AXIS_T} Acceleration Changes Over Time (FIltered)')
    plt.xlabel('time (s)')
    plt.ylabel(r'$a_%s \ (m/s^2)$' % (INPUT_AXIS))
    plt.savefig(OUTPUT_ACCES_IMG)
    plt.close()
else:
    if os.path.exists(OUTPUT_ACCES_CSV):
        send2trash(OUTPUT_ACCES_CSV)
    if os.path.exists(OUTPUT_ACCES_IMG):
        send2trash(OUTPUT_ACCES_IMG)
    OUTPUT_ACCES_CSV=INPUT_ACCE_CSV


t_data = [];x_data = []
with open(OUTPUT_ACCES_CSV, mode='r') as input_file, open(OUTPUT_VELO_CSV, mode='w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    header = next(reader)
    writer.writerow(['time'] + ['velocity'])
    for row in reader:
        t_data.append(float(row[0]))
        x_data.append(float(row[1]))

    velo_data = cumtrapz(x_data, x=t_data, initial=0)

    for tv, velocity in zip(t_data, velo_data):
        writer.writerow([tv, velocity])


df = pd.read_csv(OUTPUT_VELO_CSV)
x = df['time']
y = df['velocity']


plt.plot(x, y, color = COLOR_LINE)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
plt.ylim(y.min()-y.min()/100, y.max()+y.max()/100)
plt.title(f'{INPUT_AXIS_T} Velocity Changes Over Time')
plt.xlabel('time (s)')
plt.ylabel(r'$V_%s \ (m/s)$' % (INPUT_AXIS))
plt.savefig(OUTPUT_VELO_IMG)
plt.close()


t_data = [];x_data = []
with open(OUTPUT_VELO_CSV, mode='r') as input_file, open(OUTPUT_DISP_CSV, mode='w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    header = next(reader)
    writer.writerow(['time'] + ['displacement'])
    for row in reader:
        t_data.append(float(row[0]))
        x_data.append(float(row[1]))

    disp_data = cumtrapz(x_data, x=t_data, initial=0)

    for td, displacement in zip(t_data, disp_data):
        writer.writerow([td, displacement])


df = pd.read_csv(OUTPUT_DISP_CSV)
x = df['time']
y = df['displacement']


plt.plot(x, y, color = COLOR_LINE)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
plt.title(f'{INPUT_AXIS_T} Displacement Changes Over Time')
plt.xlabel('time (s)')
plt.ylabel(r'$s_%s \ (m)$' % (INPUT_AXIS))
plt.savefig(OUTPUT_DISP_IMG)
plt.close()


x = []
with open(OUTPUT_ACCES_CSV, mode='r') as input_file, open(OUTPUT_FORCE_CSV, mode='w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    header = next(reader)
    writer.writerow(['time'] + ['force'])
    for row in reader:
        x = float(row[1])
    
        force_data = (YOUR_MASS * x)

        writer.writerow([row[0]] + [force_data])


df = pd.read_csv(OUTPUT_FORCE_CSV)
x = df['time']
y = df['force']


plt.plot(x, y, color = COLOR_LINE)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
plt.ylim(y.min()-y.min()/100, y.max()+y.max()/100)
plt.title(f'{INPUT_AXIS_T} Force Changes Over TIme')
plt.xlabel('time (s)')
plt.ylabel(r'$F_%s \ (N)$' % (INPUT_AXIS))
plt.savefig(OUTPUT_FORCE_IMG)
plt.close()


x = []; y = []
with open(OUTPUT_DISP_CSV, mode='r') as input_D, open(OUTPUT_FORCE_CSV, mode='r') as input_F, open(OUTPUT_DIFO_CSV, mode='w', newline='') as output_file:
    read1 = csv.reader(input_D)
    read2 = csv.reader(input_F)
    writer = csv.writer(output_file)
    head1 = next(read1)
    head2 = next(read2)
    writer.writerow(['displacement'] + ['force'])
    for row in read1:
        x.append(float(row[1]))
    for row in read2:
        y.append(float(row[1]))
    for disp, force in zip(x, y):
        writer.writerow([disp, force])


df = pd.read_csv(OUTPUT_DIFO_CSV)
x = df['displacement']
y = df['force']


plt.plot(x, y, color = COLOR_LINE)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
plt.ylim(y.min()-y.min()/100, y.max()+y.max()/100)
plt.title(f'{INPUT_AXIS_T} Force Changes Over Displacement')
plt.xlabel(r'$s_%s \ (m)$' % (INPUT_AXIS))
plt.ylabel(r'$F_%s \ (N)$' % (INPUT_AXIS))
plt.savefig(OUTPUT_DIFO_IMG)
plt.close()


with open(FINAL_RESULT, mode='w', newline='') as output_file:
    writer = csv.writer(output_file)
    work = cumtrapz(y, x=x)
    works = work.sum()/(23.591786)
    writer.writerow([f'Work = {works} Joule'])


energy = []
with open(OUTPUT_VELO_CSV, mode='r') as input_file, open(ENERGY, mode='w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    header = next(reader)
    for row in reader:
        x = float(row[1])
        ex = (1/2 * YOUR_MASS * x * x)
        energy.append(ex)
    energyF = sum(energy)/23.591786
    writer.writerow([f'Energy = {energyF} Joule'])
