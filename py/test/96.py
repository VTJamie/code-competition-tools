import math
import sys


fullset = set([1, 2, 3, 4, 5, 6, 7, 8, 9])


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


def getnextpuzzle():
	input()
	g = []
	for n in range(9):
		g.append(list(map(int, input())))

	return g


def get_row_vals(row, g):
	retset = set()
	for n in g[row]:
		if n != 0:
			retset.add(n)

	return retset
def get_col_vals(col, g):	
	retset = set()
	for n in range(9):
		if g[n][col] != 0:
			retset.add(g[n][col])			
	return retset

def get_sector_vals(row, col, g):
	retset = set()

	srow = 3*(row//3)
	scol = 3*(col//3)
	for r in range(srow, srow+3):
		for c in range(scol, scol+3):
			if g[r][c] != 0:
				retset.add(g[r][c])

	return retset

def gettakenvals(row, col, g):
	return get_row_vals(row, g) | get_col_vals(col, g) | get_sector_vals(row, col, g)

def debug(g):
	for row in g:
		for val in row:
			print val,

		print 


def filleasy(g):

	mademove = True
	while mademove:
		mademove = False		
		for row in range(9):
			for col in range(9):
				if g[row][col] == 0:
					rem = fullset - gettakenvals(row, col, g)
					if len(rem) == 1:
						g[row][col] = list(rem)[0]
						mademove = True

def fillhard(g):
	return False

def completecheck(g):	
	for row in range(9):
		for col in range(9):
			if g[row][col] == 0:
				return False

	return True

def solve(g):
	while not completecheck(g):
		filleasy(g)
		fillhard(g)


if __name__ == '__main__':	
	input = raw_input
	load_file_stdin('p096_sudoku.txt')
	for t in range(10):
		g = getnextpuzzle()
		#print get_col_vals(0, g)
		#print get_row_vals(0, g)	
		
		filleasy(g)		
		if not completecheck(g):
			debug(g)
			print
		


