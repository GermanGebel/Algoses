import sys
import time

def climbStairsFastFib(n: int) -> int:        
    i = 1
    a, b = 1, 1
    while i < n:
        a, b = b, a + b
        i += 1
    
    return b


def climbStairsSlowRecursive(n):

    stack = []
    ways = []

    def backtrace(steps):
        if steps == n:
            ways.append("".join(stack))
        
        if steps + 1 <= n:
            stack.append('1')
            backtrace(steps + 1)
            stack.pop()
        
        if steps + 2 <= n:
            stack.append('2')
            backtrace(steps + 2)
            stack.pop()
    
    backtrace(0)
    # print(ways)
    return len(ways)

n = int(sys.argv[1])

slow_start = time.time()
slow = climbStairsSlowRecursive(n)
slow_end = time.time()

fast_start = time.time()
fast = climbStairsFastFib(n)
fast_end = time.time()

print(f'Slow method result: {slow}, fast result: {fast}\nSlow time: {slow_end - slow_start}, fast time: {fast_end - fast_start}')
    
        
