N = int(input("Enter the value for N: "))
matr = {}
for i in range(N):	
	matr[f'row_{i+1}'] = [str(x) for x in input("Enter first row(space separated): ").split(' ')]

def normal(matr):
	final = ''
	for row in matr.keys():
		for ele in matr[row]:
			final+=f'{str(ele)} '
	print(final)

def alternating(matr):
	final = ''
	for row in matr.keys():
		if int(row[-1])%2==0:
			matr[row].reverse()
			for ele in matr[row]:
				final+=f'{str(ele)} '
		else:
			for ele in matr[row]:
				final+=f'{str(ele)} '
	print(final)

def boundary(matr):
	final = ''
	for ele in matr['row_1']:
		final+=f'{ele} '
	for row in matr.keys():
		if row != 'row_1':
			final+=f'{matr[row][-1]} '
	for ele in reversed(matr[f'row_{N}']):
		if ele!= matr[f'row_{N}'][-1]:
			final+=f'{ele} '
	rev_keys = []
	for row in matr.keys():
		rev_keys.append(row)
	for row in reversed(rev_keys):

		if row != f'row_{N}':
			final+=f'{matr[row][0]} '
	print(final[:-2])

def diaglr(matr):
	final = ''
	for i in range(N):
		row_num = 1
		j = i
		while j>=0 and row_num<=N:
			final+=f"{str(matr[f'row_{row_num}'][j])} "
			row_num+=1
			j-=1

	for i in range(2,N+1):
		row_num=i
		j=-1
		while j>=(-1*N) and row_num<=N:
			final+=f"{str(matr[f'row_{row_num}'][j])} "
			row_num+=1
			j-=1


	print(final)

def diagrl(matr):
	new_matr = {}
	for row in matr.keys():
		new_matr[row] = matr[row][::-1]

	final = ''
	for i in range(N):
		row_num = 1
		j = i
		while j>=0 and row_num<=N:
			final+=f"{str(new_matr[f'row_{row_num}'][j])} "
			row_num+=1
			j-=1

	for i in range(2,N+1):
		row_num=i
		j=-1
		while j>=(-1*N) and row_num<=N:
			final+=f"{str(new_matr[f'row_{row_num}'][j])} "
			row_num+=1
			j-=1


	print(final)
	


while True:
	print('1. Normal')
	print('2. Alternating')
	print('3. Boundary')
	print('4. Diagonal(left to right)')
	print('5. Diagonal(right to left)')
	print('6. Exit')
	choice  = int(input("Enter choice: "))

	if choice == 1:
		normal(matr)
	elif choice == 2:
		alternating(matr)
	elif choice == 3:
		boundary(matr)
	elif choice == 4:
		diaglr(matr)
	elif choice ==5:
		diagrl(matr)
	elif choice ==6:
		break


# 1  2  3   4   17
# 5  6  7   8   18
# 9  10 11  12  19
# 13 14 15  16  20
# 13 14 15  16  20

# d = {1:'rwr', 2:'sgr', 3:'sdg'}
# print(d.keys(-1))