class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def inorder_traversal_recursive(node, lst):
    if node is None:
        return lst

    if node.left is not None:
        left = inorder_traversal_recursive(node.left, lst)
    lst.append(node.value)
    if node.right is not None:
        right = inorder_traversal_recursive(node.right, lst)
    
    return lst

     

def inorder_traversal(tree):
    inorder_values = []

    if tree is None:
        return inorder_values
    
    res = inorder_traversal_recursive(tree,inorder_values)
    return res


def find_height_recursive(node, height):
    if node is None:
        return height
    
    
    left = find_height_recursive(node.left, height+1)
    right = find_height_recursive(node.right, height+1)
    return max(left, right)
    



def find_height(tree):
    return find_height_recursive(tree,0)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)


    print("inorder:", inorder_traversal(root))
    print("height", find_height(root))



