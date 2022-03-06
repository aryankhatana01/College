def noteCreate():
	major = 'W W H W W W H'.split(' ')
	minor = 'W H W W H W W'.split(' ')
	f = open('scaleMajor.txt', 'w')
	g = open('scaleMinor.txt', 'w')
	notes = ("C C# D D# E F F# G G# A A# B C'".split(' '))*2
	for i in range(12):
		root = notes[i]
		final_note = f'{root}'
		k=i
		for step in major:
			if step == 'W':
				final_note+=f',{notes[k+2]}'
				k+=2
			else:
				final_note+=f',{notes[k+1]}'
				k+=1
		f.write(final_note+'\n')
	f.close()

	for i in range(12):
		root = notes[i]
		final_note = f'{root}'
		k=i
		for step in minor:
			if step == 'W':
				final_note+=f',{notes[k+2]}'
				k+=2
			else:
				final_note+=f',{notes[k+1]}'
				k+=1
		g.write(final_note+'\n')
	g.close()


def majorNotes(root):
	noteCreate()
	with open('scaleMajor.txt', 'r') as f:
		notes = f.read().splitlines()
		for note in notes:
			if note[:2] == f'{root},':
				print(note)


def minorNotes(root):
	noteCreate()
	with open('scaleMinor.txt', 'r') as f:
		notes = f.read().splitlines()
		for note in notes:
			if note[:2] == f'{root},':
				print(note)

while True:
	root = input("Enter the root node: ")
	scale = input("Enter the scale: ")

	if scale == 'Major':
		majorNotes(root)
	elif scale == 'Minor':
		minorNotes(root)

	else:
		break
