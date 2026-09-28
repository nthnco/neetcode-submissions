"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {}
        curr = sec = head
        while curr:
            map[curr] = Node(x = curr.val)
            curr = curr.next
        while sec:
            copy = map[sec]
            copy.next = map.get(sec.next)
            copy.random = map.get(sec.random)
            sec = sec.next
        return map.get(head)
