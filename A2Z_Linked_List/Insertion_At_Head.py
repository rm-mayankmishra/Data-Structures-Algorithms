class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def insertAtHead(self, head, X):
        newNode = Node(X)
        newNode.next = head
        head = newNode
        return head
