def dec2bin(num):
	rem = ''
	while num!=0:
		rem += str(num%2)
		num = num//2
	rem = rem[::-1]
	print(f'binary: {int(rem)}')

def bin2dec(num):
	dig = len(str(num))
	sum_ = 0
	dig_rev = str(num)[::-1]
	for i in range(0, dig):
		sum_+=int(dig_rev[i])*(2**i)
	print(f'decimal: {sum_}')
	return sum_

def dec2hex(num):
	rem_ = ''
	while num!=0:
		rem = num%16
		if rem > 9:
			if rem == 10:
				rem_+='A'
			elif rem == 11:
				rem_+='B'
			elif rem == 12:
				rem_+='C'
			elif rem == 13:
				rem_+='D'
			elif rem == 14:
				rem_+='E'
			elif rem == 15:
				rem_+='F'
		else:
			rem_+=str(num%16)

		num = num//16
	rem = rem_[::-1]
	print(f'Hexadecimal: {rem}')

def hex2dec(num):
	dig = len(num)
	sum_ = 0
	dig_rev = num[::-1]
	for i in range(0, dig):
		if dig_rev[i] == 'A':
			sum_+=10*(16**i)
		elif dig_rev[i] == 'B':
			sum_+=11*(16**i)
		elif dig_rev[i] == 'C':
			sum_+=12*(16**i)
		elif dig_rev[i] == 'D':
			sum_+=13*(16**i)
		elif dig_rev[i] == 'E':
			sum_+=14*(16**i)
		elif dig_rev[i] == 'F':
			sum_+=15*(16**i)
		else:
			sum_+=int(dig_rev[i])*(16**i)
	print(f'Decimal: {sum_}')
	return sum_

def dec2oct(num):
	rem = ''
	while num!=0:
		rem += str(num%8)
		num = num//8
	rem = rem[::-1]
	print(f'binary: {int(rem)}')

def oct2dec(num):
	dig = len(str(num))
	sum_ = 0
	dig_rev = str(num)[::-1]
	for i in range(0, dig):
		sum_+=int(dig_rev[i])*(8**i)
	print(f'decimal: {sum_}')
	return sum_

def bin2hex(num):
	dec = bin2dec(num)
	dec2hex(dec)

def hex2bin(num):
	dec = hex2dec(num)
	dec2bin(num)

def bin2oct(num):
	dec = bin2dec(num)
	dec2oct(dec)

def oct2bin(num):
	dec = oct2dec(num)
	dec2bin(dec)

def oct2hex(num):
	dec = oct2dec(num)
	dec2hex(dec)

def hex2oct(num):
	dec = hex2dec(num)
	dec2oct(dec)

def convert_radix(a, b, num):
	lon = [i for i in range(10, 36)]
	# print(lon)
	loa = [chr(i) for i in range(65, 65+len(lon))]
	# print(loa)
	d = {}
	d_r = {}
	for i, n in enumerate(lon):
		d[n] = loa[i]
		d_r[loa[i]] = lon[i]
	dig = len(str(num))
	sum_ = 0
	# print(num)
	# print(d_r)
	dig_rev = num[::-1]
	# print(dig_rev)
	for i in range(0, dig):
		# print((dig_rev[i]))
		if dig_rev[i] in loa:
			sum_ += (d_r[dig_rev[i]])*(a**i)
		else:
			sum_+=int(dig_rev[i])*(a**i)
	rem_ = ''
	while sum_!=0:
		rem = sum_%b
		if rem>9:
			rem_ += d[rem]
		else:
			rem_+=str(sum_%b)
		sum_ = sum_//b
	rem_ = rem_[::-1]
	print(rem_)


print('1. binary to decimal: ')
print('2. decimal to binary: ')
print('3. decimal to hexadecimal: ')
print('4. hexadecimal to decimal: ')
print('5. octal to decimal: ')
print('6. binary to hexadecimal: ')
print('7. hexadecimal to binary: ')
print('8. binary to octal: ')
print('9. octal to binary: ')
print('10. octal to hexadecimal: ')
print('11. hexadecimal to octal: ')
print('12. A to B: ')
print('13. exit ')

while True:
	choice = int(input("Enter choice No.: "))
	if choice == 1:
		num = int(input("Enter binary: "))
		_ = bin2dec(num)

	elif choice == 2:
		num = int(input("Enter decimal: "))
		dec2bin(num)

	elif choice == 3:
		num = int(input("Enter decimal: "))
		dec2hex(num)

	elif choice == 4:
		num = int(input("Enter hexadecimal: "))
		_ = hex2dec(num)

	elif choice == 5:
		num = int(input("Enter decimal: "))
		dec2bin(num)

	elif choice == 6:
		num = int(input("Enter binary: "))
		bin2hex(num)

	elif choice == 7:
		num = int(input("Enter hexadecimal: "))
		hex2bin(num)

	elif choice == 8:
		num = int(input("Enter binary: "))
		bin2oct(num)

	elif choice == 9:
		num = int(input("Enter octal: "))
		oct2bin(num)

	elif choice == 10:
		num = int(input("Enter octal: "))
		oct2hex(num)

	elif choice == 11:
		num = int(input("Enter hexadecimal: "))
		hex2oct(num)

	elif choice == 12:
		A = int(input("Enter A: "))
		B = int(input("Enter B: "))
		num = input("Enter num: ")
		convert_radix(A, B, num)
	elif choice == 13:
		break