from data_structures.trie import Trie

def test_trie_init():
  trie = Trie()

  assert trie.size == 0
  assert bool(trie) == True

def test_trie_insert():
  trie = Trie()

  trie.insert('hello')
  trie.insert('world')
  assert trie.size == 2

def test_trie_contains():
  trie = Trie()

  trie.insert('hello')

  assert trie.contains('hello') == True
  assert trie.contains('world') == False

  trie.insert('world')
  assert trie.contains('world') == True

def test_trie_find_prefix():
  trie = Trie()

  trie.insert('hello')
  trie.insert('world')
  print(trie.root.children['h'].children['e'].children)

  assert trie.find('he') == True
  assert trie.find('wor') == True

def test_trie_remove():
  trie = Trie()

  trie.insert('hello')
  trie.insert('world')
  assert trie.contains('world') == True

  trie.remove('world')
  assert trie.contains('world') == False