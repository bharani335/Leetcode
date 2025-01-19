# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 3ms Solution
        # dummy = ListNode(0, head)
        # left = dummy
        # right = head
        #
        # while n > 0:
        #     right = right.next
        #     n -= 1
        #
        # while right:
        #
        #     right = right.next
        #     left = left.next
        #
        # left.next = left.next.next
        #
        # return dummy.next

        original_head = head
        temp_head = head
        index_list = [1]
        while temp_head:
            index_list.append(index_list[-1] + 1)
            if temp_head.next:
                temp_head = temp_head.next
            else:
                break
        temp_head = original_head
        if len(index_list[:-n]) == 1:
            return original_head.next
        for x in range(2, len(index_list[:-n])):
            temp_head = temp_head.next

        temp_head.next = temp_head.next.next
        return original_head


Obj = Solution()
array = [4, 2, 1, 3]
n = 2
head = ListNode(array[-1])
for x in range(len(array) - 2, -1, -1):
    head = ListNode(array[x], head)

head1 = head

while head:
    print("Before=>", head.val)
    head = head.next

head = Obj.removeNthFromEnd(head1, n)

while head:
    print("After=>", head.val)
    head = head.next
