from __future__ import division
from decimal import getcontext
from decimal import Decimal as D

def factorial (num):

        if num > 0:
                return (num * factorial(num-1)) 
        return 1

r = int(raw_input())
if r<6:
	till = 6
else:
	till = r
n = 0
answer = 0

while n<till:
	# Brothers' Formulae
	answer += D(((2*n)+2)/(factorial((2*n)+1)))
	n+=1

#>>> print "Today's stock price: %.2f" % 50.4625 2
#50.46
# * - argument specifies width or precision

print '%.*f' % (r,answer)

