#2025-3-11 time: 20:55
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        #starting node with nothing
        rNode = ListNode()
        #current holder of the node
        current = rNode
        #in case when the sum of the two values go above 
        carry  = 0

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            
            if l2:
                val2 = l2.val
            else:
                val2 = 0

            total = val1+val2 + carry
            carry = total//10
            current.next = ListNode(total%10)

            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next
        return rNode.next
