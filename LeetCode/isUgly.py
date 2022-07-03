

def isUglyMy(n): # O(nlogn)
    ugly = [2, 3, 5]
    last = [n]
    
    while 1:
        
        if last[-1] == 1:
            return True
        if last[-1] == 0:
            return False
        
        flag = False
        for ug in ugly:
            if last[-1] % ug == 0:
                last.append(last[-1] / ug)
                flag = True
                break
        
        if not flag:
            return False
        