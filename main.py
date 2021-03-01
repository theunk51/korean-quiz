import random, os

with open("word.txt") as f:
  dictionary = {line.replace('\n', '').split(' - ')[1]: line.replace('\n','').split(' - ')[0] for line in f}
  f.close()


wordcount = 2
wordList, userDict = {}, {}

for x in range(wordcount):
  i = random.choice(list(dictionary.items()))
  wordList[i[0]] = i[1]

word = list(wordList.keys())

while len(word) > 0:
  term = word.pop()
  userDict[term] = input(f'\n{term}\n >>> ')
  
  if len(word) == 0:
    print('\n\nDone!')




def score(incorrect, correct):
  for key, val in wordList.items():
    for term, answer in userDict.items():
      if key ==term and val == answer:
        correct+= 1
      elif key == term and answer != val:
        incorrect.append([key, val, answer])

  return incorrect, correct
	
res = score([],0)
incorrect, correct = res[0], res[1]

def results(incorrect, correct):
  os.system('clear')
  print(f'Your score is: {correct}/{wordcount}\n\n\n')
  for i in incorrect: 
    print(f'{i[0]}: {i[1]}\nYour answer: {i[2]}\n')

results(incorrect, correct)

