import pandas as pd
from main import *

df1u = pd.read_csv(INPUT_ACCE_CSV)
df2u = pd.read_csv(f'{INPUT_AXIS}_Axis_Result_Unfiltered\\velo.csv')
df3u = pd.read_csv(f'{INPUT_AXIS}_Axis_Result_Unfiltered\\disp.csv')
df4u = pd.read_csv(f'{INPUT_AXIS}_Axis_Result_Unfiltered\\force.csv')
df5u = pd.read_csv(f'{INPUT_AXIS}_Axis_Result_Unfiltered\\difo.csv')

df1s = pd.read_csv(f'{INPUT_AXIS}_Axis_Result_Filtered\\acceS.csv')
df2s = pd.read_csv(f'{INPUT_AXIS}_Axis_Result_Filtered\\velo.csv')
df3s = pd.read_csv(f'{INPUT_AXIS}_Axis_Result_Filtered\\disp.csv')
df4s = pd.read_csv(f'{INPUT_AXIS}_Axis_Result_Filtered\\force.csv')
df5s = pd.read_csv(f'{INPUT_AXIS}_Axis_Result_Filtered\\difo.csv')

COMBO_DIRECTORY = f'{INPUT_AXIS}_Axis_Combo'
COMBO_ACCE = f'{COMBO_DIRECTORY}\\acce.png'
COMBO_VELO = f'{COMBO_DIRECTORY}\\velo.png'
COMBO_DISP = f'{COMBO_DIRECTORY}\\disp.png'
COMBO_FORCE = f'{COMBO_DIRECTORY}\\force.png'
COMBO_DIFO = f'{COMBO_DIRECTORY}\\difo.png'

if not os.path.exists(COMBO_DIRECTORY):
    os.mkdir(COMBO_DIRECTORY)

t = df1u['time']
aU = df1u[f'a{INPUT_AXIS}']; aS = df1s[f'a{INPUT_AXIS}s']
vU = df2u['velocity']; vS = df2s['velocity']
dU = df3u['displacement']; dS = df3s['displacement']
fU = df4u['force']; fS = df4s['force']
dfU1 = df5u['displacement']; dfS1 = df5s['displacement']
dfU2 = df5u['force']; dfS2 = df5s['force']

RED = '#FF3333'
GREEN = '#009900'

plt.style.use('ggplot')
fig, axs = plt.subplots(2)
axs[0].plot(t, aU, color='red', label=f'$a_{INPUT_AXIS}, Unfiltered$')
axs[0].set_ylabel(f'$a_{INPUT_AXIS} \ (m/s^2)$')
axs[0].yaxis.set_label_position("right")
axs[0].legend()
axs[1].plot(t, aS, color='green', label=f'$a_{INPUT_AXIS}, Filtered$')
axs[1].set_xlabel('time (s)')
axs[1].set_ylabel(f'$a_{INPUT_AXIS} \ (m/s^2)$')
axs[1].yaxis.set_label_position("right")
axs[1].legend()
fig.suptitle(f'{INPUT_AXIS_T} Acceleration Changes Over Time')
plt.savefig(COMBO_ACCE)
plt.close()

fig, axs = plt.subplots(2)
axs[0].plot(t, vU, color='red', label=f'$v_{INPUT_AXIS}, Unfiltered$')
axs[0].set_ylabel(f'$V_{INPUT_AXIS} \ (m/s)$')
axs[0].yaxis.set_label_position("right")
axs[0].legend()
axs[1].plot(t, vS, color='green', label=f'$v_{INPUT_AXIS}, Filtered$')
axs[1].set_xlabel('time (s)')
axs[1].set_ylabel(f'$V_{INPUT_AXIS} \ (m/s)$')
axs[1].yaxis.set_label_position("right")
axs[1].legend()
fig.suptitle(f'{INPUT_AXIS_T} Velocity Changes Over Time')
plt.savefig(COMBO_VELO)
plt.close()

fig, axs = plt.subplots(2)
axs[0].plot(t, dU, color='red', label=f'$s_{INPUT_AXIS}, Unfiltered$')
axs[0].set_ylabel(f'$s_{INPUT_AXIS} \ (m)$')
axs[0].yaxis.set_label_position("right")
axs[0].legend()
axs[1].plot(t, dS, color='green', label=f'$s_{INPUT_AXIS}, Filtered$')
axs[1].set_xlabel('time (s)')
axs[1].set_ylabel(f'$s_{INPUT_AXIS} \ (m)$')
axs[1].yaxis.set_label_position("right")
axs[1].legend()
fig.suptitle(f'{INPUT_AXIS_T} Displacement Changes Over Time')
plt.savefig(COMBO_DISP)
plt.close()

fig, axs = plt.subplots(2)
axs[0].plot(t, fU, color='red', label=f'$F_{INPUT_AXIS}, Unfiltered$')
axs[0].set_ylabel(f'$F_{INPUT_AXIS} \ (N)$')
axs[0].yaxis.set_label_position("right")
axs[0].legend()
axs[1].plot(t, fS, color='green', label=f'$F_{INPUT_AXIS}, Filtered$')
axs[1].set_xlabel('time (s)')
axs[1].set_ylabel(f'$F_{INPUT_AXIS} \ (N)$')
axs[1].yaxis.set_label_position("right")
axs[1].legend()
fig.suptitle(f'{INPUT_AXIS_T} Force Changes Over Time')
plt.savefig(COMBO_FORCE)
plt.close()

fig, axs = plt.subplots(2)
axs[0].plot(dfU1, dfU2, color='red', label='Unfiltered')
axs[0].set_ylabel(f'$F_{INPUT_AXIS} \ (N)$')
axs[0].yaxis.set_label_position("right")
axs[0].legend()
axs[1].plot(dfS1, dfS2, color='green', label='Filtered')
axs[1].set_xlabel(f'$s_{INPUT_AXIS} \ (m)$')
axs[1].set_ylabel(f'$F_{INPUT_AXIS} \ (N)$')
axs[1].yaxis.set_label_position("right")
axs[1].legend()
fig.suptitle(f'{INPUT_AXIS_T} Force Changes Over Displacement')
plt.savefig(COMBO_DIFO)
plt.close()