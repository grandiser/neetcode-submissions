# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_list = 0
        dummy = head
        tail = head

        while tail:
            len_list += 1
            tail = tail.next
        
        target = len_list - n

        # 1 2 3 4
        # len = 4
        # target = 4 - 2 = 2

        if len_list == n:
            return dummy.next

        for i in range(target):
            if i == target - 1:
                head.next = head.next.next
            else:
                head = head.next
        
        return dummy
            