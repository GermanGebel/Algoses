# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if head.next == None:
            return None
        
        slow = ListNode(next=head)
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        slow.next = slow.next.next
        
        return head