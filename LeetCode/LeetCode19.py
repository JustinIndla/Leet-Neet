# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        copy = head
        size = 0
        while(copy):
            size += 1
            copy = copy.next
        new_idx = size - n + 1

        tmp = head
        prev = None
        if(not tmp):
            return head
        if new_idx == 1:
            head = tmp.next
            return head
        for i in range(1, new_idx):
            prev = tmp
            tmp = tmp.next
            if(not tmp):
                return head
        if tmp:
            prev.next = tmp.next
        return head
        