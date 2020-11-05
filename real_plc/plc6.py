#this is the PLC 6 logic, it's about the very same thing as that in the real plc.
from logicblock.logicblock import SETD
from logicblock.logicblock import TONR
from controlblock.controlblock import *

class plc6:
	'plc6 logic'

	def __init__(self,HMI):
		self.Mid_P601_AutoInp = HMI.P601.Status-1
		self.Mid_P_PERMEATE_SR = self.Mid_P601_AutoInp
		self.Mid_P602_AutoInp = HMI.Mid_P602_AutoInp
		self.Mid_P603_AutoInp = HMI.P603.Status-1


		self.LSL601_FB = SWITCH_FBD(HMI.LSL601)
		self.LSL602_FB = SWITCH_FBD(HMI.LSL602)
		self.LSL603_FB = SWITCH_FBD(HMI.LSL603)
		self.LSH601_FB = SWITCH_FBD(HMI.LSH601)
		self.LSH602_FB = SWITCH_FBD(HMI.LSH602)
		self.LSH603_FB = SWITCH_FBD(HMI.LSH603)
		self.P601 = PMP_FBD(HMI.P601)
		self.P602 = PMP_FBD(HMI.P602)
		self.P603 = PMP_FBD(HMI.P603)
		# print ("	PLC6 Started\n")


	def Pre_Main_Product(self,IO,HMI):
#	def Pre_Condition(self):
		if HMI.PLANT.Reset_On:
			HMI.P601.Reset	=1
			HMI.P602.Reset	=1
			HMI.P603.Reset	=1							
		if HMI.PLANT.Auto_On:
			HMI.P601.Auto	=1
			HMI.P602.Auto	=1
			HMI.P603.Auto	=1

		if HMI.PLANT.Auto_Off:
			HMI.P601.Auto	=0
			HMI.P602.Auto	=0
			HMI.P603.Auto	=0

		HMI.P6.Permissive_On= HMI.P601.Avl and HMI.P602.Avl

		self.Mid_FIT601_Tot_Enb	= HMI.P602.Status==2

		HMI.P601.Permissive[0] 	= not HMI.LSL601.Alarm

		HMI.P601.MSG_Permissive[0] = HMI.P601.Permissive[0]

		HMI.P602.Permissive[0] 	= not HMI.LSL602.Alarm

		HMI.P602.MSG_Permissive[0] = HMI.P602.Permissive[0]

		HMI.P603.Permissive[0] 	= not HMI.LSL603.Alarm

		HMI.P603.MSG_Permissive[0] = HMI.P603.Permissive[0]

		HMI.P601.SD[0] 	= HMI.LSL601.Alarm

		HMI.P601.MSG_Shutdown[1] = HMI.P601.Shutdown[0]
		HMI.P601.MSG_Shutdown[2] = HMI.P601.Shutdown[1]
		HMI.P601.MSG_Shutdown[3] = HMI.P601.Shutdown[2] 
		HMI.P601.MSG_Shutdown[4] = HMI.P601.Shutdown[3] 
		HMI.P601.MSG_Shutdown[5] = HMI.P601.Shutdown[4] 

		HMI.P602.SD[0] 	= 0

		HMI.P602.MSG_Shutdown[1] = HMI.P602.Shutdown[0]
		HMI.P602.MSG_Shutdown[2] = HMI.P602.Shutdown[1]
		HMI.P602.MSG_Shutdown[3] = HMI.P602.Shutdown[2] 
		HMI.P602.MSG_Shutdown[4] = HMI.P602.Shutdown[3] 
		HMI.P602.MSG_Shutdown[5] = HMI.P602.Shutdown[4] 

		HMI.P603.SD[0] 	= HMI.LSL603.Alarm

		HMI.P603.MSG_Shutdown[1] = HMI.P603.Shutdown[0] 
		HMI.P603.MSG_Shutdown[2] = HMI.P603.Shutdown[1] 
		HMI.P603.MSG_Shutdown[3] = HMI.P603.Shutdown[2] 
		HMI.P603.MSG_Shutdown[4] = HMI.P603.Shutdown[3] 
		HMI.P603.MSG_Shutdown[5] = HMI.P603.Shutdown[4] 
#Main
		if HMI.PLANT.Stop or HMI.PLANT.Critical_SD_On:
			HMI.P6.State=1

		#self.Mid_P602_AutoInp = P6_P602_AutoInp.On

		if HMI.P6.State == 1:
			self.Mid_P601_AutoInp	= 0 
			self.Mid_P602_AutoInp	= 0 
			self.Mid_P603_AutoInp	= 0

			if HMI.P6.Permissive_On and HMI.PLANT.Start:
				HMI.P6.State = 2
			 
		elif HMI.P6.State == 2:
			self.Mid_P_PERMEATE_SR = SETD(HMI.LSH601.Alarm and HMI.AIT202.Pv >= 7 and not HMI.LIT101.AHH and 0 ,HMI.LIT101.AHH or HMI.LSL601.Alarm or HMI.AIT202.Pv < 7,self.Mid_P_PERMEATE_SR)
			self.Mid_P601_AutoInp	= self.Mid_P_PERMEATE_SR 

			self.Mid_P602_AutoInp	= HMI.Mid_P602_AutoInp #(*SIGNAL FROM P3, UF*)
			self.Mid_P603_AutoInp	= HMI.Mid_P603_AutoInp #(*SIGNAL FROM P5, RO*)

		else:
			HMI.P6.State=1

#Product
		self.LSL601_FB.SWITCH_FBD(IO.LSL601,HMI.LSL601)
		self.LSL602_FB.SWITCH_FBD(IO.LSL602,HMI.LSL602)
		self.LSL603_FB.SWITCH_FBD(IO.LSL603,HMI.LSL603)
		self.LSH601_FB.SWITCH_FBD(IO.LSH601,HMI.LSH601)
		self.LSH602_FB.SWITCH_FBD(IO.LSH602,HMI.LSH602)
		self.LSH603_FB.SWITCH_FBD(IO.LSH603,HMI.LSH603)
		self.P601.PMP_FBD(self.Mid_P601_AutoInp, IO.P601,HMI.P601)
		self.P602.PMP_FBD(self.Mid_P602_AutoInp, IO.P602,HMI.P602)
		self.P603.PMP_FBD(self.Mid_P603_AutoInp, IO.P603,HMI.P603)






