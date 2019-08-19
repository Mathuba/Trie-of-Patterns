import pytest
from Trie import trie

def test_build_trie_case_one():
    result_dict = trie.build_trie(['ATA'])
    assert result_dict == {
        0: {'A' : 1},
        1: {'T' : 2},
        2: {'A' : 3}
    }