# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_node = []
        for l in lists:
            while(l):
                all_node.append(l)
                l = l.next
        all_node.sort(key=lambda x : x.val)
        for idx in range(len(all_node) - 1):
            all_node[idx].next = all_node[idx + 1]
        if len(all_node) == 0:
            return None
        all_node[-1].next = None
        return all_node[0]