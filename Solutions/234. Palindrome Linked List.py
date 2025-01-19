# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # # 683ms Solution
        # prev = None
        # slow = head
        # fast = head
        # while fast and fast.next:
        #     # move fast pointer
        #     fast = fast.next.next
        #
        #     # move slow pointer and reverse
        #     temp = slow.next
        #     slow.next = prev
        #     prev = slow
        #     slow = temp
        #
        # # even number of nodes
        # if not fast:
        #     return self.is_equal(prev, slow)
        #
        # # odd number of nodes
        # return self.is_equal(prev, slow.next)

        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        if temp == temp[::-1]:
            return True
        return False

    # def is_equal(self, node1, node2):
    #     while node1 and node2 and node1.val == node2.val:
    #         node1 = node1.next
    #         node2 = node2.next
    #
    #     return node1 == node2


Obj = Solution()
