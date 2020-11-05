
from logicblock.logicblock import TONR
from logicblock.logicblock import bit_2_signed_integer
from logicblock.logicblock import signed_integer_2_bit
# 8 Classes in this file
class AIN_FBD:

	def __init__(self,HMI):
		self.Hty = HMI.Hty
		self.AHH = HMI.AHH
		self.AH = HMI.AH
		self.AL = HMI.AL
		self.ALL = HMI.ALL

	# def AIN_FBD(self,IO,HMI):
	# 	SAHH = HMI.SAHH
	# 	SAH  = HMI.SAHH
	# 	SAL  = HMI.SAL
	# 	SALL = HMI.SALL
	#
	# 	self.AHH, self.AH, self.AL, self.ALL = ALM(HMI.Pv,SAHH,SAH,SAL,SALL)
	# 	HMI.Hty = self.Hty
	# 	HMI.AHH = self.AHH
	# 	HMI.AH  = self.AH
	# 	HMI.AL  = self.AL
	# 	HMI.ALL = self.ALL

			
class MV_FBD:
	def __init__(self,HMI):
		self.FTO = HMI.FTO
		self.FTC = HMI.FTC
		self.Cmd_Open = HMI.Open
		self.Cmd_Close = HMI.Close

	def MV_FBD(self, AutoInp,IO,HMI):
		ZSO = IO.DI_ZSO
		ZSC = IO.DI_ZSC
		Auto = HMI.Auto
		if ZSC:
			HMI.Status = 1
		elif ZSO:
			HMI.Status = 2
		else:
			HMI.Status = 0
		# transfer
		HMI.Avl = Auto
		if AutoInp:
			self.Cmd_Close = 0
			self.Cmd_Open  = 1
		else:
			self.Cmd_Close = 1
			self.Cmd_Open  = 0
		IO.DO_Open = self.Cmd_Open
		IO.DO_Close= self.Cmd_Close

class FIT_FBD:
	def __init__(self,HMI):
		self.Hty = HMI.Hty
		self.AHH = HMI.AHH
		self.AH = HMI.AH
		self.AL = HMI.AL
		self.ALL = HMI.ALL

	# def FIT_FBD(self, WRIO_Enb, Totaliser_Enb, IO,HMI,Sec_P):
	# 	Raw_RIO = IO.AI_Value
	# 	Raw_WRIO = IO.W_AI_Value
	# 	RIO_Hty = IO.AI_Hty
	# 	WRIO_Hty = IO.W_AI_Hty
	#
	# 	SAHH = HMI.SAHH
	# 	SAH  = HMI.SAH
	# 	SAL  = HMI.SAL
	# 	SALL = HMI.SALL
	# 	Simulation = HMI.Sim
	# 	Rst_Totaliser = HMI.Rst_Totaliser
	#
	# 	if WRIO_Enb:
	# 		self.Wifi_Enb = 1
	# 		Mid_Raw = Raw_WRIO
	# 		Mid_H_Raw = self.H_Raw_WRIO
	# 		Mid_L_Raw = self.L_Raw_WRIO
	# 		Mid_Inst_Hty = WRIO_Hty
	# 	else:
	# 		self.Wifi_Enb = 0
	# 		Mid_Raw = Raw_RIO
	# 		Mid_H_Raw = self.H_Raw_RIO
	# 		Mid_L_Raw = self.L_Raw_RIO
	# 		Mid_Inst_Hty = RIO_Hty
	# 	if Simulation:
	# 	   	HMI.Pv = HMI.Sim_PV
	# 	else:
	# 		Scale_Out = SCL( Mid_Raw, Mid_H_Raw, Mid_L_Raw, self.HEU, self.LEU)
	# 		if Scale_Out > 0:
	# 			HMI.Pv = Scale_Out
	# 		elif Scale_Out <= 0:
	# 			HMI.Pv = 0.0
	# 		HMI.Sim_Pv = HMI.Pv
	# 	self.AHH, self.AH, self.AL, self.ALL = ALM(HMI.Pv, SAHH, SAH, SAL, SALL)
	# 	if Totaliser_Enb:
	# 		if Sec_P:
	# 			HMI.Totaliser = HMI.Totaliser + abs(HMI.Pv)/3600
	# 	if Rst_Totaliser:
	# 		HMI.Totaliser = 0
	# 	self.Hty = Mid_Inst_Hty and (Mid_Raw > Mid_L_Raw) and (Mid_Raw > Mid_H_Raw)
	#
	# 	HMI.Hty = self.Hty
	# 	HMI.Wifi_Enb = self.Wifi_Enb
	# 	HMI.AHH = self.AHH
	# 	HMI.AH  = self.AH
	# 	HMI.AL  = self.AL
	# 	HMI.ALL = self.AHH

class PMP_FBD:
	def __init__(self,HMI):
		self.Cmd_Start = 0
		self.Avl = HMI.Avl
		self.Fault = HMI.Fault
		self.SD = bit_2_signed_integer(HMI.Shutdown)
		self.Fault = 0
		self.RunMin = 0
		self.Total_RunMin = 0
	def PMP_FBD(self, AutoInp,IO, HMI):
		Auto = HMI.Auto
		Remote = IO.DI_Auto
		Run    = IO.DI_Run
		Trip   = IO.DI_Fault
	
		Rst = HMI.Reset
		Permissive = bit_2_signed_integer(HMI.Permissive)
		self.a = Permissive
		Shutdown   = bit_2_signed_integer(HMI.SD)

		if not Run:
			HMI.Status = 1
		else:
			HMI.Status = 2
		if self.Fault:
			HMI.Fault = 1
		else:
			HMI.Fault = 0
		if HMI.Reset:
			self.SD = 0
		self.Fault = Trip or self.SD != 0
		HMI.Remote = Remote

		self.Avl = Auto and Remote and not self.Fault and self.SD == 0
		if Remote:
			if not Auto:
				pass
			else:
				if Run:
					self.Cmd = 2
				if not Run or self.Fault:
					self.Cmd = 1
				if AutoInp:
					if not self.Fault and Permissive == -1 and bit_2_signed_integer(HMI.SD)== 0:
						self.Cmd_Start = 1
					elif self.Cmd_Start or bit_2_signed_integer(HMI.SD) != 0 or self.Fault:
						self.SD = bit_2_signed_integer(HMI.SD)
						self.Cmd_Start = 0
				else:
					self.Cmd_Start = 0
		else:
			self.Cmd_Start = 0
			self.Cmd = 1
		
		HMI.Avl = self.Avl
		HMI.Fault = self.Fault
		HMI.Shutdown = signed_integer_2_bit(self.SD)
	
		IO.DO_Start = self.Cmd_Start
	

class Duty2_FBD:
	def __init__(self):
		self.Start_Pmp1 = 0
		self.Start_Pmp2 = 0
	def Duty2_FBD(self, AutoInp, PMP1,PMP2,HMI): #PMP1 and PMP2 should be the class of pump1 and pump2 	
		Selection = HMI.Selection

		if PMP1.Status == 2 or PMP2.Status ==2:
			HMI.Pump_Running = 1
		else:
			HMI.Pump_Running =0
		HMI.Both_Pmp_Not_Avl = not PMP1.Avl and not PMP2.Avl
		if AutoInp:
			if Selection == 1:
				if PMP1.Avl:
					self.Start_Pmp1 = 1
					self.Start_Pmp2 = 0
					HMI.Selected_Pmp_Not_Avl = 0
				elif not PMP1.Avl and PMP2.Avl:
					self.Start_Pmp1 = 0
					self.Start_Pmp2 = 1
					HMI.Selected_Pmp_Not_Avl = 1
				elif not PMP1.Avl and not PMP2.Avl:
					self.Start_Pmp1 = 0
					self.Start_Pmp2 = 0
				else:
					HMI.Selected_Pmp_Not_Avl = 0
			if Selection == 2:
				if PMP2.Avl:
					self.Start_Pmp1 = 0
					self.Start_Pmp2 = 1
					HMI.Selected_Pmp_Not_Avl = 0
				elif not PMP1.Avl and PMP2.Avl:
					self.Start_Pmp1 = 1
					self.Start_Pmp2 = 0
					HMI.Selected_Pmp_Not_Avl = 1
				elif not PMP1.Avl and not PMP2.Avl:
					self.Start_Pmp1 = 0
					self.Start_Pmp2 = 0
				else:
					HMI.Selected_Pmp_Not_Avl = 0
		else:
			self.Start_Pmp1 = 0
			self.Start_Pmp2 = 0

class SWITCH_FBD:
	def __init__(self,HMI):
		Delay = HMI.Delay
		self.TON_Delay = TONR(Delay)
	def SWITCH_FBD(self, IO,HMI):
		Alarm = IO.DI_LS	
		self.TON_Delay.TONR(Alarm)
		HMI.Status = self.TON_Delay.DN
		self.Status = self.TON_Delay.DN
		

class UV_FBD:
	def __init__(self,HMI):
		self.Cmd_Start  = 0
		self.Fault = 0
		self.Avl = HMI.Avl
		self.RunHr = HMI.RunHr
		self.Total_RunHr = HMI.RunHr
		self.SD = bit_2_signed_integer(HMI.Shutdown)

	def UV_FBD(self, AutoInp,IO, HMI):
		Remote = IO.DI_Auto
		Run    = IO.DI_Run
		Trip   = IO.DI_Fault

		Auto = HMI.Auto
		Rst  = HMI.Reset
		Rst_RunHr = HMI.Reset_RunHr
		Permissive = bit_2_signed_integer(HMI.Permissive)
		Shutdown = bit_2_signed_integer(HMI.SD)

		if not Run:
			HMI.Status = 1
		else:
			HMI.Status = 2
		if self.Fault:
			HMI.Fault = 1
		else:
			HMI.Fault = 0
		if HMI.Reset:

			self.SD = 0
		self.Fault = Trip
		HMI.Remote = Remote
		self.Avl = Auto and Remote and not self.Fault and  self.SD == 0
		if Remote:
			if Run:
				self.Cmd = 2
			if not Run or self.Fault:
				self.Cmd = 1
			if AutoInp:
				if not self.Fault and Permissive == -1 and bit_2_signed_integer(HMI.SD) == 0:
					self.Cmd_Start = 1
				elif self.Cmd_Start or bit_2_signed_integer(HMI.SD) != 0 or self.Fault:
					self.SD = bit_2_signed_integer(HMI.SD)
					self.Cmd_Start = 0
			else:
				self.Cmd_Start = 0
		else:
			self.Cmd_Start = 0
			self.Cmd = 1	

		
		HMI.Avl = self.Avl
		HMI.Fault = self.Fault

		HMI.RunHr = self.RunHr
		HMI.Total_RunHr = self.Total_RunHr
		HMI.Shutdown = signed_integer_2_bit(self.SD)
		IO.Start = self.Cmd_Start	

class VSD_FBD:
	def __init__(self, HMI):
		self.Fault = HMI.Fault

		self.SD = bit_2_signed_integer(HMI.Shutdown)
		self.RunMin = 0
		self.Total_RunMin = 0
		self.Speed = HMI.Speed
		self.Rdy = HMI.Drive_Ready
		

	def VSD_FBD(self, AutoInp, AutoSpeed, VSD_In, VSD_Out,IO, HMI ):
		Remote = IO.DI_Auto
		Run    = IO.DI_Run
		Start_PB = IO.DI_VSD_PB

		Trip = VSD_In.Faulted

		Auto = HMI.Auto
		Rst  = HMI.Reset
		Rst_RunHr = HMI.Reset_RunHr
		Speed_Cmd = HMI.Speed_Command
		Permissive = bit_2_signed_integer(HMI.Permissive)
		Shutdown = bit_2_signed_integer(HMI.SD)

		if not VSD_In.Active:
			HMI.Status = 1
		else:
			HMI.Status = 2
		self.Rdy = VSD_In.Ready
		self.Speed = VSD_In.OutputFreq
		HMI.Remote = Remote
		self.Avl = Auto and Remote and not self.Fault and self.SD == 0
		HMI.Fault = VSD_In.Faulted or Trip or self.SD
		if VSD_In.Active:
			HMI.Cmd = 2  # Cmd or HMI.Cmd, the original code is realy ambiguous
		if not VSD_In.Active or VSD_In.Faulted:
			HMI.Cmd = 1
		if AutoInp:
			if not VSD_In.Faulted and Permissive == -1 and bit_2_signed_integer(
					HMI.SD) == 0:
				VSD_Out.Start = 1
				VSD_Out.Stop = 0
				VSD_Out.FreqCommand = AutoSpeed * 100
			elif VSD_Out.Start or bit_2_signed_integer(HMI.SD) != 0 or self.Fault:
				self.SD = bit_2_signed_integer(HMI.SD)
				VSD_Out.Start = 0
				VSD_Out.Stop = 0
				HMI.Cmd = 1
			if not VSD_In.ACtive:
				VSD_Out.Start = 0
				VSD_Out.Stop = 1
				VSD_Out.FreqCommand = AutoSpeed * 100
				HMI.Cmd = 1
		else:
			VSD_Out.Start = 0
			VSD_Out.Stop = 1
				

		HMI.Avl = self.Avl
		HMI.Fault = self.Fault
		HMI.Speed = self.Speed
		HMI.Drive_Ready = self.Rdy
		HMI.Shutdown = signed_integer_2_bit(self.SD)
