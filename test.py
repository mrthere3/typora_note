class Node:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head, self.tail = Node(0), Node(0)
        self.head.next, self.tail.pre = self.tail, self.head
        self.count = 0

    def getnode(self, index: int) -> Node:

        node = self.head
        for _ in range(index + 1):
            node = node.next
        return node

    def get(self, index: int) -> int:
        if 0 <= index < self.count:
            node = self.getnode(index)
            return node.val
        else:
            return -1

    def _update(self, prev: Node, next: Node, val: int) -> None:
        adddnode = Node(val)
        self.count += 1
        prev.next, adddnode.next = adddnode, next
        adddnode.pre, next.pre = prev, adddnode

    def addAtHead(self, val: int) -> None:
        self._update(self.head, self.head.next, val)

    def addAtTail(self, val: int) -> None:
        self._update(self.tail.pre, self.tail, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        elif index > self.count:
            return
        node = self.getnode(index)
        self._update(node.pre, node, val)

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.count:
            node = self.getnode(index)
            # 计数-1
            print(node.pre, node.next, index)
            self.count -= 1
            node.pre.next, node.next.pre = node.next, node.pre

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)