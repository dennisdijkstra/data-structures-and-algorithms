class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node()
        self.size = 0

    def insert(self, word):
        node = self.root

        for char in word:
            if not char in node.children:
                node.children[char] = Node()

            node = node.children[char]

        node.is_end_of_word = True
        self.size += 1

    def contains(self, word):
        node = self.root

        for char in word:
            if not char in node.children:
                return False

            node = node.children[char]

        return node.is_end_of_word

    def find(self, prefix):
        node = self.root

        for char in prefix:
            if not char in node.children:
                return False

            node = node.children[char]

        return True

    def remove(self, word):
        self.delete(self.root, word, 0)

    def delete(self, node, word, index):
        if index == len(word):
            if not node.is_end_of_word:
                return False

            del node.is_end_of_word
            self.size -= 1
            return True

        char = word[index]
        if not char in node.children:
            return False

        can_remove = self.delete(node.children[char], word, index + 1)
        if can_remove:
            del node.children[char]

        return True
