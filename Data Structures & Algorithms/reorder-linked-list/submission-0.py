# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return
        nodes = []
        current = head
        while current :
            nodes.append(current)
            current=current.next
        ordered_nodes=[]
        n=len(nodes)
        left=0
        right = n-1
        while left<=right:
            ordered_nodes.append(nodes[left])
            left+=1
            if left<=right:
                ordered_nodes.append(nodes[right])
                right-=1
        for i in range(n - 1):
            ordered_nodes[i].next=ordered_nodes[i+1]
        ordered_nodes[-1].next=None    

            
                
