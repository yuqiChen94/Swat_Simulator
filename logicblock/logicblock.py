import inspect
import types
class switch(object):
    value = None

    def __new__(class_, value):
        class_.value = value
        return True


def case(*args):
    return any((arg == switch.value for arg in args))


# class switch and func case are to create the case statement which python doesn't provide

def SETD(a, b, c):
    if b == 1:  # if unset is set, must stop
        return 0
    elif a == 1:  # else if set is set, can run
        return 1
    # if a == 1 and b == 1:
    #	print "Error: SETD input cannot be 1 and 1"
    else:  # if neither is set, keep current state
        return c


# def ALM(in_sig,a_hh,a_h,a_l,a_ll):
# 	if in_sig < a_ll:
# 		d = 1
# 	else:
# 		d = 0
# 	if in_sig < a_l:
# 		c = 1
# 	else:
# 		c = 0
# 	if in_sig > a_h:
# 		b = 1
# 	else:
# 		b = 0
# 	if in_sig > a_hh:
# 		a = 1
# 	else:
# 		a = 0
# 	return a,b,c,d

def ALM(in_val, a_hh, a_h, a_l, a_ll):

    if in_val < a_ll:
        d = 1
    else:
        d = 0
    if in_val < a_l:
        c = 1
    else:
        c = 0
    if in_val > a_h:
        b = 1
    else:
        b = 0
    if in_val > a_hh:
        a = 1
    else:
        a = 0
    return a, b, c, d


# def SCL(In, InRawMax, InRawMin, InEuMax, InEuMin):
#     Out = (In - InRawMin) * float(InEuMax - InEuMin) / float(InRawMax - InRawMin) + InEuMin
#     return Out


class TONR:
    def __init__(self, preset, name=None):
        self.Acc = 0
        self.preset = preset * 200  # count every 5 miliseconds
        self.DN = 0
        self.name = name

    # def get_my_name(self):
    # 	ans = []
    # 	frame = inspect.currentframe().f_back
    # 	tmp = dict(frame.f_globals.items() + frame.f_locals.items())
    # 	for k, var in tmp.items():
    # 		if isinstance(var, self.__class__):
    # 			if hash(self) == hash(var):
    # 				ans.append(k)
    # 	return ans

    def TONR(self, TimerEnable):
        if self.Acc == self.preset:
            # print 'stop'
            self.Acc = 0
            self.DN = 1
        else:
            self.DN = 0
            if TimerEnable:
                if self.name != None:
                    print(self.name)
                self.Acc += 1
            else:
                self.Acc = 0


def bit_2_signed_integer(arr):
    out = 0
    for i in range(1, len(arr)):
        out += 2 ** (i - 1) * arr[i]
    return out - 2 ** (len(arr) - 1) * arr[0]


def signed_integer_2_bit(value):
    a = [1] * 32
    if value >= 0:
        a[0] = 0
    for i in range(1, 32):
        a[i] = value % 2
        value = value - value
    return a

# def signed_integer_2_bit(value):
# 	a = [1] * 32
# 	if value >=0:
# 		a[0] = 0
# 	for i in xrange(1,32):
# 		a[i] = value % 2
# 		value = value - value
# 	return a
