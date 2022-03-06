import glob

def read_students(f):
	marked = f.read().splitlines()
	for i in range(len(marked)):
		marked[i] = marked[i].split(' ')[1]
	return marked

g = open('/Users/0x4ry4n/Desktop/College/A2_Aryan_2021237/Q4/Admin/AnswerKey.txt', 'r')
correct_ans = g.read().splitlines()
for i in range(len(correct_ans)):
		correct_ans[i] = correct_ans[i].split(' ')[1]
# print(correct_ans)

def evaluate(options_marked, correct_ans):
	score = 0
	for i, marked in enumerate(options_marked):
		if marked == correct_ans[i]:
			score+=4
		elif marked == '-':
			score+=0
		elif marked != correct_ans[i]:
			score-=1
	return score

ev = open('FinalReport.txt', 'a')
file_paths = [x for x in glob.glob('/Users/0x4ry4n/Desktop/College/A2_Aryan_2021237/Q4/Student/*.txt')]
for student in file_paths:
	s = student.split('/')[8][:-4]
	name = s.split('_')[0]
	number = s.split('_')[1]
	f = open(student, 'r')
	options_marked = read_students(f)
	# print(options_marked)
	score = evaluate(options_marked, correct_ans)
	ev.write(f'{name} {number} {str(score)}\n')
	
	