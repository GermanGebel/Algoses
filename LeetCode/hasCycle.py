class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycleFloyd(head: ListNode) -> bool:
    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

def hasCycleBrend(head: ListNode) -> bool:
    slow = None
    fast = head
    power = count = 1        

    while fast != None and fast.next != None:
        if slow == fast:
            return True
        
        if power == count:
            slow = fast
            count = 0
            power *= 2
        
        fast = fast.next
        count += 1

    return False

