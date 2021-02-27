import random, os

with open("word.txt") as f:
  dictionary = {line.split(' - ')[1]: line.replace('\n','').split(' - ')[0] for line in f}
  f.close()



wordcount = 1
wordList, userDict = {}, {}

for x in range(wordcount):
  i = random.choice(list(dictionary.items()))
  wordList[i[0]] = i[1]

word = list(wordList.keys())

while len(word) > 0:
  term = word.pop()
  userDict[term] = input(f'\n{term}>>> ')
  
  if len(word) == 0:
    print('\n\nDone!')



def check(function):
	def score(incorrect, correct):
		for key, val in wordList.items():
			for term, answer in userDict.items():
				if key ==term and val == answer:
					correct+= 1
				elif key == term and answer != val:
					incorrect.append([key, val, answer])
		function([], 0)
	return score
	

@check
def results():
  os.system('clear')
  print(f'Your score is: {correct}/{wordcount}\n\n\n')
  for i in incorrect: 
    print(f'{i[0]}: {i[1]}\nYour answer: {i[2]}')
	
	
		