class DI_WIFI: # self.RIO represents a switch, if it's 1`, then PLC processes wireless signal.
	def __init__(self):
		self.PLC = 0
		self.RIO1 = 0 
		self.RIO2 = 0 
		self.RIO3 = 0 
		self.RIO4 = 0 
		self.RIO5 = 0 
		self.RIO6 = 0 

class IO_AIN_FIT: # AIN_FBD and FIT_FBD both use this I/O
	def __init__(self):#,AI_Value, W_AI_Value):
		self.AI_Value   = 0#AI_Value
		self.W_AI_Value = 0#W_AI_Value
		self.AI_Hty     = 1 
		self.W_AI_Hty   = 1 


class IO_PMP_UV: # PMP_FBD and UV_FBD both use this I/O
	def __init__(self):
		self.DI_Auto = 1
		self.DI_Run  = 0
		self.DI_Fault = 0
		self.DO_Start = 0

class IO_SWITCH:
	def __init__(self):
		self.DI_LS = 0

class IO_MV:
	def __init__(self):
		self.DI_ZSO = 0
		self.DI_ZSC = 1
		self.DO_Open = 0
		self.DO_Close = 0
class VSD:
	def __init__(self):
		self.DI_Auto = 1
		self.DI_Run  = 0
		self.DI_VSD_PB = 0

class VSD_In: 
	def __init__(self):
		self.Faulted = 0
		self.Active  = 0
		self.Ready   = 0
		self.OutputFreq = 0


class VSD_Out:
	def __init__(self):
		self.ClearFaults = 0
		self.Start = 0
		self.Stop  = 0
		self.FreqCommand = 0

