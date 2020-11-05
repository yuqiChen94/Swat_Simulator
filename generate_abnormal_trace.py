from plc import plc1,plc2,plc3,plc4,plc5,plc6
from plc import plc3_0 as plc3
import sys,os
sys.path.insert(0,os.getcwd())
from SCADA import H
from IO import *
from plant.plant import plant
import numpy as np
path='data/plc3_0.npy'
data_set=[]
normal_path="data/normal.npy"
normal_data_set=np.load(normal_path,allow_pickle=True).tolist()
time_interval=1
log_path=''
maxstep = 60*60*10
# Initiating Plant
Plant = plant(log_path, time_interval,maxstep)
# Defining I/O
IO_DI_WIFI = DI_WIFI()
IO_P1 = P1()
IO_P2 = P2()
IO_P3 = P3()
IO_P4 = P4()
IO_P5 = P5()
IO_P6 = P6()
print ("Initializing SCADA HMI")
HMI = H()
print ("Initializing PLCs\n")
PLC1 = plc1.plc1(HMI)
PLC2 = plc2.plc2(HMI)
PLC3 = plc3.plc3(HMI)
PLC4 = plc4.plc4(HMI)
PLC5 = plc5.plc5(HMI)
PLC6 = plc6.plc6(HMI)
print ("Now starting Simulation")

# Main Loop Body
for time in range(0,maxstep):
    Sec_P = True
    Min_P = not bool(time%(60))
    Plant.Actuator(IO_P1,IO_P2,IO_P3,IO_P4,IO_P5,IO_P6)
    Plant.Plant(IO_P1,IO_P2,IO_P3,IO_P4,IO_P5,IO_P6,time,HMI)
# #PLC working
    PLC1.Pre_Main_Raw_Water(IO_P1,HMI)
    PLC2.Pre_Main_UF_Feed_Dosing(IO_P2,HMI)
    PLC3.Pre_Main_UF_Feed(IO_P3,HMI,Sec_P,Min_P)
    PLC4.Pre_Main_RO_Feed_Dosing(IO_P4,HMI,)
    PLC5.Pre_Main_High_Pressure_RO(IO_P5,HMI,Sec_P,Min_P)
    PLC6.Pre_Main_Product(IO_P6,HMI)

for i in range(0,maxstep):
    if Plant.result[i][0:3]!=normal_data_set[i]:
        data_set.append(Plant.result[i][0:3])




data_set = np.array(data_set)
data_set.dump(path)
# normal_data_set=np.load(normal_path,allow_pickle=True).tolist()
#
# if normal_data_set==data_set:
#     print ("same")
# else:

