class pump:
	def __init__(self):
		self.DI_auto  = 0
		self.DI_fault = 0
		self.DI_run   = 0
# above attributes are output signal to plc
# below attributes are intake signal from plc
		self.DO_start = 0


class motorvalve:
	def __init__(self):
		self.DI_zso   = 0
		self.DI_zsc   = 0
# above attributes are output signal to plc
# below attributes are intake signal from plc
		self.DO_Open  = 0
		self.DO_Close = 0

class uv: # ultra violet
	def __init__(self):
		self.DI_auto = 0
		self.DI_run = 0
		self.DI_fault = 0
		# above attributes are output signal to plc
		# below attributes are intake signal from plc
		self.DO_start = 0

class vsd_in:
	def __init__(self):
		self.Ready = 0
		self.OutputFreq = 0
		self.Active = 0
		self.Faulted = 0


class vsd_out:
	def __init__(self):
		self.Start = 0
		self.Stop = 0
		self.ClearFaults = 0
		self.FreqCommand = 0
