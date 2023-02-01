# noinspection PyMethodMayBeStatic
class Tree:
    class Node:
        def __init__(self, data):
            self.left = None
            self.data = data
            self.right = None

    def create_node(self, data):
        return self.Node(data)

    def insert(self, node, data):
        if node is None:
            return self.create_node(data)
        else:
            if data > node.data:
                node.right = self.insert(node.right, data)
            else:
                node.left = self.insert(node.left, data)
        return node

    def inorder_traversal(self, node):
        if node.left is not None:
            self.inorder_traversal(node.left)
        print(f'{node.data} ')
        if node.right is not None:
            self.inorder_traversal(node.right)

    def post_order_traversal(self, node):
        if node.right is not None:
            self.post_order_traversal(node.right)
        print(f'{node.data} ')
        if node.left is not None:
            self.post_order_traversal(node.left)

    def pre_order_traversal(self, node):
        if node.data is not None:
            print(f'{node.data}')
        if node.left is not None:
            self.pre_order_traversal(node.left)
        if node.right is not None:
            self.pre_order_traversal(node.right)


tree = Tree()
root_node = tree.create_node(10)

l = [4, 5, 6, 11, 12, 13]

for data in l:
    tree.insert(root_node, data)

tree.post_order_traversal(root_node)








