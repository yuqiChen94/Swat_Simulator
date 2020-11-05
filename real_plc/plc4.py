# this is the PLC 4 logic, it's about the very same thing as that in the real plc.
from logicblock.logicblock import SETD
from logicblock.logicblock import TONR
from controlblock.controlblock import *

class plc4:
	'plc4 logic'
	
	def __init__(self,HMI):
		self.Mid_UV401_AutoInp = HMI.UV401.Status-1
		self.Mid_P_NAHSO3_ORP_DUTY_AutoInp = HMI.P401.Status-1
		self.Mid_FIT401_Tot_Enb = 0
		self.TON_FIT401_TM = TONR(6,"FIT401")
		self.TON_FIT401_P1_TM = TONR(6,"FIT401_p1")
		self.TON_FIT401_P2_TM = TONR(6,"FIT401_p2")
		self.Mid_P_RO_FEED_DUTY_AutoInp = HMI
		self.Mid_P_NAHSO3_ORP_DUTY_AutoInp = 0
		
		self.LIT401_FB = AIN_FBD(HMI.LIT401)
		self.P_RO_FEED_DUTY_FB = Duty2_FBD()
		self.P401_FB = PMP_FBD(HMI.P401)
		self.P402_FB = PMP_FBD(HMI.P402)
		self.AIT401_FB = AIN_FBD(HMI.AIT401)
		self.FIT401_FB = FIT_FBD(HMI.FIT401)
		self.UV401_FB = UV_FBD(HMI.UV401)
		self.AIT402_FB = AIN_FBD(HMI.AIT402)
		self.LS401_FB = SWITCH_FBD(HMI.LS401)

		self.P_NAHSO3_ORP_DUTY_FB = Duty2_FBD()
		self.P403_FB = PMP_FBD(HMI.P403)
		self.P404_FB = PMP_FBD(HMI.P404)
		# print ("	PLC4 Started\n")

	def Pre_Main_RO_Feed_Dosing(self, IO,HMI):
#	def Pre_Condition(self):
		if HMI.PLANT.Reset_On:
			HMI.P401.Reset	=1
			HMI.P402.Reset	=1
			HMI.P403.Reset	=1
			HMI.P404.Reset	=1
			HMI.UV401.Reset	=1		

		if HMI.PLANT.Auto_On:
			HMI.P401.Auto	=1
			HMI.P402.Auto	=1
			HMI.P403.Auto	=1
			HMI.P404.Auto	=1
			HMI.UV401.Auto	=1

		if HMI.PLANT.Auto_Off:
			HMI.P401.Auto	=0
			HMI.P402.Auto	=0
			HMI.P403.Auto	=0
			HMI.P404.Auto	=0
			HMI.UV401.Auto	=0


		HMI.P4.Permissive_On= (HMI.P401.Avl or HMI.P402.Avl) and (HMI.P403.Avl or HMI.P404.Avl) and HMI.UV401.Avl

		self.Mid_FIT401_Tot_Enb	= HMI.P401.Status==2 or HMI.P402.Status==2

		self.TON_FIT401_TM.TONR((HMI.P401.Status==2 or HMI.P402.Status==2 )and HMI.FIT401.ALL)
		self.TON_FIT401_P1_TM.TONR(HMI.FIT401.ALL and HMI.P401.Status == 2)
		self.TON_FIT401_P2_TM.TONR(HMI.FIT401.ALL and HMI.P402.Status == 2)

		HMI.P401.Permissive[0] 	= not HMI.LIT401.ALL
		HMI.P401.Permissive[1] 	= HMI.MV501.Status==2 or HMI.MV502.Status==2 or HMI.MV503.Status==2 or HMI.MV504.Status==2 

		HMI.P401.MSG_Permissive[1] = HMI.P401.Permissive[0]
		HMI.P401.MSG_Permissive[2] = 0

		HMI.P402.Permissive[0] 	= not HMI.LIT401.ALL
		HMI.P402.Permissive[1] 	= HMI.MV501.Status==2 or HMI.MV502.Status==2 or HMI.MV503.Status==2 or HMI.MV504.Status==2 

		HMI.P402.MSG_Permissive[1] = HMI.P402.Permissive[0]

		HMI.P403.Permissive[0] 	= not HMI.LS401.Alarm
		HMI.P403.Permissive[1]	= HMI.P401.Status==2 or HMI.P402.Status==2

		HMI.P403.MSG_Permissive[1] = HMI.P403.Permissive[0]
		HMI.P403.MSG_Permissive[2] = HMI.P403.Permissive[1]

		HMI.P404.Permissive[0] 	= not HMI.LS401.Alarm
		HMI.P404.Permissive[1] 	= HMI.P401.Status==2 or HMI.P402.Status==2

		HMI.P404.MSG_Permissive[1] = HMI.P404.Permissive[0]
		HMI.P404.MSG_Permissive[2] = HMI.P404.Permissive[1]

		HMI.UV401.Permissive[0] 	= HMI.P401.Status==2 or HMI.P402.Status==2
		HMI.UV401.Permissive[1] 	= not HMI.FIT401.ALL

		HMI.UV401.MSG_Permissive[1] = HMI.P403.Permissive[0]
		HMI.UV401.MSG_Permissive[2] = HMI.P403.Permissive[1]

		HMI.P401.SD[0]	= HMI.LIT401.ALL
		HMI.P401.SD[1]	= self.TON_FIT401_P1_TM.DN
		HMI.P401.SD[2]	= HMI.P401.Status==2 and HMI.MV501.Status!=2 and HMI.MV502.Status!=2 and HMI.MV503.Status!=2 and HMI.MV504.Status!=2 

		HMI.P401.MSG_Shutdown[1] = HMI.P401.Shutdown[0] 
		HMI.P401.MSG_Shutdown[2] = HMI.P401.Shutdown[1] 
		HMI.P401.MSG_Shutdown[3] = HMI.P401.Shutdown[2] 
		HMI.P401.MSG_Shutdown[4] = HMI.P401.Shutdown[3]
		HMI.P401.MSG_Shutdown[5] = HMI.P401.Shutdown[4]

		HMI.P402.SD[0] 	= HMI.LIT401.ALL
		HMI.P402.SD[1] 	= self.TON_FIT401_P2_TM.DN
		HMI.P402.SD[2] 	= HMI.P402.Status==2 and HMI.MV501.Status!=2 and HMI.MV502.Status!=2 and HMI.MV503.Status!=2 and HMI.MV504.Status!=2 

		HMI.P402.MSG_Shutdown[1] = HMI.P402.Shutdown[0] 
		HMI.P402.MSG_Shutdown[2] = HMI.P402.Shutdown[1] 
		HMI.P402.MSG_Shutdown[3] = HMI.P402.Shutdown[2] 
		HMI.P402.MSG_Shutdown[4] = HMI.P402.Shutdown[3]
		HMI.P402.MSG_Shutdown[5] = HMI.P402.Shutdown[4]

		HMI.P403.SD[0] 	= HMI.LS401.Alarm
		HMI.P403.SD[1] 	= (HMI.P401.Status==2 or HMI.P402.Status==2 )and HMI.FIT401.ALL

		HMI.P403.MSG_Shutdown[1] = HMI.P403.Shutdown[0] 
		HMI.P403.MSG_Shutdown[2] = HMI.P403.Shutdown[1] 
		HMI.P403.MSG_Shutdown[3] = HMI.P403.Shutdown[2] 
		HMI.P403.MSG_Shutdown[4] = HMI.P403.Shutdown[3]
		HMI.P403.MSG_Shutdown[5] = HMI.P403.Shutdown[4]

		HMI.P404.SD[0]	= HMI.LS401.Alarm
		HMI.P404.SD[1] 	= (HMI.P401.Status==2 or HMI.P402.Status==2) and HMI.FIT401.ALL

		HMI.P404.MSG_Shutdown[1] = HMI.P404.Shutdown[0] 
		HMI.P404.MSG_Shutdown[2] = HMI.P404.Shutdown[1] 
		HMI.P404.MSG_Shutdown[3] = HMI.P404.Shutdown[2] 
		HMI.P404.MSG_Shutdown[4] = HMI.P404.Shutdown[3]
		HMI.P404.MSG_Shutdown[5] = HMI.P404.Shutdown[4]

		HMI.UV401.SD[0] 	= self.TON_FIT401_TM.DN

		HMI.UV401.MSG_Shutdown[1] = HMI.UV401.Shutdown[0] 
		HMI.UV401.MSG_Shutdown[2] = HMI.UV401.Shutdown[1] 
		HMI.UV401.MSG_Shutdown[3] = HMI.UV401.Shutdown[2] 
		HMI.UV401.MSG_Shutdown[4] = HMI.UV401.Shutdown[3] 
		HMI.UV401.MSG_Shutdown[5] = HMI.UV401.Shutdown[4] 

# Main
		if HMI.P4.State == 1:
			self.Mid_UV401_AutoInp				=0
			self.Mid_P_RO_FEED_DUTY_AutoInp		=0
			self.Mid_P_NAHSO3_ORP_DUTY_AutoInp	=0

			if HMI.P4.Permissive_On and HMI.PLANT.Start:
				HMI.P4.State=2
			 

		if HMI.P4.State == 2:
			self.Mid_UV401_AutoInp				=0		
			self.Mid_P_RO_FEED_DUTY_AutoInp		= HMI.MV503.Status==2 and HMI.MV504.Status==2 
			self.Mid_P_NAHSO3_ORP_DUTY_AutoInp	=0

			if HMI.P401.Status ==2:
				HMI.P4.State=3
			


		if HMI.P4.State == 3:
			self.Mid_UV401_AutoInp				=1
			self.Mid_P_RO_FEED_DUTY_AutoInp		=1
			self.Mid_P_NAHSO3_ORP_DUTY_AutoInp	=0

			if HMI.UV401.Status==2:
				HMI.P4.State=4
			 

		if HMI.P4.State == 4:
			self.Mid_UV401_AutoInp				=1		
			self.Mid_P_RO_FEED_DUTY_AutoInp		=1

			self.Mid_P_NAHSO3_ORP_DUTY_AutoInp = SETD((HMI.P401.Status==2 or HMI.P402.Status==2) and (HMI.AIT402.AH),(HMI.P401.Status!=2 and HMI.P402.Status!=2) or (HMI.AIT402.AL),self.Mid_P_NAHSO3_ORP_DUTY_AutoInp)

			if HMI.RO_HPP.SD_On: #(shutdown->stopping sequence)
				HMI.P4.State=5
			 

		if HMI.P4.State == 5:
			self.Mid_UV401_AutoInp				=1		
			self.Mid_P_RO_FEED_DUTY_AutoInp		=HMI.MV503.Status==1 and HMI.MV504.Status==1
			self.Mid_P_NAHSO3_ORP_DUTY_AutoInp	= 0

			if not HMI.P401.Status ==2:
				HMI.P4.State=6
			 

		if HMI.P4.State == 6:
			self.Mid_UV401_AutoInp				=0		
			self.Mid_P_RO_FEED_DUTY_AutoInp		=0
			self.Mid_P_NAHSO3_ORP_DUTY_AutoInp	= 0

			if HMI.UV401.Status==1:			
				HMI.P4.State=1
				 
		else:
			HMI.P4.State=1




# RO_Feed_Dosing
		self.P_RO_FEED_DUTY_FB.Duty2_FBD(self.Mid_P_RO_FEED_DUTY_AutoInp, HMI.P401, HMI.P402, HMI.P_RO_FEED_DUTY)
		self.P401_FB.PMP_FBD(self.P_RO_FEED_DUTY_FB.Start_Pmp1,IO.P401,HMI.P401)
		self.P402_FB.PMP_FBD(self.P_RO_FEED_DUTY_FB.Start_Pmp2,IO.P402,HMI.P402)
		self.UV401_FB.UV_FBD(self.Mid_UV401_AutoInp, IO.UV401, HMI.UV401)
		self.LS401_FB.SWITCH_FBD(IO.LS401,HMI.LS401)
		self.P_NAHSO3_ORP_DUTY_FB.Duty2_FBD(self.Mid_P_NAHSO3_ORP_DUTY_AutoInp, HMI.P403, HMI.P404, HMI.P_NAHSO3_ORP_DUTY)
		self.P403_FB.PMP_FBD(self.P_NAHSO3_ORP_DUTY_FB.Start_Pmp1,IO.P403,HMI.P403)
		self.P404_FB.PMP_FBD(self.P_NAHSO3_ORP_DUTY_FB.Start_Pmp2,IO.P404,HMI.P404)

