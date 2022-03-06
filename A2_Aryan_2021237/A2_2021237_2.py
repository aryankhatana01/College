import math

n = int(input("Enter number of Vertices: "))
x = [int(x) for x in input("Enter X: ").split(' ')]
y = [int(y) for y in input("Enter Y: ").split(' ')]
z = [int(z) for z in input("Enter Z: ").split(' ')]
q = int(input("Number of transormations queries: "))
queries = {}
for i in range(q):
	queries[f'query_{i}'] = input("Enter query: ")

matr = [x, y, z, [0]*(n-1)]
matr[3].append(1)
print(matr)
# print([[0]*n, [0]*n, [0]*n, [0]*n])
def scaling_T(sx, sy, sz):
	result = [[0]*n, [0]*n, [0]*n, [0]*n]
	T = [[sx, 0, 0, 0], [0,sy, 0, 0], [0, 0, sz, 0], [0, 0, 0, 1]]
	for i in range(len(T)):
		for j in range(len(matr[0])):
 			for k in range(len(matr)):
	 			result[i][j] += T[i][k] * matr[k][j]

	return result

def translating_T(tx, ty, tz):
	result = [[0]*n, [0]*n, [0]*n, [0]*n]
	T = [[1,0,0,tx], [0,1,0,ty], [0,0,1,tz], [0,0,0,1]]
	for i in range(len(T)):
		for j in range(len(matr[0])):
			for k in range(len(matr)):
				result[i][j] += T[i][k] * matr[k][j]
	return result

def rotation_T(axis, phi):
	Tz = [[math.cos(math.radians(phi)), -1*math.sin(math.radians(phi)), 0, 0], [math.sin(math.radians(phi)), math.cos(math.radians(phi)), 0, 0], [0,0,1,0], [0,0,0,1]]
	Tx = [[1,0,0,0], [0, math.cos(math.radians(phi)), -1*math.sin(math.radians(phi)), 0], [0,math.sin(math.radians(phi)), math.cos(math.radians(phi)),0], [0,0,0,1]]
	Ty = [[math.cos(math.radians(phi)),0,math.sin(math.radians(phi)),0], [0, 1, 0, 0], [-1*math.sin(math.radians(phi)),0, math.cos(math.radians(phi)),0], [0,0,0,1]]
	if axis == 'x':
		result = [[0]*n, [0]*n, [0]*n, [0]*n]
		for i in range(len(Tx)):
			for j in range(len(matr[0])):
				for k in range(len(matr)):
					result[i][j] += Tx[i][k] * matr[k][j]
		return result

	elif axis == 'y':
		result = [[0]*n, [0]*n, [0]*n, [0]*n]
		for i in range(len(Ty)):
			for j in range(len(matr[0])):
				for k in range(len(matr)):
					result[i][j] += Ty[i][k] * matr[k][j]
		return result

	elif axis == 'z':
		result = [[0]*n, [0]*n, [0]*n, [0]*n]
		for i in range(len(Tz)):
			for j in range(len(matr[0])):
				for k in range(len(matr)):
					result[i][j] += Tz[i][k] * matr[k][j]
		return result



for query in queries.values():
	ind_terms = [x for x in query.split(' ')]
	if ind_terms[0] == 'S':
		sx = int(ind_terms[1])
		sy = int(ind_terms[2])
		sz = int(ind_terms[3])
		matr = scaling_T(sx, sy, sz)
	elif ind_terms[0] == 'T':
		tx = int(ind_terms[1])
		ty = int(ind_terms[2])
		tz = int(ind_terms[3])
		matr = translating_T(tx, ty, tz)
	elif ind_terms[0] == 'R':
		axis = ind_terms[1]
		phi = int(ind_terms[2])
		matr = rotation_T(axis, phi)

f = open('matix.txt', 'w+')
f.write(str(matr))
print(matr)


# print(scaling_T(2,1,1))


	


