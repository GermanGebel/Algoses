from collections import defaultdict


def getN(n):
    return sum([int(i) ** 2 for i in str(n)])


def isHappyDict(n): # extra space O(nlogn)
    d = defaultdict(int)
        
    while 1:
        d[n] += 1 # O(1)

        n = getN(n) # get n: O
        
        if n == 1:
            return True
        
        if d[n] > 0: # O(1)
            break
        
    return False


def isHappySlowFastFloyd(n):
    slow = fast = n

    while 1:
        slow = getN(slow)
        fast = getN(getN(fast))

        if slow == fast:
            break
    
    return slow == 1

