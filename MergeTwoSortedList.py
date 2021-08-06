# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        merged=[]
        l1node=l1
        while l1node is not None:
            merged.append(l1node.val)
            l1node=l1node.next
        l2node=l2
        while l2node is not None:
            merged.append(l2node.val)
            l2node=l2node.next
        merged.sort()
        nodes = []
        for i in range(0, len(merged)):
            node = ListNode()
            node.val = merged[i]
            node.next = None
            nodes.append(node)
        if len(nodes) > 1:
            for i in range(0, len(nodes) - 1):
                nodes[i].next = nodes[i+1]
            nodes[len(nodes)-1].next = None
            return nodes[0]
        elif len(nodes) == 1:
            head = ListNode()
            head.val = nodes[0].val
            head.next = None
            return head
        
        return None