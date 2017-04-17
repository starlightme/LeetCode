# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pointer_1 =  l1
        pointer_2 =  l2
        node_num  =  0
        sub_num   =  0
        v1 =  0
        v2 =  0
        l  = [] 
        while (pointer_1 is not  None or pointer_2 is not  None or  sub_num is not 0):
            if pointer_1 is not None:
                v1 = pointer_1.val
                pointer_1 = pointer_1.next
            else:
                v1 = 0
            if pointer_2 is not None:
                v2 = pointer_2.val
                pointer_2 = pointer_2.next
            else:
                v2 = 0
            node_num = ( v1 + v2 +  sub_num ) % 10
            sub_num  = ( v1 + v2 +  sub_num ) / 10
            l.append(node_num)
        return l
        