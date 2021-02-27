import random

with open('word.txt') as f:
  dictionary = {line[1].replace('\n', '') : line[0] for line.split(' - ') in f}
	f.close()


def check(): pass

x = random.shuffle(dictionary.keys)
