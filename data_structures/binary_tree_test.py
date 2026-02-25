from data_structures.binary_tree import BinaryTree


def test_binary_tree_init():
    binary_tree = BinaryTree()

    assert binary_tree.size == 0
    assert binary_tree.root == None


def test_binary_tree_insert():
    binary_tree = BinaryTree()

    binary_tree.insert(1)
    binary_tree.insert(20)
    binary_tree.insert(15)

    assert binary_tree.size == 3
