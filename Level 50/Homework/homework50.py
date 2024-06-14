import sys

try:
    raise TypeError
except:
    print(repr(sys.exc_info()[1]))
    try:
        raise ValueError
    except:
        print(repr(sys.exc_info()[1]))
    print(repr(sys.exc_info()[1])) 

print(repr(sys.exc_info()))

