# main.py
import math_utils

print(math_utils.add(10, 5))
print(math_utils.subtract(10, 5))


#import specific function
from math_utils import add
print(add(4, 2))

#import with alias
import math_utils as mu
print(mu.add(3, 1))

#importing specific function from package folder
from mypackage.operations import multiply
print(multiply(3, 4))