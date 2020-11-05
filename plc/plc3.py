# this is the PLC 3 logic, it's about the very same thing as that in the real plc.
from logicblock.logicblock import *
from controlblock.controlblock import *

class plc3:
	'plc3 logic'

# there could be CIP in the future, but current SWaT system has none
	def __init__(self,HMI):
		self.TON_FIT301_P1_TM = TONR(6,'FIT301_P1')
		self.TON_FIT301_P2_TM = TONR(6,'FIT301_P2')
		self.SEC_TEST = 0
		self.MIN_TEST = 0
		self.Mid_NEXT = 0
		self.Mid_MV301_AutoInp			= HMI.MV301.Status-1
		self.Mid_MV302_AutoInp			= HMI.MV302.Status-1
		self.Mid_MV303_AutoInp			= HMI.MV303.Status-1
		self.Mid_MV304_AutoInp			= HMI.MV304.Status-1
		self.Mid_P_UF_FEED_DUTY_AutoInp	=0
		self.Mid_P602_AutoInp			=HMI.P602.Status-1
		self.Mid_P_NAOCL_UF_DUTY_AutoInp=0

	
		self.LIT301_FB = AIN_FBD(HMI.LIT301)
		self.P_UF_FEED_DUTY_FB = Duty2_FBD()
		self.P301_FB = PMP_FBD(HMI.P301)
		self.P302_FB = PMP_FBD(HMI.P302)
		self.FIT301_FB = FIT_FBD(HMI.FIT301)
		self.PSH301_FB = SWITCH_FBD(HMI.PSH301)
		self.DPSH301_FB = SWITCH_FBD(HMI.DPSH301)
		self.DPIT301_FB = AIN_FBD(HMI.DPIT301)
		self.MV301_FB = MV_FBD(HMI.MV301)
		self.MV302_FB = MV_FBD(HMI.MV302)
		self.MV303_FB = MV_FBD(HMI.MV303)
		self.MV304_FB = MV_FBD(HMI.MV304)

		# print ("	PLC3 Started\n")

	def Pre_Main_UF_Feed(self,IO,HMI,Sec_P,Min_P):
		if HMI.PLANT.Reset_On:
			HMI.MV301.Reset	=1
			HMI.MV302.Reset	=1
			HMI.MV303.Reset	=1
			HMI.MV304.Reset	=1
			HMI.P301.Reset	=1
			HMI.P302.Reset	=1		
		
		if HMI.PLANT.Auto_On:
			HMI.MV301.Auto	=1
			HMI.MV302.Auto	=1
			HMI.MV303.Auto	=1
			HMI.MV304.Auto	=1
			HMI.P301.Auto	=1
			HMI.P302.Auto	=1

		if HMI.PLANT.Auto_Off:
			HMI.MV301.Auto	=0
			HMI.MV302.Auto	=0
			HMI.MV303.Auto	=0
			HMI.MV304.Auto	=0
			HMI.P301.Auto	=0
			HMI.P302.Auto	=0
		

		HMI.P3.Permissive_On 	=  HMI.MV301.Avl and HMI.MV302.Avl and HMI.MV303.Avl and HMI.MV304.Avl and (HMI.P301.Avl or HMI.P302.Avl)

		self.Mid_FIT301_Tot_Enb	= HMI.P301.Status==2 or HMI.P302.Status==2


		self.TON_FIT301_P1_TM.TONR(HMI.FIT301.ALL and HMI.P301.Status == 2)
		# print self.TON_FIT301_P1_TM.name
		self.TON_FIT301_P2_TM.TONR(HMI.FIT301.ALL and HMI.P302.Status == 2)

		HMI.P301.Permissive[0] 	= not HMI.LIT301.ALL
		HMI.P301.Permissive[1] 	= not HMI.LIT401.AHH
		HMI.P301.Permissive[2] 	= HMI.MV302.Status==2 or HMI.MV304.Status==2

		HMI.P301.MSG_Permissive[1] = HMI.P301.Permissive[0]
		HMI.P301.MSG_Permissive[2] = HMI.P301.Permissive[1]
		HMI.P301.MSG_Permissive[3] = HMI.P301.Permissive[2]

		HMI.P302.Permissive[0] 	= not HMI.LIT301.ALL
		HMI.P302.Permissive[1] 	= not HMI.LIT401.AHH
		HMI.P302.Permissive[2] 	= HMI.MV302.Status==2 or HMI.MV304.Status==2

		HMI.P302.MSG_Permissive[1] = HMI.P302.Permissive[0]
		HMI.P302.MSG_Permissive[2] = HMI.P302.Permissive[1]
		HMI.P302.MSG_Permissive[3] = HMI.P302.Permissive[2]

		HMI.P301.SD[0] 	= HMI.LIT301.ALL
		HMI.P301.SD[1] 	= HMI.LIT401.AHH
		HMI.P301.SD[2] 	= HMI.PSH301.Alarm
		HMI.P301.SD[3] 	= 0#(*TOn_FIT301_P1_TM.DN*)
		HMI.P301.SD[4] 	= HMI.P301.Status ==2 and HMI.MV302.Status!=2 and HMI.MV304.Status!=2

		HMI.P301.MSG_Shutdown[1] = HMI.P301.Shutdown[0]
		HMI.P301.MSG_Shutdown[2] = HMI.P301.Shutdown[1] 
		HMI.P301.MSG_Shutdown[3] = HMI.P301.Shutdown[2] 
		HMI.P301.MSG_Shutdown[4] = HMI.P301.Shutdown[3] 
		HMI.P301.MSG_Shutdown[5] = HMI.P301.Shutdown[4] 

		HMI.P302.SD[0] 	= HMI.LIT301.ALL
		HMI.P302.SD[1] 	= HMI.LIT401.AHH
		HMI.P302.SD[2] 	= HMI.PSH301.Alarm
		HMI.P302.SD[3] 	= 0#(*TOn_FIT301_P2_TM.DN*)
		HMI.P302.SD[4] 	= HMI.P302.Status ==2 and HMI.MV302.Status!=2 and HMI.MV304.Status!=2

		HMI.P302.MSG_Shutdown[1] = HMI.P302.Shutdown[0] 
		HMI.P302.MSG_Shutdown[2] = HMI.P302.Shutdown[1] 
		HMI.P302.MSG_Shutdown[3] = HMI.P302.Shutdown[2] 
		HMI.P302.MSG_Shutdown[4] = HMI.P302.Shutdown[3] 
		HMI.P302.MSG_Shutdown[5] = HMI.P302.Shutdown[4]


#	def Main_Seq(self,Sec_P,Min_P):

		# if Sec_P:
		# 	self.SEC_TEST=self.SEC_TEST+1
		#
		# if  Min_P     :
		# 	self.MIN_TEST=self.MIN_TEST+1

		if HMI.PLANT.Stop or HMI.PLANT.Critical_SD_On:
			HMI.P3.Shutdown=1
		
		if HMI.DPIT301.Hty:
			HMI.PLANT.TMP_High= HMI.DPIT301.AH
		else:
			HMI.PLANT.TMP_High= HMI.DPSH301.Alarm
		

		# self.Mid_P602_AutoInp.On = self.Mid_P602_AutoInp

		#_On_ENTRY = self.Mid_Last_State != HMI.P3.State
#The above lines need to be dealt, we don't know the variables.
		#R_TRIG_BW.InputBit = HMI.P3.State ==13
		#OSRI( R_TRIG_BW)
#this R_TRIG_BW seems only needed when chemical backwash is needed
		if HMI.LIT401.AH and HMI.P3.State > 1:
			HMI.P3.State=99
		#(*-----------WRITE FAULT COnDITIOn--------------*)
		while switch(HMI.P3.State):
			if case(1):
				self.Mid_Last_State= HMI.P3.State
				self.Mid_MV301_AutoInp			=0
				self.Mid_MV302_AutoInp			=0
				self.Mid_MV303_AutoInp			=0
				self.Mid_MV304_AutoInp			=0
				self.Mid_P_UF_FEED_DUTY_AutoInp	=0
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				HMI.P3.Shutdown		=0
				if HMI.P3.Permissive_On and HMI.PLANT.Start:
					HMI.P3.State=2
				break
			if case(2):
				self.Mid_Last_State= HMI.P3.State
				self.Mid_MV301_AutoInp			=0
				self.Mid_MV302_AutoInp			=0
				self.Mid_MV303_AutoInp			=0
				self.Mid_MV304_AutoInp			=not HMI.LIT301.ALL and not HMI.LIT401.AH  
				self.Mid_P_UF_FEED_DUTY_AutoInp	=0
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if  HMI.MV304.Status==2 or self.Mid_NEXT:
					self.Mid_NEXT = 0
					HMI.P3.State=3
				break
			if case(3):
				self.Mid_Last_State= HMI.P3.State
				self.Mid_MV301_AutoInp			=0
				self.Mid_MV302_AutoInp			=0
				self.Mid_MV303_AutoInp			=0
				self.Mid_MV304_AutoInp			=1
				self.Mid_P_UF_FEED_DUTY_AutoInp	=1
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if  HMI.P301.Status ==2 or self.Mid_NEXT:
					self.Mid_NEXT =0
					HMI.P3.State=4
				break
			if case(4):
				self.Mid_Last_State= HMI.P3.State
				self.Mid_MV301_AutoInp			=0
				self.Mid_MV302_AutoInp			=0
				self.Mid_MV303_AutoInp			=0
				self.Mid_MV304_AutoInp			=1
				self.Mid_P_UF_FEED_DUTY_AutoInp	=1
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if Sec_P:
					HMI.Cy_P3.UF_REFILL_SEC=HMI.Cy_P3.UF_REFILL_SEC+1
				if HMI.Cy_P3.UF_REFILL_SEC>HMI.Cy_P3.UF_REFILL_SEC_SP or self.Mid_NEXT:
					self.Mid_NEXT =0
					HMI.P3.State=5
				break


				# timer
			if case(5):
				self.Mid_Last_State= HMI.P3.State
				self.Mid_MV301_AutoInp			=0
				self.Mid_MV302_AutoInp			=1
				self.Mid_MV303_AutoInp			=0
				self.Mid_MV304_AutoInp			=1
				self.Mid_P_UF_FEED_DUTY_AutoInp	=1
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if HMI.MV302.Status ==2 or self.Mid_NEXT:
					self.Mid_NEXT =0
					HMI.P3.State=6					
				break
			if case(6):
				self.Mid_Last_State= HMI.P3.State
				self.Mid_MV301_AutoInp			=0
				self.Mid_MV302_AutoInp			=1
				self.Mid_MV303_AutoInp			=0
				self.Mid_MV304_AutoInp			=0
				self.Mid_P_UF_FEED_DUTY_AutoInp	=1
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if HMI.MV304.Status ==1 or self.Mid_NEXT:
					self.Mid_NEXT =0
					HMI.P3.State=7					
				break
			if case(7):
				self.Mid_Last_State= HMI.P3.State
				self.Mid_MV301_AutoInp			=0
				self.Mid_MV302_AutoInp			=1
				self.Mid_MV303_AutoInp			=0
				self.Mid_MV304_AutoInp			=0
				self.Mid_P_UF_FEED_DUTY_AutoInp	=1
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if HMI.P3.TMP_High:
					HMI.P3.State=8	
				else:
					if Min_P:
						HMI.Cy_P3.UF_FILTRATION_MIN+=1
				if HMI.Cy_P3.UF_FILTRATION_MIN>=HMI.Cy_P3.UF_FILTRATION_MIN_SP or self.Mid_NEXT:				
					self.Mid_NEXT =0
					HMI.P3.State=8
				if  HMI.P3.Shutdown and HMI.LIT401.AH:
					self.Mid_NEXT =0			
					HMI.P3.State=8	
				break
			if case(8):
				self.Mid_Last_State= HMI.P3.State
				self.Mid_MV301_AutoInp			=0
				self.Mid_MV302_AutoInp			=1
				self.Mid_MV303_AutoInp			=0
				self.Mid_MV304_AutoInp			=0
				self.Mid_P_UF_FEED_DUTY_AutoInp	=0
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if not HMI.P301 == 2 or self.Mid_NEXT:
					self.Mid_NEXT =0
					HMI.P3.State=9				
				break
			if case(9):
				self.Mid_Last_State= HMI.P3.State
				self.Mid_MV301_AutoInp			=0
				self.Mid_MV302_AutoInp			=0
				self.Mid_MV303_AutoInp			=0
				self.Mid_MV304_AutoInp			=0
				self.Mid_P_UF_FEED_DUTY_AutoInp	=0
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if HMI.P3.Shutdown:	
					HMI.P3.State=1	
				elif HMI.MV302.Status==1 or self.Mid_NEXT and not HMI.P3.Shutdown:
					self.Mid_NEXT =0			
					HMI.P3.State=10	
				break
			if case(10):
				self.Mid_Last_State= HMI.P3.State
				self.Mid_MV301_AutoInp			=1
				self.Mid_MV302_AutoInp			=0
				self.Mid_MV303_AutoInp			=1
				self.Mid_MV304_AutoInp			=0
				self.Mid_P_UF_FEED_DUTY_AutoInp	=0
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if HMI.MV301.Status==2 and HMI.MV303.Status==2 or self.Mid_NEXT:
					self.Mid_NEXT =0
					HMI.P3.State=11				
				break
			if case(11):
				self.Mid_Last_State= HMI.P3.State
				self.Mid_MV301_AutoInp			=1
				self.Mid_MV302_AutoInp			=0
				self.Mid_MV303_AutoInp			=1
				self.Mid_MV304_AutoInp			=0
				self.Mid_P_UF_FEED_DUTY_AutoInp	=0
				self.Mid_P602_AutoInp			=1
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if HMI.P602.Status==2 or self.Mid_NEXT:
					self.Mid_NEXT =0
					HMI.P3.State=12				
				break
			if case(12):
				self.Mid_Last_State= HMI.P3.State
				self.Mid_MV301_AutoInp			=1
				self.Mid_MV302_AutoInp			=0
				self.Mid_MV303_AutoInp			=1
				self.Mid_MV304_AutoInp			=0
				self.Mid_P_UF_FEED_DUTY_AutoInp	=0
				self.Mid_P602_AutoInp			=1
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if Sec_P:
					HMI.Cy_P3.BACKWASH_SEC= HMI.Cy_P3.BACKWASH_SEC+1
				if HMI.Cy_P3.BACKWASH_SEC> HMI.Cy_P3.BACKWASH_SEC_SP or self.Mid_NEXT:
					self.Mid_NEXT =0
					HMI.Cy_P3.BW_CNT +=1
					HMI.P3.State=13
				break
			if case(13): 
				self.Mid_Last_State= HMI.P3.State
				self.Mid_MV301_AutoInp			=1
				self.Mid_MV302_AutoInp			=0
				self.Mid_MV303_AutoInp			=1
				self.Mid_MV304_AutoInp			=0
				self.Mid_P_UF_FEED_DUTY_AutoInp	=0
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if HMI.P602.Status==1 or self.Mid_NEXT:
					HMI.P3.State = 14
				break
			if case(14): 
				self.Mid_Last_State= HMI.P3.State
				self.Mid_MV301_AutoInp			=0
				self.Mid_MV302_AutoInp			=0
				self.Mid_MV303_AutoInp			=1
				self.Mid_MV304_AutoInp			=0
				self.Mid_P_UF_FEED_DUTY_AutoInp	=0
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if HMI.MV301.Status==1 or self.Mid_NEXT:
					self.Mid_NEXT=0
					HMI.P3.State=15		
				break
			if case(15):    
				self.Mid_Last_State= HMI.P3.State
				self.Mid_MV301_AutoInp			=0
				self.Mid_MV302_AutoInp			=0
				self.Mid_MV303_AutoInp			=1
				self.Mid_MV304_AutoInp			=1
				self.Mid_P_UF_FEED_DUTY_AutoInp	=0
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if HMI.MV304.Status==2 or self.Mid_NEXT:
					self.Mid_NEXT=0
					HMI.P3.State=16		
				break
			if case(16):  
				self.Mid_Last_State= HMI.P3.State
				self.Mid_MV301_AutoInp			=0
				self.Mid_MV302_AutoInp			=0
				self.Mid_MV303_AutoInp			=1
				self.Mid_MV304_AutoInp			=1
				self.Mid_P_UF_FEED_DUTY_AutoInp	=0
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				if Sec_P:
					HMI.Cy_P3.DRAIN_SEC=HMI.Cy_P3.DRAIN_SEC+1
				if HMI.Cy_P3.DRAIN_SEC>HMI.Cy_P3.DRAIN_SEC_SP or self.Mid_NEXT:
					self.Mid_NEXT=0
					HMI.P3.State=4
				break
			if case(17):     
				self.Mid_MV301_AutoInp			=1
				self.Mid_MV302_AutoInp			=0
				self.Mid_MV303_AutoInp			=1
				self.Mid_MV304_AutoInp			=0
				self.Mid_P_UF_FEED_DUTY_AutoInp	=0
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=1
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if HMI.P205.Status == 2 or self.Mid_NEXT:
					self.Mid_NEXT=0
					HMI.P3.State=18			
				break
			if case(18):      
				self.Mid_MV301_AutoInp			=1
				self.Mid_MV302_AutoInp			=0
				self.Mid_MV303_AutoInp			=1
				self.Mid_MV304_AutoInp			=0
				self.Mid_P_UF_FEED_DUTY_AutoInp	=0
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=1
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if Sec_P:
					HMI.Cy_P3.CIP_CLEANING_SEC=HMI.Cy_P3.CIP_CLEANING_SEC+1
				if HMI.Cy_P3.CIP_CLEANING_SEC>HMI.Cy_P3.CIP_CLEANING_SEC_SP or self.Mid_NEXT:
					self.Mid_NEXT=0
					HMI.P3.State=19
				break
			if case(19):    
				self.Mid_MV301_AutoInp			=1
				self.Mid_MV302_AutoInp			=0
				self.Mid_MV303_AutoInp			=1
				self.Mid_MV304_AutoInp			=0
				self.Mid_P_UF_FEED_DUTY_AutoInp	=0
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if not HMI.P205.Status == 2 or self.Mid_NEXT:
						self.Mid_NEXT=0
						HMI.P3.State=14
				break
			if case(99): 
				self.Mid_MV301_AutoInp			=0
				self.Mid_MV302_AutoInp			=0
				self.Mid_MV303_AutoInp			=0
				self.Mid_MV304_AutoInp			=0
				self.Mid_P_UF_FEED_DUTY_AutoInp	=0
				self.Mid_P602_AutoInp			=0
				self.Mid_P_NAOCL_UF_DUTY_AutoInp=0
				HMI.Cy_P3.UF_REFILL_SEC		=0
				HMI.Cy_P3.UF_FILTRATION_MIN	=0
				HMI.Cy_P3.BACKWASH_SEC		=0
				HMI.Cy_P3.CIP_CLEANING_SEC	=0
				HMI.Cy_P3.DRAIN_SEC			=0
				if  (HMI.LIT401.AL and not HMI.P3.Shutdown) or HMI.PLANT.Start:
					HMI.P3.State=2
				elif HMI.LIT401.AH and HMI.P3.Shutdown:
					HMI.P3.State=1
				break
			HMI.P3.State=1
			break
#end of case structure
		HMI.Mid_P602_AutoInp = self.Mid_P602_AutoInp
#	def UF_Feed(self):
		self.P_UF_FEED_DUTY_FB.Duty2_FBD(self.Mid_P_UF_FEED_DUTY_AutoInp, HMI.P301, HMI.P302, HMI.P_UF_FEED_DUTY)
		self.P301_FB.PMP_FBD(self.P_UF_FEED_DUTY_FB.Start_Pmp1, IO.P301, HMI.P301)
		self.P302_FB.PMP_FBD(self.P_UF_FEED_DUTY_FB.Start_Pmp2, IO.P302, HMI.P302)
		self.PSH301_FB.SWITCH_FBD(IO.PSH301, HMI.PSH301)
		self.DPSH301_FB.SWITCH_FBD(IO.DPSH301, HMI.DPSH301)
		self.MV301_FB.MV_FBD(self.Mid_MV301_AutoInp, IO.MV301, HMI.MV301)
		self.MV302_FB.MV_FBD(self.Mid_MV302_AutoInp, IO.MV302, HMI.MV302)
		self.MV303_FB.MV_FBD(self.Mid_MV303_AutoInp, IO.MV303, HMI.MV303)
		self.MV304_FB.MV_FBD(self.Mid_MV304_AutoInp, IO.MV304, HMI.MV304)

