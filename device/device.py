# The sensors would return values not in physical unit. e.g. 0.7 meter tank level would be returned by ultra sonic level sensor to PLC as some value like 32940.
def usl_w(level): #ultra sonic level sensor wireless
	return (level - 0.0) * float(0-31208)/float(1225-0.0) + 31208

def usl(level): #ultra sonic level sensor 
	return (level - 0.0) * float(3277-16383)/float(1225-0.0) + 16383 

def fi_w(flow): #flow indicator wireless
	return (flow - 0.0) * float(-15-31208)/float(10-0.0) + 31208 

def fi(flow): #flow indicator
	return (flow - 0.0) * float(3277-16383)/float(10-0.0) + 16383 




