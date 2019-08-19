#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    i_index = 0
    root_index = i_index
    tree[root_index] = {}
    for pattern in patterns:
        current_node = tree[root_index]
        for current_symbol in pattern:
            if current_node.get(current_symbol):
                current_node = tree[current_node[current_symbol]]
            else:
                i_index += 1
                current_node[current_symbol] = i_index
                tree[i_index] = {}
                current_node = tree[i_index]
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
