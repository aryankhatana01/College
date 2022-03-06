f = open('data.txt', 'r')
def spec_word(word):
	lines_list = f.readlines()
	low = []
	for line in lines_list:
		line = line[:-1]
		for words in line.split(' '):
			low.append(words)

	for i, word_ in enumerate(low):
		low[i] = word_.lower()
	word = word.lower()
	cnt = 0
	for word_ in low:
		if word == word_:
			cnt+=1
	if cnt>0:
		return cnt
	if cnt == 0:
		return 'Word does not exist'

def disp_uni_word():
	lines_list = f.readlines()
	low = []
	for line in lines_list:
		line = line[:-1]
		for words in line.split(' '):
			low.append(words)

	for i, word_ in enumerate(low):
		low[i] = word_.lower()
	word_cnt = {}
	for word in low:
		cnt = spec_word(word)
		if word not in word_cnt.keys():
			word_cnt[word] = 0
		word_cnt[word]+=1
	for word, cnt in word_cnt.items():
		if cnt == 1:
			print(word, end = ';')

def all_count():
	lines_list = f.readlines()
	low = []
	for line in lines_list:
		line = line[:-1]
		for words in line.split(' '):
			low.append(words)

	for i, word_ in enumerate(low):
		low[i] = word_.lower()
	word_cnt = {}
	for word in low:
		cnt = spec_word(word)
		if word not in word_cnt.keys():
			word_cnt[word] = 0
		word_cnt[word]+=1
	# print(word_cnt)
	for word, cnt in word_cnt.items():
		print(f'{word}:{cnt}')


def replace_word(word1, word2):
	lines_list = f.readlines()
	new_ll = []
	for line in lines_list:
		line = line[:-1]
		line = line.replace(word1, word2)
		new_ll.append(line)
	new_data = "".join(new_ll)
	f_ = open('data.txt', 'w')
	f_.write(new_data)
	print('replaced successfully!!')


while True:
	print("1. Display spec Word Count")
	print("2. Display all unique word")
	print("3. Display all Word Counts")
	print("4. Replace Word")
	print("5. quit")

	choice = int(input("Enter Choice number: "))
	if choice == 1:
		word = input("Enter word: ")
		print(f'Word count: {spec_word(word)}')
	elif choice == 2:
		disp_uni_word()
	elif choice == 3:
		all_count()
	elif choice == 4:
		word1 = input("Ebter word to replace: ")
		word2 = input("Enter word to be replaced with: ")
		_ = replace_word(word1, word2)
	elif choice ==5:
		break
