class BSTNode():
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.value = val
    
    def insert(self, val):
        if not self.value:
            self.value = val
            return
        
        if self.value == val:
            return
        
        if val < self.value:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return
        if val > self.value:
            if self.right:
                self.right.insert(val)
                return
            self.right = BSTNode(val)
            return
    
    def delete(self, val):
        if self == None:
            return self
        if val < self.value:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.value:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.value)
        return self

    
    def exists(self, val):
        if self.value == val:
            return True

        if val < self.value:
            if self.left:
                return self.left.exists(val)
            return False
        if val > self.value:
            if self.right:
                return self.right.exists(val)
            return False
        
        return False

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.value is not None:
            vals.append(self.value)
        if self.right is not None:
            self.right.inorder(vals)
        return vals


    
if __name__ == "__main__":
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    bst = BSTNode()
    for num in nums:
        bst.insert(num)
    print(bst.exists(17))
    print(bst.inorder([]))
        
    