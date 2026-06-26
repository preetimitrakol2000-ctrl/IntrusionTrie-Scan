class PacketTrieNode:
    def __init__(self):
        # Maps raw characters to downstream child structures
        self.child_branches = {}
        self.is_terminal_flag = False
