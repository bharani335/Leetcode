# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # # 11ms Solution
        # if head == None:
        #     return head
        # if head.next == None:
        #     return head
        # oddhead = head
        # evenhead = head.next
        # even = evenhead
        # while evenhead and evenhead.next:
        #     oddhead.next = oddhead.next.next
        #     evenhead.next = evenhead.next.next
        #     oddhead = oddhead.next
        #     evenhead = evenhead.next
        # oddhead.next = even
        # return head

        original = head
        odd_head = head
        if head and head.next:
            even_head = head.next
            even_head_start = head.next
        else:
            return head
        while even_head and even_head.next:
            odd_head.next = even_head.next
            odd_head = odd_head.next
            even_head.next = odd_head.next
            odd_head.next = even_head_start
            even_head = even_head.next

        return original


Obj = Solution()

