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

    def in_order_traversal(self, node):
        if node.left is not None:
            self.in_order_traversal(node.left)
        print(f'{node.data} ')
        if node.right is not None:
            self.in_order_traversal(node.right)

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

    def get_height(self, node):
        if node.left and node.right:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))
        elif node.left:
            return 1 + self.get_height(node.left)
        elif node.right:
            return 1 + self.get_height(node.right)
        else:
            return 1

    def get_nodes_at_k_distance(self, node, k):
        if k == 0:
            print(node.data)
        if node.left:
            self.get_nodes_at_k_distance(node.left, k - 1)
        if node.right:
            self.get_nodes_at_k_distance(node.right, k - 1)

    def level_order_traversal(self, node):
        q = [node]
        while len(q) != 0:
            node = q.pop(0)
            print(node.data)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

    def get_size(self, node):
        if node is None:
            return 0
        return 1 + self.get_size(node.left) + self.get_size(node.right)

    def get_max_value(self, node):
        if node is None:
            return 0
        return max(node.data, self.get_max_value(node.left), self.get_max_value(node.right))

    def left_view(self, node):
        if node is not None:
            print(node.data)
        if node.left is not None:
            self.left_view(node.left)

    def right_view(self, node):
        if node is not None:
            print(node.data)
        if node.right is not None:
            self.right_view(node.right)

    def is_child_sum_true(self, node):
        if node.left.data is None:
            node.left.data = 0
        if node.right.data is None:
            node.right.data = 0

        if node.left.data + node.right.data != node.data:
            return False
        if node.left is not None:
            self.is_child_sum_true(node.left)
        if node.right is not None:
            self.is_child_sum_true(node.right)

tree = Tree()
root_node = tree.create_node(10)

l = [5, 5, 6]

for data in l:
    tree.insert(root_node, data)

tree.is_child_sum_true(root_node)
