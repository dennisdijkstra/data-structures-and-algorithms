from data_structures.queue_ import Queue


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def getRoot(self):
        return self.root

    def insert(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            self.size += 1
            return

        queue = [self.root]

        while queue:
            current_node = queue.pop(0)

            if current_node.left is None:
                current_node.left = node
                self.size += 1
                break
            else:
                queue.append(current_node.left)

            if current_node.right is None:
                current_node.right = node
                self.size += 1
                break
            else:
                queue.append(current_node.right)

    def in_order(self, list, isRoot, node=None):
        if isRoot:
            node = self.root

        if node is None:
            return

        self.in_order(list, False, node.left)
        list.append(node.value)
        self.in_order(list, False, node.right)

    def pre_order(self, list, isRoot, node=None):
        if isRoot:
            node = self.root

        if node is None:
            return

        list.append(node.value)
        self.pre_order(list, False, node.left)
        self.pre_order(list, False, node.right)

    def post_order(self, list, isRoot, node=None):
        if isRoot:
            node = self.root

        if node is None:
            return

        self.post_order(list, False, node.left)
        self.post_order(list, False, node.right)
        list.append(node.value)

    def bfs(self):
        queue = Queue()
        queue.enqueue(self.root)

        while queue.size > 0:
            print(queue.peek().value)
            node = queue.dequeue()

            if node.left is not None:
                queue.enqueue(node.left)

            if node.right is not None:
                queue.enqueue(node.right)
