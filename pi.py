from __future__ import division
from decimal import Decimal as D


dots = int(raw_input())
if dots < 6:
    MAX = 6
else:
    MAX = dots
pi = 0
for k in range(MAX):
    pi += D(16**-k) * (D(4/(8*k+1)) - D(2/(8*k+4)) - D(1/(8*k+5)) - D(1/(8*k+6)))
#getcontext.prec default
print pi
print '%.*f' % (dots, pi)

