from heapq import heappop, heappush
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Python method of comparator!!!
# Note the default would be __lt__ and return self.val < other.val 
# This will be the minQueue
class Wrapper:
    def __init__(self, node: ListNode) -> None:
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_node = ListNode()
        cur = dummy_node
        
        q = []
        
        # push to heap
        for i in range(0, len(lists)): 
            i_node = lists[i]
            if (i_node):
                heappush(q, Wrapper(i_node))
                
        while (len(q) > 0):
            minNode = heappop(q).node
            
            cur.next = minNode
            cur = cur.next
            
            if (minNode.next):
                heappush(q, Wrapper(minNode.next))
        
            
        return dummy_node.next