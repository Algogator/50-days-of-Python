#import pdb

def fibo(num):
    while num>-1:
        if num == 0:
            #print 0
            return 0
        elif num == 1:
          #  print 1
            return 1
        else:
            return fibo(num-2)+fibo(num-1)



num = int(raw_input())
#pdb.set_trace()


#Calculating each number for the fib. series
for num in range (0,num):
    print fibo(num)