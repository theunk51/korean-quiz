import random
from text import wordList
'''with open('word.txt', 'r') as f:
  wordList = {line.split(' - ')[1].replace('\n',''): line.split(' - ')[0] for line in f}
  f.close()'''


'''with open("text.py", 'x') as k:
  for key, val in wordList.items():
    k.write(f'  "{key}" : "{val}",\n')'''

b = [key for key in wordList.keys()]
bank = random.shuffle(b)

def check():
  #for dict(i).values()  wordList.values():

while bank != []:
  fraction = len(i) - len(set(b) - set(i)) 

  try:
    word = bank.pop()
    i = set(word, input(word, '\n>>> '))
  except:
    print('Congratulations! You completed the list!)
    print(f'Your scores is: {fraction} / {len(b)} {(fraction/len(b))*100}%')
    print('Your incorrect answers: {}')

'''use a data set thaht is ablte to be subtracted and mutated (set, dict) '''