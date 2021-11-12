# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
        prev = None
        
        while current:
            if current.val == val:

				# if val is at the end or middle
                if prev: 
                    prev.next = current.next

				# if head is to be removed
                else: 
                    head = current.next
                current = current.next

			# if there no value to remove	
            else:
                prev = current
                current = current.next
                
        return head
        