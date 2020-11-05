import random
import os
class operator:
    path_list=os.getcwd()+"\plc\plc6_list.txt"
    line_no=0
    check=0
    ori=[]
    def __init__(self, path):
        self.path = path
        self.ori=open(path, 'rU').readlines()
        self.line_no = random.randrange(0,len(self.ori))
        self.line =self.ori[self.line_no].strip('\n')

    def indices(self, element):
        result = []
        offset = -1
        while True:
            try:
                offset = self.line.index(element, offset + 1)
            except ValueError:
                return result
            result.append(offset)

    def choose(self):
        print (self.line)
    def operator_ABS(self):
        numlist=['0','1','2','3','4','5','6','7','8','9']
        result = []
        i=[]
        # print self.line
        for num in numlist:
            result.append(self.indices(num))
        for j in range(0,len(numlist)):
            if result[j]!=[]:
                i.append(j)
        #     print j
        # print i
        if i!=[]:
            numpos=i[random.randrange(0, len(i))]
            numresult= result[numpos]
            cpos=numresult[random.randrange(0, len(numresult))]
            # print "numpos",numpos
            # print numresult
            # print cpos
            newlist = numlist
            del newlist[numpos]
            choosenum = newlist[random.randrange(0, len(newlist))]
            newline=self.line[0:cpos]+choosenum+self.line[cpos+1:]
            self.check=1
            print (newline)
            print (self.line)
            self.line = newline
        else:
            self.check = 0
            print ("error")

    def operator_AOR(self):
        Aolist=['+','-','*','/','%']
        result = []
        i=[]
        # print self.line
        for op in Aolist:
            result.append(self.indices(op))
        for j in range(0,len(Aolist)):
            if result[j]!=[]:
                i.append(j)
        #     print j
        # print i
        if i!=[]:
            oppos=i[random.randrange(0, len(i))]
            opresult= result[oppos]
            cpos=opresult[random.randrange(0, len(opresult))]
            # print "oppos",oppos
            # print opresult
            # print cpos
            newlist = Aolist
            del newlist[oppos]
            chooseop = newlist[random.randrange(0, len(newlist))]
            newline=self.line[0:cpos]+chooseop+self.line[cpos+1:]
            print (newline)
            print (self.line)
            self.line=newline
            self.check = 1
        else:
            print ("error")

    def operator_ASR(self):
        Asolist = ['+=', '-=', '*=', '/=', '%=']
        result = []
        i = []
        # print self.line
        for op in Asolist:
            result.append(self.indices(op))
        for j in range(0, len(Asolist)):
            if result[j] != []:
                i.append(j)
        # print j
        # print i
        if i != []:
            oppos = i[random.randrange(0, len(i))]
            opresult = result[oppos]
            cpos = opresult[random.randrange(0, len(opresult))]
            # print "oppos",oppos
            # print opresult
            # print cpos
            newlist = Asolist
            del newlist[oppos]
            chooseop = newlist[random.randrange(0, len(newlist))]
            newline = self.line[0:cpos] + chooseop + self.line[cpos + 1:]
            print (newline)
            print (self.line)
            self.line = newline
            self.check = 1
        else:
            print ("error")

    def operator_ROR(self):
        Asolist = ['>', '<', '>=', '<=', '==','!=','<>']
        result = []
        i = []
        # print self.line
        for op in Asolist:
            result.append(self.indices(op))
        for j in range(0, len(Asolist)):
            if result[j] != []:
                i.append(j)
        # print j
        # print i
        if i != []:
            oppos = i[random.randrange(0, len(i))]
            opresult = result[oppos]
            cpos = opresult[random.randrange(0, len(opresult))]
            # print "oppos",oppos
            # print opresult
            # print cpos
            newlist = Asolist
            del newlist[oppos]
            chooseop = newlist[random.randrange(0, len(newlist))]
            newline = self.line[0:cpos] + chooseop + self.line[cpos + 1:]
            print (newline)
            print (self.line)
            self.line = newline
            self.check = 1
        else:
            print ("error")

    def operator_COR(self):
        try:
            cpos = self.line.index('if')
            num = random.randrange(0, 2)
            if num == 0:
                newline = self.line[0:cpos] + 'if True:'
            else:
                newline = self.line[0:cpos] + 'if False:'
            print (self.line)
            print (newline)
            self.line = newline
            self.check = 1
        except:
            print ("error")

    def gen(self,mutantnum):
        if self.check == 1:
            with open(self.path_list, 'a') as f2:
                f2.write("Mutation number:"+str(mutantnum)+"\r\n")
                f2.write(self.ori[self.line_no].strip('\n'))
                f2.write("   >>>>>   ")
                f2.write(self.line)
                f2.write('\n\r')
            path_new=self.path[0:len(self.path)-3]+"_"+str(mutantnum)+".py"
            count1 = len(open(self.path, 'rU').readlines())
            self.ori[self.line_no]=self.line+"\r\n"
            with open(path_new, 'a') as f1:
                for i in range(0,len(self.ori)):
                    f1.write(self.ori[i])
            return True
        else:
            print ("No generation")
            return False





# +,-,*,/