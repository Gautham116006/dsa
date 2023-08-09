class Tree:
    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data
        # end def __init__
    # end class Node

    def create_node(self, data):
        node = self.Node(data)
        return node
    # end def create_node

    def insert(self, node, data):
        if node is None:
            return self.create_node(data)
        # end if
        if node.data > data:
            node.left = self.insert(node.left, data)
        # end if
        if node.data < data:
            node.right = self.insert(node.right, data)
        # end if

        else:
            if data > node.data:
                node.right = self.insert(node.right, data)
            else:
                node.left = self.insert(node.left, data)
        return node
    # end def insert

    def inorder_traversal(self, node):
        if node.left is not None:
            self.inorder_traversal(node.left)
        print(f'{node.data} ')
        if node.right is not None:
            self.inorder_traversal(node.right)
    # end def inorder_traversal

    def post_order_traversal(self, node):
        if node.right is not None:
            self.post_order_traversal(node.right)
        print(f'{node.data} ')
        if node.left is not None:
            self.post_order_traversal(node.left)
    # end def post_order_traversal

    def pre_order_traversal(self, node):
        if node.data is not None:
            print(f'{node.data}')
        if node.left is not None:
            self.pre_order_traversal(node.left)
        if node.right is not None:
            self.pre_order_traversal(node.right)
    # end def pre_order_traversal


tree = Tree()
root_node = tree.create_node(10)

l = [4, 5, 6, 11, 12, 13]

for data in l:
    tree.insert(root_node, data)

tree.post_order_traversal(root_node)

