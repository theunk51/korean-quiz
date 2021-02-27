import random
import os
with open('word.txt') as f:
  dictionary = {line.split(' - ')[1].replace('\n',''): line.split(' - ')[0] for line in f}
  f.close()

'''
from itertools import isslice
wordList = isslice(dictionary, 24)
print(wordList)

def check(): 
  for word, answer in userDict.items():
    break 

while bank != []:
  word = bank.pop()
  userDict = {}
  userDict[word] = input(f'\n{word}\n>>> ')
  
  if bank == []:
    print('Congratulations! You completed the list!')
    os.system('cls')



use a data set thaht is ablte to be subtracted and mutated (set, dict) '''

wordcount = 2
wordList, userDict = {}, {}


for x in range(wordcount):
  i = random.choice(list(dictionary.items()))
  wordList[i[0]] = i[1]


word = list(wordList.keys())

while len(word) > 0:
  term = word.pop()
  userDict[term] = input(f'\n{term} \n>>> ')

  if len(word) == 0:
    print('\n\n Done')


incorrect = []
correct = 0
def score(incorrect, correct):
  for key, val in wordList.items():
    for term, answer in userDict.items():
      if term == key and val == answer: 
        correct += 1
      elif term == key and answer != val:
        incorrect.append([key, val, answer])
  
  
  return incorrect
  return correct

score(incorrect, correct)
print(incorrect, correct)


def results(incorrect, correct):
  key, val, answer = incorrect[0][0], incorrect[0][1], incorrect[0][2]
  os.system('clear')

  print(f'Your score is: {correct}/{wordcount}\n\n\n')
  for i in incorrect:
    print(f"{key}: {val}\nyour answer: {answer}\n\n")


results(incorrect, correct)

'''try:
  len(wordList) == len(userDict)
except:
  print("Unexpected error:", sys.exc_info()[0])
  raise
  break'''






  
