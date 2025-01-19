# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # # 3ms Solution
        # n = 1
        # node = head
        # while node.next:
        #   n += 1
        #   node = node.next
        # print(n)
        # m = (n + 1)/ 2 if n % 2 == 1 else n / 2 + 1
        # print(m)
        # node = head
        # for _ in range(m - 1):
        #   node = node.next
        # return node

        if not head and not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.next if fast else slow


Obj = Solution()
array = [4, 2, 1, 3]
array = [1, 2, 3, 4, 5]
head = ListNode(array[-1])
for x in range(len(array) - 2, -1, -1):
    head = ListNode(array[x], head)

head1 = head

while head:
    print("Before=>", head.val)
    head = head.next

head = Obj.middleNode(head1)

while head:
    print("After=>", head.val)
    head = head.next
