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

    
if __name__ == "__main__":
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    bst = BSTNode()
    for num in nums:
        bst.insert(num)
    print(bst.exists(17))
        
    