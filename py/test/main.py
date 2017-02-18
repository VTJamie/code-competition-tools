import math
import sys
import inflect
from collections import deque

import string


def load_file_stdin(filename):
	
	sys.stdin = open(filename)

def isprime(n):
	s = int(math.sqrt(n)+1)
	if n == 2:
		return True
	for i in range(2, s):
		if n%i == 0:
			return False
	return True
	

if __name__ == '__main__':	
	input = raw_input
	

	a = [2, 3, 5, -8, 1]
	s = 0
	sr = 0
	for n in a:
		s = s + n
		if sr ^ s - sr == s:
			print 'OMG'
		sr = sr ^ s

		print sr - s, s















