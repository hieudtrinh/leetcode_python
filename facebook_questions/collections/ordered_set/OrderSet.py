# found this implementation from leetcode's discussion board
class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class OrderedSet(object):

    def __init__(self):
        self._set = set()

        self.ref = {}
        self.head = None
        self.tail = None

    def add(self, val):
        if val in self._set:
            return False

        self._set.add(val)

        node = Node(val)
        self.ref[val] = node

        if not self.head:
            self.head, self.tail = node, node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        return True

    def remove(self, val):
        if val not in self._set:
            return False

        node = self.ref[val]

        if node == self.head:           # or only 1
            self.head = node.next
            if self.head:
                self.head.prev = None
            if self.tail == node:
                self.tail = node.next
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        del self.ref[val]
        self._set.remove(val)

        return True

    def toArray(self):
        ret = []
        p = self.head
        while p:
            ret.append(p.val)
            p = p.next
        return ret

    def contain(self, val):
        if val in self._set:
            return True
        return False


if __name__ == "__main__":
    os = OrderedSet()
    assert not os.contain(1)
    assert os.add(1)
    assert os.toArray() == [1]
    assert os.contain(1)
    assert os.remove(1)
    assert not os.remove(1)

    assert os.add(2)
    assert os.add(3)
    assert os.add(4)
    assert os.toArray() == [2, 3, 4]
    assert os.contain(2)
    assert os.remove(2)
    assert not os.contain(2)