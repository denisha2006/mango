def minimax(d, n, maxp, a, b):
	if d == depth:
		return tree[n]
	
	if maxp:
		v = -999
		for i in range(2):
			v = max(v, minimax(d+1, n*2+i, False, a, b))
			a = max(v, a)
			if b <= a:
				print(f"Node pruned having a={a} and b={b}")
				break
		return v

	else:
		v = 999
		for i in range(2):
			v = min(v, minimax(d+1, n*2+i, True, a, b))
			b = min(b, v)
			if b <= a:
				print(f"Node pruned having a={a} and b={b}")
				break
		return v

tree = list(map(int, input("Enter the leaf nodes: ").split()))
depth = 0
while 2**depth < len(tree):
	depth += 1

if 2**depth != len(tree):
	print("Enter the values in power of 2, eg. 4, 8, 16, 32, etc.")
else:
	print("Optimal value is:", minimax(0, 0, True, -999, 999))
