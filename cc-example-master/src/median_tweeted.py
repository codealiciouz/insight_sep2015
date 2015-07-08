# example of program that calculates the median number of unique words per tweet.
# 7.7.2015 jsa

# import needed libraries
import sys #for arg handling
import re  #regex
import os  #for file handling
import collections 

# used median function to avoid possible issues with numpy,statistics,etc
def median(values):
    values = sorted(values)
    if len(values) < 1:
            return None
    if len(values) %2 == 1:
            return values[((len(values)+1)/2)-1]
    if len(values) %2 == 0:
            return float(sum(values[(len(values)/2)-1:(len(values)/2)+1]))/2.0

# open input output files
infile=open(sys.argv[1],"r+")
outfile=open(sys.argv[2],"w+")
#print infile, outfile

wordcount=[]
median_value=[]

#print "Median ... "


# get each line and add words to the collection
for i,line in enumerate(infile): 

	# use a collection because it does counts
	words = collections.Counter()
	words.update(line.split())
	num_words  = len(words)
	wordcount.append(num_words)
	mwc = median(wordcount)
	median_value.append(mwc)

	# write to file
	outfile.write("%0.1f\n" %mwc)  

	#print num_words
	#print mwc



# close file
infile.close();


# close file
outfile.close();




