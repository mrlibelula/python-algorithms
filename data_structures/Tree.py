from __future__ import annotations

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child: TreeNode) -> TreeNode:
        child.parent = self
        self.children.append(child)
        return self
    
    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level
    
    def print(self) -> None:
        indent = ' ' * self.get_level() * 3
        prefix = indent + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print()
    
def build_product_tree():
    root = TreeNode('Electronics')
    
    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('MacBook'))
    laptop.add_child(TreeNode('Surface'))
    laptop.add_child(TreeNode('Thinkpad'))
    
    cellphone = TreeNode('Cell Phone')
    cellphone.add_child(TreeNode('iPhone'))
    cellphone.add_child(TreeNode('Google Pixel'))
    cellphone.add_child(TreeNode('Vivo'))
    
    tv = TreeNode('TV')
    tv.add_child(TreeNode('Samsung'))
    
    lg = TreeNode('LG')
    lg.add_child(TreeNode('Libe\'s awesome TV'))
    tv.add_child(lg)
    
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    return root

if __name__ == '__main__':
    root = build_product_tree()
    root.print()
    pass