# ProgrammingExercises0201
# Recall the data from last time
#
# data=[5,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,2]
# Write three columns to a comma-separated file:
#
# data_value, data_value**2, (data_value+data_value**2)/3.


def write_columns(data, fname):
    '''
    Given data as a list, write three columns to fname.

    :param: data
    :type : list
    :param: fname
    :type: str
    '''
    f = open(fname, 'w')  # write mode
    for i in data:
        x = str(i) + ',' + str(i**2) + ',' + str((i+i**2)/3)
        f.write(x + '\n')

    f.close()



data=[5,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,2]
x=0
for i in data:
    x = x+i+i**2+(i+i**2)/3
print x

fname = 'myfile.csv'
write_columns(data, fname)


### BEGIN  TESTS
import numpy as np
from nose.tools import assert_almost_equal

data = [5, 4, 6, 1, 9, 0, 3, 9, 2, 7, 10, 8, 4, 7, 1, 2, 7, 6, 5, 2, 8, 2, 0, 1, 1, 1, 2, 10, 6, 2]
fname = 'test_data.csv'
write_columns(data, fname)
assert_almost_equal(np.loadtxt(fname, delimiter=',').sum(), 1328, 2)

### END  TESTS