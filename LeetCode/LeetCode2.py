# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        i = 0
        j = 0
        while l1:
            num1 += l1.val * (10 ** i)
            l1 = l1.next
            i += 1
        while l2:
            num2 += l2.val * (10 ** j)
            l2 = l2.next
            j += 1
        final_sum = str(num1 + num2)
        out = ListNode()
        for i in range(len(final_sum)):
            tmp = out
            tmp.val = int(final_sum[i])
            out = ListNode()
            out.next = tmp
        return out.next
