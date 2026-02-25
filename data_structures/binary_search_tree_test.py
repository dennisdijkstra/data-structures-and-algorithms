from data_structures.binary_search_tree import BinarySearchTree


def test_bst_init():
    bst = BinarySearchTree()

    assert bst.size == 0
    assert bst.root == None


def test_bst_insert():
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(20)
    bst.insert(15)

    assert bst.size == 3


def test_bst_find_non_existing():
    bst = BinarySearchTree()
    values = [5, 33, 9, 16]

    bst.insert(values[0])
    bst.insert(values[1])
    bst.insert(values[2])
    found_node = bst.find(values[3])

    assert found_node == None


def test_bst_find():
    bst = BinarySearchTree()
    values = [5, 33, 9, 16]

    bst.insert(values[0])
    bst.insert(values[1])
    bst.insert(values[2])
    bst.insert(values[3])
    found_node = bst.find(values[3])

    assert found_node.value == values[3]


def test_bst_find_min():
    bst = BinarySearchTree()
    values = [5, 33, 9, 16]

    bst.insert(values[0])
    bst.insert(values[1])
    bst.insert(values[2])
    bst.insert(values[3])
    min_node = bst.find_min()

    assert bst.size == 4
    assert min_node.value == values[0]


def test_bst_find_max():
    bst = BinarySearchTree()
    values = [45, 120, 87, 12]

    bst.insert(values[0])
    bst.insert(values[1])
    bst.insert(values[2])
    bst.insert(values[3])
    max_node = bst.find_max()

    assert bst.size == 4
    assert max_node.value == values[1]


def test_bst_in_order_traverse():
    bst = BinarySearchTree()
    bst.insert(2)
    bst.insert(9)
    bst.insert(5)
    bst.insert(20)
    bst.insert(8)
    bst.insert(7)
    bst.insert(8)
    bst.insert(3)
    bst.insert(100)

    list = []
    bst.in_order(list, True)
    assert list == [2, 3, 5, 7, 8, 8, 9, 20, 100]


def test_bst_pre_order_traverse():
    bst = BinarySearchTree()
    bst.insert(2)
    bst.insert(9)
    bst.insert(5)
    bst.insert(20)
    bst.insert(8)
    bst.insert(7)
    bst.insert(8)
    bst.insert(3)
    bst.insert(100)

    list = []
    bst.pre_order(list, True)
    assert list == [2, 9, 5, 3, 8, 7, 8, 20, 100]


def test_bst_post_order_traverse():
    bst = BinarySearchTree()
    bst.insert(2)
    bst.insert(9)
    bst.insert(5)
    bst.insert(20)
    bst.insert(8)
    bst.insert(7)
    bst.insert(8)
    bst.insert(3)
    bst.insert(100)

    list = []
    bst.post_order(list, True)
    assert list == [3, 7, 8, 8, 5, 100, 20, 9, 2]


def test_bst_contains():
    bst = BinarySearchTree()
    node = bst.insert(2)
    bst.insert(9)
    bst.insert(5)
    bst.insert(20)

    assert bst.contains(node) == True
