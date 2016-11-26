import math

memoncr = {}
memofact = {}
def fact(n):
	if n not in memofact:
		memofact[n] = math.factorial(n)
	return memofact[n]

def nCr(n, r):
	if r == 0 or n == r:
		return 1
	if r > n:
		return 0
	if (n,r) not in memoncr:
		memoncr[(n,r)] = fact(n)//(fact(r)*fact(n-r))
	return memoncr[(n,r)]