from io_plc.IO_PLC import *

class P1:
	def __init__(self):
		# P1
		self.LIT101 = IO_AIN_FIT()
		self.FIT101 = IO_AIN_FIT() 
		self.MV101  = IO_MV() 
		self.P101   = IO_PMP_UV()
		self.P102   = IO_PMP_UV()
class P2:
	def __init__(self):
		# P2
		self.LS201  = IO_SWITCH()
		self.LS202  = IO_SWITCH()
		self.LSL203  = IO_SWITCH()
		self.LSLL203  = IO_SWITCH()
		self.MV201  = IO_MV()
		self.P201   = IO_PMP_UV()
		self.P202   = IO_PMP_UV()
		self.P203   = IO_PMP_UV()
		self.P204   = IO_PMP_UV()
		self.P205   = IO_PMP_UV()
		self.P206   = IO_PMP_UV()
		self.P207   = IO_PMP_UV()
		self.P208   = IO_PMP_UV()
		self.FIT201 = IO_AIN_FIT()
		self.AIT201 = IO_AIN_FIT()
		self.AIT202 = IO_AIN_FIT()
		self.AIT203 = IO_AIN_FIT()
class P3:
	def __init__(self):
		# P3
		self.LIT301 = IO_AIN_FIT()
		self.FIT301 = IO_AIN_FIT()
		self.P301   = IO_PMP_UV()
		self.P302   = IO_PMP_UV()
		self.PSH301 = IO_SWITCH()
		self.DPSH301= IO_SWITCH()
		self.DPIT301= IO_AIN_FIT()
		self.MV301  = IO_MV()
		self.MV302  = IO_MV()
		self.MV303  = IO_MV()
		self.MV304  = IO_MV()
class P4:
	def __init__(self):
		# P4
		self.LS401  = IO_SWITCH()
		self.LIT401 = IO_AIN_FIT()
		self.UV401  = IO_PMP_UV()
		self.P401   = IO_PMP_UV()
		self.P402   = IO_PMP_UV()
		self.P403   = IO_PMP_UV()
		self.P404   = IO_PMP_UV()
		self.AIT401 = IO_AIN_FIT()
		self.AIT402 = IO_AIN_FIT()
		self.FIT401 = IO_AIN_FIT()
class P5:
	def __init__(self):
		# P5
		self.AIT501 = IO_AIN_FIT()
		self.AIT502 = IO_AIN_FIT()
		self.AIT503 = IO_AIN_FIT()
		self.AIT504 = IO_AIN_FIT()
		self.PIT501 = IO_AIN_FIT()
		self.PIT502 = IO_AIN_FIT()
		self.PIT503 = IO_AIN_FIT()
		self.FIT501 = IO_AIN_FIT()
		self.FIT502 = IO_AIN_FIT()
		self.FIT503 = IO_AIN_FIT()
		self.FIT504 = IO_AIN_FIT()
		self.MV501  = IO_MV()
		self.MV502  = IO_MV()
		self.MV503  = IO_MV()
		self.MV504  = IO_MV()
#for Pressure Pump, we have VSD IO(normal) and VSD_In and VSD_Out, in total 3 I/O
		self.P501   = VSD()
		self.P502   = VSD() 
		self.P501_VSD_In  = VSD_In()
		self.P502_VSD_In  = VSD_In()
		self.P501_VSD_Out = VSD_Out()
		self.P502_VSD_Out = VSD_Out()
class P6:
	def __init__(self):
		# P6
		self.LSL601  = IO_SWITCH()
		self.LSL602  = IO_SWITCH()
		self.LSL603  = IO_SWITCH()
		self.LSH601  = IO_SWITCH()
		self.LSH602  = IO_SWITCH()
		self.LSH603  = IO_SWITCH()
		self.P601   = IO_PMP_UV()
		self.P602   = IO_PMP_UV()
		self.P603   = IO_PMP_UV()
		self.FIT601 = IO_AIN_FIT()

