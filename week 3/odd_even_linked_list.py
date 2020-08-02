# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# Constraints:

# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...
# The length of the linked list is between [0, 10^4].

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        evenBegin = head.next
        oddPtr = head
        evenPtr = head.next
        
        while True:
            if oddPtr.next is not None:
                oddPtr.next = oddPtr.next.next
            else:
                oddPtr.next = evenBegin
                break
            if evenPtr.next is not None:
                evenPtr.next = evenPtr.next.next
            else:
                oddPtr.next = evenBegin
                break
            oddPtr = oddPtr.next
            evenPtr = evenPtr.next
        return head