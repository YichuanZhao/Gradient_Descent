import numpy as np

def evalluate_func(x1, x2):

	return x1**3/3 + x2**2*x1 - 3*x1

def evalluate_defunc(x1, x2):

	return x1**2 + x2**2 - 3, 2*x1*x2

def get_paras(a1, a2, b1, b2):

	p1 = -b1**3 - 2.0*b1*b2**2 - b1*b2**2
	p2 = 2.0*a1*b1**2 + 2.0*a1*b2**2 + 2.0*a2*b1*b2 + 2.0*a2*b1*b2
	p3 = -a1**2*b1 - 2.0*a1*a2*b2 - a2**2*b1 + 3.0*b1

	return p1, p2, p3

def get_roots(a, b, c, s):

	test = b**2 - 4.0*a*c

	r1 = 0.0

	if test >= 0:

		if s == 1:
			r1 = (-b + (b**2 - 4.0*a*c)**0.5)/(2.0*a)
		else:
			r1 = (-b - (b**2 - 4.0*a*c)**0.5)/(2.0*a)

	else:
		r1 = -b/(2.0*a)

	
	return r1
	

def steepest_descent(x1 ,x2, s):

	thre = 1e-6

	a, b = evalluate_defunc(x1, x2)

	check = (a**2 + b**2)**0.5 

	index = 0

	t = 0

	while check > thre:

		p1, p2, p3 = get_paras(x1, x2, a, b)

		if s == 1:
			t = get_roots(p1, p2, p3, s)
		else:
			t = get_roots(p1, p2, p3, s)

		# print t

		x1 = x1 - t*a
		x2 = x2 - t*b

		a, b = evalluate_defunc(x1, x2)

		check = (a**2 + b**2)**0.5

		index = index + 1

	return x1, x2




x1_min, x2_min = steepest_descent(0, 0, 1)

print 'A local minimum locates at ( ' + str(x1_min) + ', ' + str(x2_min) + ' )' 

x1_max, x2_max = steepest_descent(0, 0, 0)

print 'A local maximum locates at ( ' + str(x1_max) + ', ' + str(x2_max) + ' )' 


