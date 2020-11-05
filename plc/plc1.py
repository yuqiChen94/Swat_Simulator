#this is the PLC 1 logic, it's about the very same thing as that in the real plc.
from logicblock.logicblock import SETD
from logicblock.logicblock import TONR
from controlblock.controlblock import *

class plc1:
	'plc1 logic'
	
	def __init__(self,HMI):
		self.P_RAW_WATER_DUTY_FB = Duty2_FBD()
#		print "P_RAW_WATER_DUTY_FB Initialized"
		self.P101_FB = PMP_FBD(HMI.P101)
#		print "P101_FB Initialized" 	
		self.P102_FB = PMP_FBD(HMI.P102)
#		print "P102_FB Initialized" 	
		self.LIT101_FB = AIN_FBD(HMI.LIT101)
		# print HMI.LIT101.SAHH
#		print "LIT101_FB Initialized"
		self.MV101_FB = MV_FBD(HMI.MV101)
#		print "MV101_FB Initialized"
		self.FIT101_FB = FIT_FBD(HMI.FIT101)
#		print "FIT101_FB Initialized"
#		print "All Phase 1 Function Blocks Initialized Successufully\n"
		self.TON_FIT102_P1_TM = TONR(10)		
		self.TON_FIT102_P2_TM = TONR(10)
		self.Mid_MV101_AutoInp = HMI.MV101.Status-1
		self.Mid_P_RAW_WATER_DUTY_AutoInp=HMI.P101.Status-1
		#Initialization
		self.Mid_FIT101_Flow_Hty = 1
		self.Mid_P_RAW_WATER_DUTY_AutoInp = 1
		self.Min_Test = 0
		# print ("	PLC1 started\n")
	def Pre_Main_Raw_Water(self,IO,HMI):
		if HMI.PLANT.Reset_On:
			HMI.MV101.Reset = 1
			HMI.P101.Reset 	= 1
			HMI.P102.Reset 	= 1
		if HMI.PLANT.Auto_On:
			HMI.MV101.Auto 	= 1
			HMI.P101.Auto 	= 1
			HMI.P102.Auto 	= 1
		if HMI.PLANT.Auto_Off:
			HMI.MV101.Auto = 0
			HMI.P101.Auto  = 0
			HMI.P102.Auto  = 0
		HMI.P1.Permissive_On = HMI.MV101.Avl and (HMI.P101.Avl or HMI.P102.Avl)
		HMI.PLANT.Ready = HMI.P1.Permissive_On and HMI.P2.Permissive_On and HMI.P3.Permissive_On and HMI.P4.Permissive_On
		# self.TON_FIT102_P1_TM = TONR(10)
		# self.TON_FIT102_P2_TM = TONR(10)
# The above two timers are initialized in __init__ due to limitations of python		
		HMI.P101.Permissive[0] = HMI.LIT101.Hty and not HMI.LIT101.ALL
		HMI.P101.Permissive[1] = HMI.MV201.Status == 2
#		for i in (2,len(HMI_P101.Permissive)):  # The assigning of all other bits are done in initializing in HMI.py, so not so necessary here.
#			HMI_P101.Permissive[i] = 1
		HMI.P101.MSG_Permissive[1] = HMI.P101.Permissive[0]
		HMI.P101.MSG_Permissive[2] = HMI.P101.Permissive[1]
#		for i in (3,len(HMI_P101.MSG_Permissive)):
#			HMI_P101.MSG_Permissive[i] = 0
		HMI.P102.Permissive[0] = HMI.LIT101.Hty and not HMI.LIT101.ALL
		HMI.P102.Permissive[1] = (HMI.MV201.Status == 2)
#		for i in (2,len(HMI_P102.Permissive)):
#			HMI_P101.Permissive[i] = 1
		HMI.P102.MSG_Permissive[1] = HMI.P102.Permissive[0]
		HMI.P102.MSG_Permissive[2] = HMI.P102.Permissive[1]
#		for i in (3,len(HMI_P102.MSG_Permissive)):
#			HMI_P101.MSG_Permissive[i] = 0
		HMI.P101.SD[0] = HMI.LIT101.Hty and HMI.LIT101.ALL
		HMI.P101.SD[1] = HMI.P101.Status == 2 and HMI.MV201.Status != 2
		HMI.P101.SD[2] = self.TON_FIT102_P1_TM.DN
		if HMI.P101.SD[2]:
			print ("timeout")
		HMI.P101.MSG_Shutdown[1] = HMI.P101.Shutdown[0] 
		HMI.P101.MSG_Shutdown[2] = HMI.P101.Shutdown[1]
		HMI.P101.MSG_Shutdown[3] = HMI.P101.Shutdown[2]

		HMI.P102.SD[0] = HMI.LIT101.Hty and HMI.LIT101.ALL
		HMI.P102.SD[1] = HMI.P102.Status == 2 and HMI.MV201.Status != 2
		HMI.P102.SD[2] = self.TON_FIT102_P2_TM.DN
		
		HMI.P102.MSG_Shutdown[1] = HMI.P102.Shutdown[0] 
		HMI.P102.MSG_Shutdown[2] = HMI.P102.Shutdown[1]
		HMI.P102.MSG_Shutdown[3] = HMI.P102.Shutdown[2]


		
	#def Main_Seq(self,Min_P):
		# if Min_P:
		# 	self.Min_Test += 1
		if HMI.PLANT.Stop:
			HMI.P1.Shutdown = 1


		if HMI.P1.State == 1:
			self.Mid_MV101_AutoInp = 0
			self.Mid_P_RAW_WATER_DUTY_AutoInp = 0
			HMI.P1.Ready = 0
			if HMI.PLANT.Ready and HMI.PLANT.Start and HMI.P1.Permissive_On:
				HMI.P1.State = 2


		elif HMI.P1.State == 2:
			self.Mid_MV101_AutoInp = SETD(HMI.LIT101.AL, HMI.LIT101.AH, self.Mid_MV101_AutoInp)
			self.Mid_P_RAW_WATER_DUTY_AutoInp = SETD(HMI.MV201.Status == 2 and HMI.LIT301.AL, HMI.MV201.Status != 2 or HMI.LIT301.AH, self.Mid_P_RAW_WATER_DUTY_AutoInp)
			if HMI.P1.Shutdown:
				HMI.P1.State=3
				HMI.P1.Shutdown=0

		elif HMI.P1.State == 3:
			self.Mid_MV101_AutoInp = SETD(HMI.LIT101.AL, HMI.LIT101.AH, self.Mid_MV101_AutoInp)
			self.Mid_P_RAW_WATER_DUTY_AutoInp = SETD(HMI.MV201.Status == 2 and HMI.LIT301.AL,
													 HMI.MV201.Status != 2 or HMI.LIT301.AH,
													 self.Mid_P_RAW_WATER_DUTY_AutoInp)

			if HMI.LIT101.AH and HMI.LIT301.AH:
				self.Mid_MV101_AutoInp=0
				self.Mid_P_RAW_WATER_DUTY_AutoInp=0
				HMI.P1.State=2

			if HMI.P1.Shutdown:
				HMI.P1.State = 1
				HMI.P1.Shutdown = 0


#	def Raw_Water(self,Min_P,Sec_P):
		self.MV101_FB.MV_FBD(self.Mid_MV101_AutoInp, IO.MV101, HMI.MV101)
		self.P_RAW_WATER_DUTY_FB.Duty2_FBD(self.Mid_P_RAW_WATER_DUTY_AutoInp, HMI.P101, HMI.P102, HMI.P_RAW_WATER_DUTY)
		self.P101_FB.PMP_FBD(self.P_RAW_WATER_DUTY_FB.Start_Pmp1, IO.P101, HMI.P101)
		self.P102_FB.PMP_FBD(self.P_RAW_WATER_DUTY_FB.Start_Pmp2, IO.P102, HMI.P102)
		
