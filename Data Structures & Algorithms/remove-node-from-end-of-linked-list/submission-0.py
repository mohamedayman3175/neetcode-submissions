# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        current_final=dummy
        current=head
        lis=[]
        while current:
            lis.append(current)
            current=current.next
        lis.pop(-n)
        if not lis:
            return None


        for i in range(len(lis) - 1):
            lis[i].next = lis[i + 1]


        lis[-1].next = None

        return lis[0]


