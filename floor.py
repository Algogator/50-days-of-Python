w = float(input())
h = float(input())
c = float(input())

"""
http://stackoverflow.com/questions/4915361/whats-the-difference-between-raw-input-and-input-in-python3-x

The difference is that raw_input() does not exist in Python 3.x, while input() does.

In Python 2, raw_input() returns a string, and input() tries to run the input as a Python expression.
Since getting a string was almost always what you wanted, Python 3 does that with input().
As Sven says, if you ever want the old behaviour, eval(input()) works.
"""

tcost = w*h*c

print "cost : %f" % tcost