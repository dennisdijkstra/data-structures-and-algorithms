from trie import Trie

def test_trie_init():
  trie = Trie()
  
  assert trie.size == 0
  assert bool(trie) == True