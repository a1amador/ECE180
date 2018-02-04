# Download this corpus of 10,000 common English words and do the following: Compute the average length of the words.
#
# What is the longest word?
# What is the longest word that starts with s
# What is the most common starting letter?
# What is the most common ending letter?

# you can use this bit of code to download the words from the corpus
import urllib2

u = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt'
response = urllib2.urlopen(u)
words = [i.strip() for i in response.readlines()]


# 1) to compute the longest word
wlen=0
for i in words:
    if len(i)>wlen:
        wlen = len(i)
        long_word = i


# 2) What is the longest word that starts with s

wlen=0
for i in words:
    if len(i)>wlen and i[0]=='s':
        wlen = len(i)
        long_word = i

# 3) What is the most common starting letter?
L0 = []
for i in words:
    L0.append(i[0])

count = {}
for s in L0:
  if count.has_key(s):
    count[s] += 1
  else:
    count[s] = 1

for key in count:
  if count[key] > 1:
    print key, count[key]

# 4) What is the most common ending letter?
L0 = []
for i in words:
    L0.append(i[-1])

count = {}
for s in L0:
  if count.has_key(s):
    count[s] += 1
  else:
    count[s] = 1

for key in count:
  if count[key] > 1:
    print key, count[key]


# write a function to compute the longest word
# def get_longest_word(words):




# def get_longest_words_startswith(words, starts):



# def get_most_common_start(words):



# def get_most_common_end(words):

