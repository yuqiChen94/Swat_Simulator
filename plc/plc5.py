# this is the PLC 5 logic, it's about the very same thing as that in the real plc.
from logicblock.logicblock import *
from controlblock.controlblock import *


class plc5:
	'plc5 logic'
	def __init__(self,HMI):
		self.Mid_Stop = 0
		self.Mid_NEXT = 0
		self.TON_FIT401_TM=TONR(3,"FIT401_TM")
		self.SEC_TEST = 0
		self.TEST_MIN = 0
		self.Mid_FIT501_Tot_Enb = 1
		self.Mid_FIT502_Tot_Enb = 1
		self.Mid_FIT503_Tot_Enb = 1
		self.Mid_FIT504_Tot_Enb = 1
		self.Mid_MV501_AutoInp = HMI.MV501.Status-1
		self.Mid_MV502_AutoInp = HMI.MV502.Status-1
		self.Mid_MV503_AutoInp = HMI.MV503.Status-1
		self.Mid_MV504_AutoInp = HMI.MV504.Status-1
		self.Mid_P50X_AutoSpeed = 0
		self.Mid_P_RO_HIGH_AutoInp = 1

		self.AIT501_FB = AIN_FBD(HMI.AIT501)
		self.AIT502_FB = AIN_FBD(HMI.AIT502)
		self.AIT503_FB = AIN_FBD(HMI.AIT503)
		self.AIT504_FB = AIN_FBD(HMI.AIT504)
		self.PIT501_FB = AIN_FBD(HMI.PIT501)
		self.PIT502_FB = AIN_FBD(HMI.PIT502)
		self.PIT503_FB = AIN_FBD(HMI.PIT503)

		self.FIT501_FB = FIT_FBD(HMI.FIT501)
		self.FIT502_FB = FIT_FBD(HMI.FIT502)
		self.FIT503_FB = FIT_FBD(HMI.FIT503)
		self.FIT504_FB = FIT_FBD(HMI.FIT504)

		self.MV501_FB  = MV_FBD(HMI.MV501)
		self.MV502_FB  = MV_FBD(HMI.MV502)
		self.MV503_FB  = MV_FBD(HMI.MV503)
		self.MV504_FB  = MV_FBD(HMI.MV504)
		self.P501_FB   = VSD_FBD(HMI.P501)
		self.P502_FB   = VSD_FBD(HMI.P502)
		self.P_RO_HIGH_DUTY_FB = Duty2_FBD()


	def Pre_Main_High_Pressure_RO(self,IO,HMI,Sec_P,Min_P):
		if HMI.PLANT.Reset_On:
			HMI.P501.Reset	=1
			HMI.P502.Reset	=1
			HMI.MV501.Reset	=1
			HMI.MV502.Reset	=1
			HMI.MV503.Reset	=1
			HMI.MV504.Reset =1

		if HMI.PLANT.Auto_On:
			HMI.P501.Auto	=1
			HMI.P502.Auto	=1
			HMI.MV501.Auto	=1
			HMI.MV502.Auto	=1
			HMI.MV503.Auto	=1
			HMI.MV504.Auto 	=1


		if HMI.PLANT.Auto_Off:
			HMI.P501.Auto	=0
			HMI.P502.Auto	=0
			HMI.MV501.Auto	=0
			HMI.MV502.Auto	=0
			HMI.MV503.Auto	=0
			HMI.MV504.Auto 	=0

		HMI.P5_Permissive_On= (HMI.P501.Avl or HMI.P502.Avl) and HMI.MV501.Avl and HMI.MV502.Avl and HMI.MV503.Avl and HMI.MV504.Avl

		self.Mid_FIT501_Tot_Enb	= HMI.P501.Status==2 or HMI.P502.Status==2
		self.Mid_FIT502_Tot_Enb	= HMI.MV501.Status==2
		self.Mid_FIT503_Tot_Enb	= HMI.P401.Status==2 or HMI.P402.Status==2
		self.Mid_FIT504_Tot_Enb	= HMI.P401.Status==2 or HMI.P402.Status==2
		self.TON_FIT401_TM.TONR(HMI.FIT401.ALL and HMI.P_RO_FEED_DUTY.Pump_Running)
		HMI.P501.Permissive[0] 	= HMI.P_RO_FEED_DUTY.Pump_Running
		HMI.P501.Permissive[1] 	= not HMI.FIT401.ALL
		HMI.P501.Permissive[2] 	= HMI.UV401.Status==2

		HMI.P501.MSG_Permissive[1] = HMI.P501.Permissive[0]
		HMI.P501.MSG_Permissive[2] = HMI.P501.Permissive[1]
		HMI.P501.MSG_Permissive[3] = HMI.P501.Permissive[2]

		HMI.P502.Permissive[0]	= HMI.P_RO_FEED_DUTY.Pump_Running
		HMI.P502.Permissive[1]	= not HMI.FIT401.ALL
		HMI.P502.Permissive[2]	= HMI.UV401.Status==2

		HMI.P502.MSG_Permissive[1] = HMI.P502.Permissive[0]
		HMI.P502.MSG_Permissive[2] = HMI.P502.Permissive[1]
		HMI.P502.MSG_Permissive[3] = HMI.P502.Permissive[2]

		HMI.P501.SD[0] 	= not HMI.P_RO_FEED_DUTY.Pump_Running
		HMI.P501.SD[1] 	= self.TON_FIT401_TM.DN
		HMI.P501.SD[2] 	= HMI.UV401.Status!=2
		HMI.P501.SD[3] 	= 0
		HMI.P501.SD[4] 	= 0

		HMI.P501.MSG_Shutdown[1] = HMI.P501.Shutdown[0]
		HMI.P501.MSG_Shutdown[2] = HMI.P501.Shutdown[1]
		HMI.P501.MSG_Shutdown[3] = HMI.P501.Shutdown[2]
		HMI.P501.MSG_Shutdown[4] = HMI.P501.Shutdown[3]
		HMI.P501.MSG_Shutdown[5] = HMI.P501.Shutdown[4]

		HMI.P502.SD[0] 	= not HMI.P_RO_FEED_DUTY.Pump_Running
		HMI.P502.SD[1] 	= self.TON_FIT401_TM.DN
		HMI.P502.SD[2] 	= HMI.UV401.Status!=2
		HMI.P502.SD[3] 	= 0
		HMI.P502.SD[4] 	= 0

		HMI.P502.MSG_Shutdown[1]= HMI.P502.Shutdown[0]
		HMI.P502.MSG_Shutdown[2]= HMI.P502.Shutdown[1]
		HMI.P502.MSG_Shutdown[3]= HMI.P502.Shutdown[2]
		HMI.P502.MSG_Shutdown[4]= HMI.P502.Shutdown[3]
		HMI.P502.MSG_Shutdown[5]= HMI.P502.Shutdown[4]
#Main

		if HMI.PLANT.Stop:
			HMI.P5.State=13


		HMI.Cy_P5.RO_TMP	=((HMI.PIT501.Pv+ HMI.PIT503.Pv)/2)-HMI.PIT502.Pv
		HMI.Cy_P5.HPP_Q_MAX_M3H	 		= 2
		HMI.Cy_P5.HPP_Q_SET_M3H 			= 1.25
		HMI.Cy_P5.MIN_RO_VSD_SPEED		= HMI.Cy_P5.HPP_Q_SET_M3H/ HMI.Cy_P5.HPP_Q_MAX_M3H *50 *0.1
		HMI.Cy_P5.RAMPING_RATE_PER_SEC	= 1.5
		HMI.Cy_P5.VSD_MIN_SPEED			= 10
		HMI.Cy_P5.VSD_HIGH_SPEED			= 30

		while switch(HMI.P5.State):
			if case(1):
				self.Mid_P_RO_HIGH_AutoInp		= 0
				self.Mid_MV501_AutoInp			= 0
				self.Mid_MV502_AutoInp			= 0
				self.Mid_MV503_AutoInp			= 0
				self.Mid_MV504_AutoInp			= 0
				self.Mid_P50X_AutoSpeed			= HMI.Cy_P5.VSD_MIN_SPEED
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if HMI.P5.Permissive_On and HMI.PLANT.Start:
					self.Mid_NEXT=0
					HMI.P5.State=3
				break
			if case(2):
				self.Mid_P_RO_HIGH_AutoInp	= 0
				self.Mid_MV501_AutoInp		= 0
				self.Mid_MV502_AutoInp		= 0
				self.Mid_MV503_AutoInp		= 0
				self.Mid_MV504_AutoInp		= 0
				self.Mid_P50X_AutoSpeed		= HMI.Cy_P5.VSD_MIN_SPEED
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if HMI.P_RO_FEED_DUTY.Pump_Running and self.Mid_NEXT:
					self.Mid_NEXT=0
					HMI.P5.State=3
				break
			if case(3):
				self.Mid_P_RO_HIGH_AutoInp	= 0
				self.Mid_MV501_AutoInp		= 0
				self.Mid_MV502_AutoInp		= 0
				self.Mid_MV503_AutoInp		= 1
				self.Mid_MV504_AutoInp		= 1
				self.Mid_P50X_AutoSpeed		= HMI.Cy_P5.VSD_MIN_SPEED
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if HMI.MV503.Status==2 and HMI.MV504.Status==2 and HMI.P_RO_FEED_DUTY.Pump_Running or self.Mid_NEXT:
					self.Mid_NEXT=0
					HMI.P5.State=4
				break
			if case(4):
				self.Mid_P_RO_HIGH_AutoInp	= 0
				self.Mid_MV501_AutoInp		= 0
				self.Mid_MV502_AutoInp		= 0
				self.Mid_MV503_AutoInp		= 1
				self.Mid_MV504_AutoInp		= 1
				self.Mid_P50X_AutoSpeed		= HMI.Cy_P5.VSD_MIN_SPEED
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				# if Min_P:
				# 	HMI.Cy_P5.FLUSHING_MIN= HMI.Cy_P5.FLUSHING_MIN+1
				# if HMI.Cy_P5.FLUSHING_MIN>HMI.Cy_P5.FLUSHING_MIN_SP or self.Mid_NEXT:
				# 	HMI.Cy_P5.SD_FLUSHING_DONE_On	=1
				# 	self.Mid_NEXT =0
				# 	HMI.P5.State=5
				break
			if case(5):
				self.Mid_P_RO_HIGH_AutoInp	= 1
				self.Mid_MV501_AutoInp		= 0
				self.Mid_MV502_AutoInp		= 0
				self.Mid_MV503_AutoInp		= 1
				self.Mid_MV504_AutoInp		= 1
				self.Mid_P50X_AutoSpeed		= HMI.Cy_P5.VSD_MIN_SPEED
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if (HMI.P501.Speed >= self.Mid_P50X_AutoSpeed) or (HMI.P502.Speed >= self.Mid_P50X_AutoSpeed) or self.Mid_NEXT:
					self.Mid_NEXT=0
					HMI.P5.State=6
				break
			if case(6):
				self.Mid_P_RO_HIGH_AutoInp	= 1
				self.Mid_MV501_AutoInp		= 0
				self.Mid_MV502_AutoInp		= 0
				self.Mid_MV503_AutoInp		= 1
				self.Mid_MV504_AutoInp		= 1
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if  self.Mid_P50X_AutoSpeed <  HMI.Cy_P5.VSD_HIGH_SPEED:
					if Sec_P:
						if (HMI.PIT502.Pv<HMI.PIT503.Pv) and HMI.PIT501.Pv<250:
							self.Mid_P50X_AutoSpeed =  self.Mid_P50X_AutoSpeed + 0.5
				if ((HMI.FIT501.Pv > HMI.Cy_P5.HPP_Q_SET_M3H) and (HMI.PIT502.Pv<HMI.PIT503.Pv)) and HMI.PIT501.Pv>250 or self.Mid_NEXT:
						self.Mid_NEXT=0
						HMI.P5.State=7
				break
			if case(7):
				self.Mid_P_RO_HIGH_AutoInp	= 1
				self.Mid_MV501_AutoInp		= 0
				self.Mid_MV502_AutoInp		= 0
				self.Mid_MV503_AutoInp		= 1
				self.Mid_MV504_AutoInp		= 1
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if HMI.AIT504.Pv < HMI.AIT504.SAH or self.Mid_NEXT:
					self.Mid_NEXT=0
					HMI.P5.State=8
				break
			if case(8):
				self.Mid_P_RO_HIGH_AutoInp	= 1
				self.Mid_MV501_AutoInp		= 1
				self.Mid_MV502_AutoInp		= 0
				self.Mid_MV503_AutoInp		= 1
				self.Mid_MV504_AutoInp		= 1
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if HMI.MV501.Status==2 or self.Mid_NEXT:
					self.Mid_NEXT=0
					HMI.P5.State=9
				break
			if case(9):
				self.Mid_P_RO_HIGH_AutoInp	= 1
				self.Mid_MV501_AutoInp		= 1
				self.Mid_MV502_AutoInp		= 0
				self.Mid_MV503_AutoInp		= 0
				self.Mid_MV504_AutoInp		= 1
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if HMI.MV503.Status==1 or self.Mid_NEXT:
					self.Mid_NEXT=0
					HMI.P5.State=10
				break
			if case(10):
				self.Mid_P_RO_HIGH_AutoInp	= 1
				self.Mid_MV501_AutoInp		= 1
				self.Mid_MV502_AutoInp		= 1
				self.Mid_MV503_AutoInp		= 0
				self.Mid_MV504_AutoInp		= 1
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if HMI.MV502.Status==2 or self.Mid_NEXT:
					self.Mid_NEXT=0
					HMI.P5.State=11
				break
			if case(11):
				self.Mid_P_RO_HIGH_AutoInp	= 1
				self.Mid_MV501_AutoInp		= 1
				self.Mid_MV502_AutoInp		= 1
				self.Mid_MV503_AutoInp		= 0
				self.Mid_MV504_AutoInp		= 0
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if HMI.MV504.Status==1 or self.Mid_NEXT:
					self.Mid_NEXT=0
					HMI.P5.State=12
				break
			if case(12):
				self.Mid_P_RO_HIGH_AutoInp	= 1
				self.Mid_MV501_AutoInp		= 1
				self.Mid_MV502_AutoInp		= 1
				self.Mid_MV503_AutoInp		= 0
				self.Mid_MV504_AutoInp		= 0
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if HMI.PLANT.Stop or self.Mid_Stop :
					self.Mid_Stop=0
					HMI.P5.State=13
				break
			if case(13):
				self.Mid_P_RO_HIGH_AutoInp	= 1
				self.Mid_MV501_AutoInp		= 1
				self.Mid_MV502_AutoInp		= 1
				self.Mid_MV503_AutoInp		= 0
				self.Mid_MV504_AutoInp		= 0
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if  self.Mid_P50X_AutoSpeed >  HMI.Cy_P5.VSD_MIN_SPEED  :
					if Sec_P:
						self.Mid_P50X_AutoSpeed =  self.Mid_P50X_AutoSpeed - 0.5
				if  (HMI.P501.Speed <= HMI.Cy_P5.VSD_MIN_SPEED) and  (HMI.P502.Speed <= HMI.Cy_P5.VSD_MIN_SPEED) or self.Mid_NEXT:
					self.Mid_NEXT=0
					HMI.P5.State=14
				break
			if case(14):
				self.Mid_P_RO_HIGH_AutoInp	= 0
				self.Mid_MV501_AutoInp		= 1
				self.Mid_MV502_AutoInp		= 1
				self.Mid_MV503_AutoInp		= 0
				self.Mid_MV504_AutoInp		= 0
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if not HMI.P_RO_HIGH_DUTY.Pump_Running or self.Mid_NEXT :
					self.Mid_NEXT=0
					HMI.P5.State=15
				break
			if case(15):
				self.Mid_P_RO_HIGH_AutoInp	= 0
				self.Mid_MV501_AutoInp		= 1
				self.Mid_MV502_AutoInp		= 1
				self.Mid_MV503_AutoInp		= 0
				self.Mid_MV504_AutoInp		= 1
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				if Sec_P:
					HMI.Cy_P5.MV504_TIMEOUT_TM= HMI.Cy_P5.MV504_TIMEOUT_TM+1
				if HMI.MV504.Status==2 or self.Mid_NEXT or HMI.Cy_P5.MV504_TIMEOUT_TM >120:
					self.Mid_NEXT=0
					HMI.P5.State=16
				break
			if case(16):
				self.Mid_P_RO_HIGH_AutoInp	= 0
				self.Mid_MV501_AutoInp		= 1
				self.Mid_MV502_AutoInp		= 0
				self.Mid_MV503_AutoInp		= 0
				self.Mid_MV504_AutoInp		= 1

				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if Sec_P:
					HMI.Cy_P5.MV502_TIMEOUT_TM= HMI.Cy_P5.MV502_TIMEOUT_TM+1
				if HMI.MV502.Status==1 or self.Mid_NEXT or HMI.Cy_P5.MV502_TIMEOUT_TM >120:
					self.Mid_NEXT=0
					HMI.P5.State=17
				break
			if case(17):
				self.Mid_P_RO_HIGH_AutoInp	= 0
				self.Mid_MV501_AutoInp		= 1
				self.Mid_MV502_AutoInp		= 0
				self.Mid_MV503_AutoInp		= 1
				self.Mid_MV504_AutoInp		= 1
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if Sec_P:
					HMI.Cy_P5.MV503_TIMEOUT_TM= HMI.Cy_P5.MV503_TIMEOUT_TM+1
				if HMI.MV503.Status==2 or self.Mid_NEXT or HMI.Cy_P5.MV503_TIMEOUT_TM >120 :
					self.Mid_NEXT=0
					HMI.P5.State=18
				break
			if case(18):
				self.Mid_P_RO_HIGH_AutoInp	= 0
				self.Mid_MV501_AutoInp		= 0
				self.Mid_MV502_AutoInp		= 0
				self.Mid_MV503_AutoInp		= 1
				self.Mid_MV504_AutoInp		= 1
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if HMI.MV501.Status==1 or self.Mid_NEXT or HMI.Cy_P5.MV501_TIMEOUT_TM >120 :
					self.Mid_NEXT=0
					HMI.P5.State=19
				break
			if case(19):
				self.Mid_P_RO_HIGH_AutoInp	= 0
				self.Mid_MV501_AutoInp		= 0
				self.Mid_MV502_AutoInp		= 0
				self.Mid_MV503_AutoInp		= 1
				self.Mid_MV504_AutoInp		= 1
				self.Mid_P50X_AutoSpeed		= HMI.Cy_P5.VSD_MIN_SPEED
				HMI.Cy_P5.RO_HPP_SD_On			=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if HMI.Cy_P5.RO_SD_FLUSHING_MIN>HMI.Cy_P5.RO_SD_FLUSHING_MIN_SP or self.Mid_NEXT:
					self.Mid_NEXT=0
					HMI.P5.State=20
				break
			if case(20):
				self.Mid_P_RO_HIGH_AutoInp	= 0
				self.Mid_MV501_AutoInp		= 0
				self.Mid_MV502_AutoInp		= 0
				self.Mid_MV503_AutoInp		= 1
				self.Mid_MV504_AutoInp		= 1
				self.Mid_P50X_AutoSpeed		= HMI.Cy_P5.VSD_MIN_SPEED
				HMI.Cy_P5.RO_HPP_SD_On			=1
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				HMI.Cy_P5.MV503_TIMEOUT_TM		=0
				HMI.Cy_P5.MV504_TIMEOUT_TM		=0
				if (not HMI.P_RO_FEED_DUTY.Pump_Running ) or self.Mid_NEXT:
					self.Mid_NEXT=0
					HMI.P5.State=21
				break
			if case(21):
				self.Mid_P_RO_HIGH_AutoInp	= 0
				self.Mid_MV501_AutoInp		= 0
				self.Mid_MV502_AutoInp		= 0
				self.Mid_MV503_AutoInp		= 0
				self.Mid_MV504_AutoInp		= 0
				self.Mid_P50X_AutoSpeed		= HMI.Cy_P5.VSD_MIN_SPEED
				HMI.Cy_P5.RO_HPP_SD_On=0
				HMI.Cy_P5.FLUSHING_MIN			=0
				HMI.Cy_P5.RO_SD_FLUSHING_MIN		=0
				HMI.Cy_P5.RO_HIGH_PUMP_Shutdown	=0
				HMI.Cy_P5.SD_FLUSHING_DONE_On	=0
				HMI.Cy_P5.MV501_TIMEOUT_TM		=0
				HMI.Cy_P5.MV502_TIMEOUT_TM		=0
				if HMI.MV503.Status==1 and HMI.MV504.Status==1 or self.Mid_NEXT or HMI.Cy_P5.MV503_TIMEOUT_TM >120 or HMI.Cy_P5.MV504_TIMEOUT_TM >120 :
					HMI.P5.State=1
				break
			HMI.P5.State=1
			break
# End of Case struture
#	def Pre_Condition(self):

#	def High_Pressure_RO(self):
		# self.AIT501_FB.AIN_FBD(IO.AIT501,HMI.AIT501)
		# self.AIT502_FB.AIN_FBD(IO.AIT502,HMI.AIT502)
		# self.AIT503_FB.AIN_FBD(IO.AIT503,HMI.AIT503)
		# self.AIT504_FB.AIN_FBD(IO.AIT504,HMI.AIT504)
		# self.PIT501_FB.AIN_FBD(IO.PIT501,HMI.PIT501)
		# self.PIT502_FB.AIN_FBD(IO.PIT502,HMI.PIT502)
		# self.PIT503_FB.AIN_FBD(IO.PIT503,HMI.PIT503)
		# self.FIT501_FB.FIT_FBD(self.Mid_FIT501_Tot_Enb,IO.FIT501,HMI.FIT501,Sec_P)
		# self.FIT502_FB.FIT_FBD(self.Mid_FIT502_Tot_Enb,IO.FIT502,HMI.FIT502,Sec_P)
		# self.FIT503_FB.FIT_FBD(self.Mid_FIT503_Tot_Enb,IO.FIT503,HMI.FIT503,Sec_P)
		# self.FIT504_FB.FIT_FBD(self.Mid_FIT504_Tot_Enb,IO.FIT504,HMI.FIT504,Sec_P)
		self.MV501_FB.MV_FBD(self.Mid_MV501_AutoInp,IO.MV501,HMI.MV501)
		self.MV502_FB.MV_FBD(self.Mid_MV502_AutoInp,IO.MV502,HMI.MV502)
		self.MV503_FB.MV_FBD(self.Mid_MV503_AutoInp,IO.MV503,HMI.MV503)
		self.MV504_FB.MV_FBD(self.Mid_MV504_AutoInp,IO.MV504,HMI.MV504)
		self.P501_FB.VSD_FBD(self.P_RO_HIGH_DUTY_FB.Start_Pmp1,self.Mid_P50X_AutoSpeed, IO.P501_VSD_In, IO.P501_VSD_Out, IO.P501,HMI.P501)
		self.P502_FB.VSD_FBD(self.P_RO_HIGH_DUTY_FB.Start_Pmp2,self.Mid_P50X_AutoSpeed, IO.P502_VSD_In, IO.P502_VSD_Out, IO.P502,HMI.P502)
		self.P_RO_HIGH_DUTY_FB.Duty2_FBD(self.Mid_P_RO_HIGH_AutoInp,HMI.P501,HMI.P502,HMI.P_RO_HIGH_DUTY)





