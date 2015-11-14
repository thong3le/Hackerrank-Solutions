#!/bin/python

    
def insertionSort(ar):   
    if len(ar) == 1:
        print ar
        return
    
    e = ar[-1]
    for i in range(len(ar) - 2, -1, -1):
        if ar[i] > e:
            arr = ar[:(i+1)] + ar[i:(len(ar) - 1)]
            print ' '.join(arr)
            if i == 0:
                printar([e] + ar[:(len(ar) - 1)])
        elif ar[i] == e:
            arr = ar[:(i+1)] + ar[i:(len(ar) - 1)]
            printar(arr)
            return
        else:
            arr = ar[:(i+1)] + [e] + ar[(i+1):(len(ar) - 1)]
            printar(arr)
            return
        
    return 

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)


#solution2

n = int(raw_input())
test = raw_input()
a = test.split()
val = a[n-1]
for i in range(n-2,-2,-1):
    test=test.split()
    if i == -1:
        test[i+1] = val
        break
    elif int(test[i])>int(val):
        test[i+1]=test[i]
    
    else:
        test[i+1] = val
        break
    test = ' '.join(test)
    print test  
test = ' '.join(test)
print test

