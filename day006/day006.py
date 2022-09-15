# defining and calling python functions
from itertools import count


print('hello') # built-in functions
print(len('hello'))

def test_func():
    print('hello')
    print('bye')

test_func() # calling the function

# indentation
'''
def function():
....do something
....do something
.... ...

'''

# while loops
'''
while something_is_true:
    do this
'''
count = 0
while count < 10:
    print(count)
    count += 1

