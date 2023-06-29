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
    # end def insert
# end class Tree
