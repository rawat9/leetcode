# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
            
        current_sum, max_sum, n = 0, 0, len(lst)

        i, j = 0, n-1
        while i <= j:
            current_sum = lst[i] + lst[j]
            i += 1
            j -= 1
            
            max_sum = max(current_sum, max_sum)
            
        return max_sum
