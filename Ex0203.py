# Using the same corpus of 10,000 common English words as before, create a new file that consists of
# each consecutive non-overlapping sequence of five lines merged into one line. Here are the first 10 lines:

# the of and to a
# in for is on that
# by this with i you
# it not or be are
# from at as your all
# have new more an was
# we will home can us
# about if page my has
# search free but our one
# other do no information time

# the of and to a
# in for is on that
# by this with i you
# it not or be are
# from at as your all
# have new more an was
# we will home can us
# about if page my has
# search free but our one
# other do no information time

# If the last group has less than five at the end, just write out the last group.

# you can use this bit of code to download the words from the corpus
import urllib2

u = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt'
response = urllib2.urlopen(u)
words = [i.strip() for i in response.readlines()]

fname = 'output_by_5.txt'
f = open(fname, 'w')  # write mode
words_5=[]
w5 = []
cc=0
for i in words:
    cc = cc+1
    if cc%5==0:
        f.write(i + '\n')
    else:
        f.write(i + ' ')

f.close()




fname = 'output_by_5.txt'
def write_chunks_of_five(words,fname):
    '''
    :param: words
    :type: list
    :param: fname
    :type: str
    '''
# YOUR CODE HERE
