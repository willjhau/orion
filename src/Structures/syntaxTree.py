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
    
    def tidyTree(self):
        if not self.children:
            return
        
        if self.symbol.name == "Identifier":
            self.children = []
            return

        if self.symbol.name == "Type":
            self.children = []
            return
        
        if self.symbol.name == "IntegerLiteral":
            self.children = []
            return
        
        if self.symbol.name == "StringLiteral":
            self.children = []
            return
        
        if self.symbol.name == "CharacterLiteral":
            self.children = []
            return
        
        if self.symbol.name == "FloatLiteral":
            self.children = []
            return
        
        if self.symbol.name == "BooleanLiteral":
            self.children = []
            return
        
        if "Operator" in self.symbol.name:
            self.children = []
            return

        newChildren = []
        for child in self.children:
            # print(child.symbol.name)
            if child.symbol.name in ":; =":
                continue
            if child.symbol.name == "MaybeSpace":
                continue

            child.tidyTree()
            newChildren.append(child)
        self.children = newChildren
        return self