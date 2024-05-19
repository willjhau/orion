class SyntaxTreeNode:
    def __init__(self, symbol, matched_string):
        self.symbol = symbol
        self.matched_string = matched_string
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.symbol) + ": " + repr(self.matched_string) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret
    
    def countLeaves(self):
        if not self.children:
            return 1
        return sum(child.countLeaves() for child in self.children)