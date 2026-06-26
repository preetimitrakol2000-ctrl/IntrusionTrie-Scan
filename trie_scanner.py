from trie_node import PacketTrieNode

class NetworkSignatureTrie:
    def __init__(self):
        self.root = PacketTrieNode()

    def black_list_exploit(self, signature_string):
        current = self.root
        for char in signature_string:
            if char not in current.child_branches:
                current.child_branches[char] = PacketTrieNode()
            current = current.child_branches[char]
        current.is_terminal_flag = True

    def scan_string_segment(self, window_string):
        """Returns True if the prefix string matches a blacklisted pattern exactly."""
        current = self.root
        for char in window_string:
            if char not in current.child_branches:
                return False
            current = current.child_branches[char]
            if current.is_terminal_flag:
                return True
        return False
