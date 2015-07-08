# example of program that calculates the total number of times each word has been tweeted.
# 7.7.2015

import sys
import collections
import operator

#open input output file
infile=open(sys.argv[1], "r")
outfile=open(sys.argv[2], "w+")


# use a collection because it does counts
words = collections.Counter()

# get each line and add unique words to the collection along with numbewr of times it occurred
for line in infile: words.update(line.split())

#sort the collection
sorted_words = sorted(words.items())

# get the maximum length of each column for formatting of output file
word_length, count_length = [max(len(str(item)) for item in line) for line in zip(*sorted_words)]


# longer way of getting the length of the columns
lengths = []
for line in zip(*sorted_words):
	max_len = 0
	for item in line:
		if len(str(item)) > max_len: max_len = len(str(item))
	lengths.append(max_len)

word_len, count_len = lengths	
#print word_length, count_length
#print word_len, count_len

#write the output to file
for word,count in sorted_words:
	outfile.write(("{} {}\n").format(word.ljust(word_length), str(count).rjust(count_length) ))

