# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = list1
        prev_a = dummy
        for _ in range(a):
            prev_a = prev_a.next
        node_a = prev_a.next
        node_b = node_a
        for _ in range(b-a):
            node_b = node_b.next
        
        prev_a.next = list2
        last_node_list2 = list2
        while last_node_list2.next:
            last_node_list2 = last_node_list2.next
        
        last_node_list2.next = node_b.next
        node_b.next = None
        
        return dummy.next
        