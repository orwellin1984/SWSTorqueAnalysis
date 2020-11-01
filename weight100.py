import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os


# ----------------------Data clean function1 ---------------
def cleanError(torque):
    for index in range(0, len(torque)):
        if torque[index] <= 1.5:
            torque[index] = 0.1
        else:
            pass


# ----------------------Data clean function2 ---------------
def cleanZero(torque):
    length = len(torque)
    x = 0
    while x < length:
        if torque[x] <= 0.1:
            torque.remove(torque[x])
            x -= 1
            length -= 1
        x += 1


# --------------Input The Data Location-----------------------
path = '/home/ling/Documents/pythonProject/SWSTorqueData/Data'
os.chdir(path)
# --------------Load The original Data---------------------------------
Data_pt1 = pd.read_csv('20201007-145302.csv', header=0)
Data_pt2 = pd.read_csv('20201007-145604.csv', header=0)
Data_pt3 = pd.read_csv('20201007-145822.csv', header=0)
Data_pt4 = pd.read_csv('20201007-150105.csv', header=0)
# ---------------------Data Separately-----------------------------
Data_pt1 = pd.DataFrame(Data_pt1)
Data_25 = Data_pt1[0:950]
Data_50 = Data_pt1[950: len(Data_pt1)]
torque_25 = list(Data_25['計測値'])
torque_50 = list(Data_50['計測値'])
cleanError(torque_25)
cleanZero(torque_25)
cleanError(torque_50)
cleanZero(torque_50)

Data_pt2 = pd.DataFrame(Data_pt2)

Data_pt2 = pd.DataFrame(Data_pt2)
Data_75 = Data_pt2[0:1150]
Data_100 = Data_pt2[1150: len(Data_pt2)]
torque_75 = list(Data_75['計測値'])
torque_100 = list(Data_100['計測値'])
cleanError(torque_75)
cleanZero(torque_75)
cleanError(torque_100)
cleanZero(torque_100)


Data_pt3 = pd.DataFrame(Data_pt3)
Data_125 = Data_pt3[0:915]
Data_150 = Data_pt3[915: len(Data_pt3)]
torque_125 = list(Data_125['計測値'])
torque_150 = list(Data_150['計測値'])
cleanError(torque_125)
cleanZero(torque_125)
cleanError(torque_150)
cleanZero(torque_150)


Data_pt4 = pd.DataFrame(Data_pt4)
Data_175 = Data_pt4[0:950]
Data_200 = Data_pt4[950: len(Data_pt4)]
torque_175 = list(Data_175['計測値'])
torque_200 = list(Data_200['計測値'])
cleanError(torque_175)
cleanZero(torque_175)
cleanError(torque_200)
cleanZero(torque_200)

# ----------------------create the X Axle-------------------------------
xnp25 = np.array(range(0, len(torque_25))) * (0.25 / len(torque_25))
xnp50 = np.array(range(0, len(torque_50))) * (0.25 / len(torque_50)) + 0.25
xnp75 = np.array(range(0, len(torque_75))) * (0.25 / len(torque_75)) + 0.5
xnp100 = np.array(range(0, len(torque_100))) * (0.25 / len(torque_100)) + 0.75
xnp125 = np.array(range(0, len(torque_125))) * (0.25 / len(torque_125)) + 1.0
xnp150 = np.array(range(0, len(torque_150))) * (0.25 / len(torque_150)) + 1.25
xnp175 = np.array(range(0, len(torque_175))) * (0.25 / len(torque_175)) + 1.50
xnp200 = np.array(range(0, len(torque_200))) * (0.25 / len(torque_200)) + 1.75

# -------------------------Draw the plot---------------------------------
plt.plot(xnp25, torque_25, linewidth='0.5', label='0~25 cm')
plt.plot(xnp50, torque_50, linewidth='0.5', label='25~50 cm')
plt.plot(xnp75, torque_75, linewidth='0.5', label='25~75 cm')
plt.plot(xnp100, torque_100, linewidth='0.5', label='75~100 cm')
plt.plot(xnp125, torque_125, linewidth='0.5', label='100~125 cm')
plt.plot(xnp150, torque_150, linewidth='0.5', label='125~150 cm')
plt.plot(xnp175, torque_175, linewidth='0.5', label='150~175 cm')
plt.plot(xnp200, torque_200, linewidth='0.5', label='175~200 cm')

# plt.xticks(np.arange(0, 2.1, 0.1))

plt.xlabel('m')
plt.ylabel('N/m')


plt.legend()
plt.show()
