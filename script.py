import os
path=os.getcwd()+"\generate_abnormal_trace.py"
new_path=os.getcwd()+"\\new_generate_abnormal_trace.py"
number=100
ori=open(path, 'r+').readlines()
plc_index=4
for i in range(0,number):
    line1="from plc import plc"+str(plc_index)+"_"+str(i)+" as plc"+str(plc_index)+'\n'
    line2="path='data/plc"+str(plc_index)+"_"+str(i)+".npy'"+'\n'
    ori[1]=line1
    ori[8]=line2
    with open(new_path, 'r+') as f:
        for j in range(0,len(ori)):
            f.write(ori[j])
    f.close()
    os.system("python new_generate_abnormal_trace.py")
    # print (line1)
    # print (line2)