# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lookup = head
        values = []
        while lookup:
            values.append(lookup.val)
            lookup = lookup.next
        
        idx = 1
        while idx < len(values):
            tmp = values[idx-1]
            values[idx-1] = values[idx]
            values[idx] = tmp
            idx += 2

        out = ListNode()
        for i in values[::-1]:
            tmp = out
            tmp.val = i
            out = ListNode()
            out.next = tmp
        return out.next