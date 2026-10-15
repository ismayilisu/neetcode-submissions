# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def recurse(head,k):

            temp=head
            last=temp
            for _ in range(k):
                if not temp:
                    return head
                temp=temp.next
            start=head
            prev=None
            while start!=temp:
                nexx=start.next
                start.next=prev
                prev=start
                start=nexx
            head.next=recurse(start,k)
            return prev
        return recurse(head,k)
        