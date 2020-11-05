from mutation_operator import*
import os
path=os.getcwd()+"/plc/plc3.py"
number=5
i=0
while i<number:
    ran_no=random.randrange(0,5)
    if (ran_no==0):
        test = operator(path)
        test.operator_ABS()
        if (test.gen(i)==True):
            i+=1
    if (ran_no==1):
        test = operator(path)
        test.operator_AOR()
        if (test.gen(i)==True):
            i+=1
    if (ran_no==2):
        test = operator(path)
        test.operator_COR()
        if (test.gen(i)==True):
            i+=1
    if (ran_no==3):
        test = operator(path)
        test.operator_ASR()
        if (test.gen(i)==True):
            i+=1
    if (ran_no==4):
        test = operator(path)
        test.operator_ROR()
        if (test.gen(i)==True):
            i+=1
