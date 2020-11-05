import numpy as np
import os

def normal_data_process(normal_path,interval):
    normal_vector=[]
    normal_data_set = np.load(normal_path, allow_pickle=True).tolist()
    for i in range(0,len(normal_data_set)-interval):
        vector=normal_data_set[i]+normal_data_set[i+interval]
        normal_vector.append(vector)
    return normal_vector

def data_process(data_path,normal_path,interval):
    normal_data_set=normal_data_process(normal_path,interval)
    abnormal_vector = []
    files = os.listdir(data_path)
    for file in files:
        path = data_path + '/' + file
        if path != normal_path:
            abnormal_data_set = np.load(path, allow_pickle=True).tolist()
            for i in range(0, len(abnormal_data_set) - interval):
                vector = abnormal_data_set[i] + abnormal_data_set[i + interval]
                abnormal_vector.append(vector)
    return normal_data_set,abnormal_vector

def undersample(normal_data_set,abnormal_data_set):
    new_set=[]
    t=round(len(abnormal_data_set)/len(normal_data_set))
    for i in range(0,len(abnormal_data_set)):
        if i%t==0:
            new_set.append(abnormal_data_set[i])

    return new_set

def label(normal_data_set,abnormal_data_set):
    x_path="training_data/x.npy"
    y_path="training_data/y.npy"
    y=[]
    for i in range(0,len(normal_data_set)):
        y.append(1)
    for i in range(0,len(abnormal_data_set)):
        y.append(0)

    x = np.array(normal_data_set+abnormal_data_set)
    y = np.array(y)
    print (x.shape)
    print (y.shape)

    x.dump(x_path)
    y.dump(y_path)


interval=100
normal_path="data/normal.npy"
data_path="data"
normal_data_set_path="training_data/normal.npy"
abnormal_data_set_path="training_data/abnormal.npy"
normal_data_set,abnormal_data_set=data_process(data_path,normal_path,interval)
new_abnormal_data_set=undersample(normal_data_set,abnormal_data_set)

label(normal_data_set,new_abnormal_data_set)

normal_data_set = np.array(normal_data_set)
normal_data_set.dump(normal_data_set_path)

new_abnormal_data_set = np.array(new_abnormal_data_set)
new_abnormal_data_set.dump(abnormal_data_set_path)