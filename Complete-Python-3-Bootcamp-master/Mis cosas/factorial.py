import math as m

n = 152398989


def fermat(l, n):
	mini = 0.0000001
	for xi in range (m.ceil(n**0.5), n+1):
		y = (xi**2 - n) ** 0.5
		if (y.is_integer()):
			a = 





