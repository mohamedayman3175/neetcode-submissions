# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        lis=[]
        for i in range(len(lists)):       
            while(lists[i]):
                lis.append(lists[i].val)
                lists[i]=lists[i].next
        lis.sort()
        for value in lis:
            current.next=ListNode(value)
            current=current.next
        return dummy.next