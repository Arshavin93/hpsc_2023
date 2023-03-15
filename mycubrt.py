"""
A python module for calculating cube root of a number using Newton's method implemented as an assignment
"""
def cubrt(x,debug=False,cases=True):
	"""
	User defined cubrt function
	Inputs
	x: The number of which cube root is to be calculated
	debug: True if iterations values are to be printed. Default value is false
	cases: False to disable zero and negative number check, Default value of True
	
	"""
	
	from numpy import nan
	
	if cases:
		if x==0:
			return 0
		elif x<0:
			print("An error has occured since you have passed a negative value of x which is not a real number")
			return nan
	assert x>0
	s=1
	kmax=100
	tol=1e-14
	for k in range (kmax):
		if debug:
			print("At iteration number %s, s=%20.15f" %(k,s))
		s0=s
		s=(1/3)*(2*s+(x/(s**2)))
		delta_s=s-s0
		if abs((delta_s/x))<tol:
			break
	if debug:
		print("After %s iteration, s=%20.15f" %(k+1,s))
	return s

def test_main():
	from numpy import cbrt
	xvalues=[0 , 9 , 1000 , 1e12]
	for x in xvalues:
		print("Testing with x=%20.15e" %x)
		s=cubrt(x)
		s_numpy=cbrt(x)
		print("cubrt s = %20.15e, numpy s = %20.15e" %(s,s_numpy))
		assert abs(s-s_numpy) < 1e-14, "Your cube root does not agree with numpy cube root"
