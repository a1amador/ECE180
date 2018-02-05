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


def get_longest_word(words):
    '''
    Given a list of words (each element in words is of type str), compute the longest word
    Args:
    :param: words
    :type : list
    Returns:
    The longest word in list of words (type: str)
    '''
    wlen = 0
    long_word = []
    for i in words:
        if len(i) > wlen:
            wlen = len(i)
            long_word = i
    return long_word


def get_longest_words_startswith(words,starts):
    '''
    Given a list of words, compute the longest word
    that begins with the letter defined by parameter `starts`
    :param: words - each element in words is of type str
    :type : list
    :param: starts - must be a single letter
    :type: str
    Returns:
    The longest word in list of words that begins with the letter defined by parameter `starts` (type: str)
    '''
    assert isinstance(starts,str) and len(starts) == 1
    wlen = 0
    long_word = []
    for i in words:
        if len(i) > wlen and i.startswith(starts):
            wlen = len(i)
            long_word = i
    return long_word


def get_most_common_start(words):
    '''
    Given a list of words, compute the most common starting letter
    :param: words - each element in words is of type str
    :type : list
    Returns:
    The most common starting letter (type: str)
    '''
    most_common = []
    L0 = []
    for i in words:
        L0.append(i[0])

    cc_dict = {}
    for w0 in L0:
        if cc_dict.has_key(w0):
            cc_dict[w0] = cc_dict[w0] + 1
        else:
            cc_dict[w0] = 1

    max_val = max(cc_dict.values())
    cc = 0
    for v in cc_dict.itervalues():
        if v == max_val:
            most_common = cc_dict.keys()[cc]
        cc = cc + 1
    return most_common



def get_most_common_end(words):
    '''
    Given a list of words, compute the most common ending letter
    :param: words - each element in words is of type str
    :type : list
    Returns:
    The most common ending letter (type: str)
    '''
    most_common = []
    L0 = []
    for i in words:
        L0.append(i[-1])

    cc_dict = {}
    for w0 in L0:
        if cc_dict.has_key(w0):
            cc_dict[w0] = cc_dict[w0] + 1
        else:
            cc_dict[w0] = 1

    max_val = max(cc_dict.values())
    cc = 0
    for v in cc_dict.itervalues():
        if v == max_val:
            most_common = cc_dict.keys()[cc]
        cc = cc + 1
    return most_common

### BEGIN  TESTS
assert get_longest_words_startswith(words,'s')=='sublimedirectory'
### END  TESTS

### BEGIN  TESTS
assert get_most_common_start(words)=='c'
### END  TESTS

### BEGIN  TESTS
assert get_most_common_end(words)=='s'
### END  TESTS
