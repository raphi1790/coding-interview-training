from collections import deque

class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def invert_binary_tree(root):
    if root is None:
        return None
    
    root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(root.left)
    return root


def bfs_traversal(root):
    sorted_values = []
    queue = deque()

    if root is None:
        return sorted_values

    queue.append(root)

    while queue:
        num_nodes_level = len(queue)
        for _ in range(num_nodes_level):
            current_node = queue.popleft()

            sorted_values.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
    
    return sorted_values

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    new_root = invert_binary_tree(root)
    print("bfs_traversal:", bfs_traversal(new_root))
    print(new_root.left.left)
    