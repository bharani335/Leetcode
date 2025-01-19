# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head

        left = head
        right = self.return_mid(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge_left_right(left, right)

    def return_mid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge_left_right(self, left, right):
        tail = mainhead = ListNode()

        while left and right:
            if left.val > right.val:
                tail.next = right
                right = right.next
            else:
                tail.next = left
                left = left.next
            tail = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right
        return mainhead.next


Obj = Solution()
array = [4, 2, 1, 3]
head = ListNode(array[-1])
for x in range(len(array) - 2, -1, -1):
    head = ListNode(array[x], head)

head1 = head

while head:
    print("Before=>", head.val)
    head = head.next

head = Obj.sortList(head1)

while head:
    print("After=>", head.val)
    head = head.next
