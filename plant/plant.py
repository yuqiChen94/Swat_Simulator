from device.device import *
def resume_from_path(log_path):
    pass
class plant:
    def __init__(self, log_path, time_interval, maxstep):
        self.log_path=log_path
        self.time_interval=time_interval
        self.maxstep=maxstep
        if self.log_path=="":
            init=[505,890,900,200,200]


            self.result = [[0 for x in range(5)] for x in range(maxstep + 1)]
            self.result[0] = init
        else:
            # init=[505,890,900,200,200]
            # self.result = [[0 for x in range(5)] for x in range(maxstep + 1)]
            # self.result[0] = init
            resume_from_path(self.log_path)


    def Actuator(self, P1, P2, P3, P4, P5, P6): #
        P1.MV101.DI_ZSO = P1.MV101.DO_Open
        P1.MV101.DI_ZSC = P1.MV101.DO_Close
        P2.MV201.DI_ZSO = P2.MV201.DO_Open
        P2.MV201.DI_ZSC = P2.MV201.DO_Close
        P3.MV301.DI_ZSO = P3.MV301.DO_Open
        P3.MV301.DI_ZSC = P3.MV301.DO_Close
        P3.MV302.DI_ZSO = P3.MV302.DO_Open
        P3.MV302.DI_ZSC = P3.MV302.DO_Close
        P3.MV303.DI_ZSO = P3.MV303.DO_Open
        P3.MV303.DI_ZSC = P3.MV303.DO_Close
        P3.MV304.DI_ZSO = P3.MV304.DO_Open
        P3.MV304.DI_ZSC = P3.MV304.DO_Close
        P5.MV501.DI_ZSO = P5.MV501.DO_Open
        P5.MV501.DI_ZSC = P5.MV501.DO_Close
        P5.MV502.DI_ZSO = P5.MV502.DO_Open
        P5.MV502.DI_ZSC = P5.MV502.DO_Close
        P5.MV503.DI_ZSO = P5.MV503.DO_Open
        P5.MV503.DI_ZSC = P5.MV503.DO_Close
        P5.MV504.DI_ZSO = P5.MV504.DO_Open
        P5.MV504.DI_ZSC = P5.MV504.DO_Close

        P1.P101.DI_Run = P1.P101.DO_Start
        P1.P102.DI_Run = P1.P102.DO_Start
        P3.P301.DI_Run = P3.P301.DO_Start
        P3.P302.DI_Run = P3.P302.DO_Start
        P4.P401.DI_Run = P4.P401.DO_Start
        P4.P402.DI_Run = P4.P402.DO_Start
        P5.P501.DI_Run = P5.P501_VSD_Out.Start or not P5.P501_VSD_Out.Stop
        P5.P502.DI_Run = P5.P502_VSD_Out.Start or not P5.P502_VSD_Out.Stop
        P6.P601.DI_Run = P6.P601.DO_Start
        P6.P602.DI_Run = P6.P602.DO_Start

    def Plant(self, P1, P2, P3, P4, P5, P6,k,HMI):
        self.h_t101=0
        self.h_t301=0
        self.h_t401=0
        self.h_t601=0
        self.h_t602=0
        self.p = {"f_mv101":2.3*1000000000/3600,"S_t101":1.5*1000000,"S_t301":1.5*1000000,"S_t401":1.5*1000000,"S_t601":1.5*1000000,"S_t601":1.5*1000000,"S_t602":1.5*1000000,"f_p101":2.0*1000000000/3600,"f_mv201":2.0*1000000000/3600,"f_p301":2.0*1000000000/3600,"f_mv302":2.0*1000000000/3600,"f_p602":2.0*1000000000/3600,"f_p401":2.0*1000000000/36001,"f_mv501":2.0*1000000000/3600,"f_mv502":0.00006111,"f_mv503":0.00049,"f_p601":2.0*1000000000/36001,"LIT101_AL":0.2,"LIT101_AH":0.8,"LIT301_AL":0.2,"LIT301_AH":0.8,"LIT401_AL":0.2,"LIT401_AH":0.8,"LIT601_AL":0.2,"LIT601_AH":0.8,"LIT602_AL":0.2,"LIT602_AH":0.8,"cond_AIT201_AL":250,"cond_AIT201_AH":260,"ph_AIT202_AL":6.95,"ph_AIT202_AH":7.05,"orp_AIT203_AL":420,"orp_AIT203_AH":500,"cond_AIT503_AH":260,"h201_AL":50,"h202_AL":4,"h203_AL":15,"cond_AIT503_AL":250,"cond_AIT503_AH":260,"orp_AIT402_AL":420,"orp_AIT402_AH":500,"omega_inlet":0.001}  # critical plant parameters


        if P1.MV101.DI_ZSO == 1:
            self.h_t101=self.h_t101+self.p['f_mv101'] / self.p['S_t101']
        if P1.P101.DI_Run == 1 or P1.P102.DI_Run == 1: #P101, drawing water from tank101
            self.h_t101=self.h_t101-self.p['f_p101'] / self.p['S_t101']

        if P2.MV201.DI_ZSO == 1 and P1.P101.DI_Run == 1:#mv201, feeding water to tank301
            self.h_t301=self.h_t301+self.p['f_mv201'] / self.p['S_t301']

        if P3.P301.DI_Run == 1 or P3.P302.DI_Run == 1: #p301, drawing water from tank301
            self.h_t301=self.h_t301-self.p['f_p301'] / self.p['S_t301']


        if P3.P301.DI_Run == 1 or P3.P302.DI_Run == 1 and P3.MV301.DI_ZSC and  P3.MV302.DI_ZSC and P3.MV303.DI_ZSC and P3.MV304.DO_ZSO and P6.P602.DI_Run == 0: #UF flushing procedure, 30 sec
            pass
        if P3.P301.DI_Run == 1 or P3.P302.DI_Run == 1 and P3.MV301.DI_ZSC == 1 and  P3.MV302.DI_ZSO == 1 and P3.MV303.DI_ZSC == 1 and P3.MV304.DI_ZSC == 1 and P6.P602.DI_Run == 0:   #UF ultra filtration procedure, 30 min
            self.h_t401=self.h_t401+ self.p['f_mv302'] / self.p['S_t401']

        if P3.P301.DI_Run == 0 and P3.P302.DI_Run == 0 and P3.MV301.DI_ZSO == 1 and  P3.MV302.DI_ZSC == 1 and P3.MV303.DI_ZSO == 1 and P3.MV304.DI_ZSC == 1 and P6.P602.DI_Run == 1:   #UF back wash procedure, 45 sec
            self.h_t602=self.h_t602- self.p['f_p602'] / self.p['S_t602']
        if P3.P301.DI_Run == 0 and P3.P302.DI_Run == 0 and P3.MV301.DI_ZSC == 1 and  P3.MV302.DI_ZSC == 1 and P3.MV303.DI_ZSC == 1 and P3.MV304.DI_ZSO == 1 and P6.P602.DI_Run == 0:   #UF feed tank draining procedure, 1 min
            pass

        if P4.P401.DI_Run == 1 or P4.P402.DI_Run == 1: #P401, drawing water from t401
            self.h_t401=self.h_t401- self.p['f_p401'] / self.p['S_t401']

        if P4.P401.DI_Run == 1 or P4.P402.DI_Run == 1 and P5.P501.DI_Run == 1 or P5.P502.DI_Run == 1 and P5.MV501.DI_ZSO == 1 and P5.MV502.DI_ZSO == 1 and P5.MV503.DI_ZSC == 1 and P5.MV504.DI_ZSC == 1:#procedure for RO normal functioning with product of permeate 60% and backwash 40%
            self.h_t601=self.h_t601+self.p['f_mv501'] / self.p['S_t601']
            self.h_t602=self.h_t602+self.p['f_mv502'] / self.p['S_t602']
        elif P4.P401.DI_Run == 1 or P4.P402.DI_Run == 1 and P5.P501.DI_Run == 1 or P5.P502.DI_Run == 1 and P5.MV501.DI_ZSC == 1 and P5.MV502.DI_ZSC == 1 and P5.MV503.DI_ZSO == 1 and P5.MV504.DI_ZSO == 1:#procedure for RO flushing with product of backwash 60% and drain 40%
            self.h_t602=self.h_t602+self.p['f_mv503'] / self.p['S_t602']
        if P6.P601.DI_Run == 1: # Pumping water out of tank601
            self.h_t601=self.h_t601-self.p['f_p601'] / self.p['S_t601']

        HMI.LIT101.Pv=self.result[k][0]
        HMI.LIT101.set_alarm()
        HMI.LIT301.Pv=self.result[k][1]
        HMI.LIT301.set_alarm()
        HMI.LIT401.Pv=self.result[k][2]
        HMI.LIT401.set_alarm()

        # print ( HMI.LIT101.Pv)
        # print ( HMI.LIT301.Pv)
        # print ( HMI.LIT401.Pv)
        if self.result[k][3]>700:
            HMI.LSH601.Alarm =True
        if self.result[k][3]<200:
            HMI.LSL601.Alarm =True

        if self.result[k][4]>700:
            HMI.LSH601.Alarm =True
        if self.result[k][4]<200:
            HMI.LSL601.Alarm =True


        self.result[k + 1][0] =self.result[k][0]+self.h_t101*self.time_interval
        self.result[k + 1][1] = self.result[k][1] + self.h_t301 * self.time_interval
        self.result[k + 1][2] = self.result[k][2] + self.h_t401 * self.time_interval
        self.result[k + 1][3] = self.result[k][3] + self.h_t601 * self.time_interval
        self.result[k + 1][4] = self.result[k][4] + self.h_t602 * self.time_interval


        print (self.result[k][0:3])

