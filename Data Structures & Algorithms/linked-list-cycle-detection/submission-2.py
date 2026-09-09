# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev_val=[]
        current = head
        i = 0        
        while current:
            if current.val in prev_val[:i] + prev_val[i + 1:]:
                if current.next == None:
                    return False
                return True
            i+=1
            prev_val.append(current.val)
            current = current.next
        return False



