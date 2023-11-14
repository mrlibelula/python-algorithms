from __future__ import annotations

class BinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data) -> None:
        if data == self.data: return
        if data < self.data:
            # add data to left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data to right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
                
    def in_order_traversal(self) -> list:
        # [left subtree + root node + right subtree]
        elements = []
        
        # left subtree
        if self.left:
            elements += self.left.in_order_traversal()
            
        # root node
        elements.append(self.data)
        
        # right subtree
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def pre_order_traversal(self) -> list:
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    
    def post_order_traversal(self) -> list:
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def delete(self, value) -> BinarySearchTreeNode|None:    # O(log n)
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None: return None
            if self.left is None: return self.right
            if self.right is None: return self.left
            
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)
            
        return self
    
    def calculate_sum(self):
        sum_nums = self.data
        if self.left:
            sum_nums += self.left.calculate_sum()
        if self.right:
            sum_nums += self.right.calculate_sum()
        return sum_nums
    
    def search(self, value):
        if self.data == value: return True
        if value < self.data:
            return self.left.search(value) if self.left else False
        if value > self.data:
            return self.right.search(value) if self.right else False
    
def build_tree(elements):
    print('Building tree with these elements: ', elements)
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 1, 18]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())
    
    print('Deletion:')
    numbers_tree.delete(23)
    print(numbers_tree.in_order_traversal())