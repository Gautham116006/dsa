"""
a -> b -> c -> d
"""


class LinkedList:
    """
    class for a linked list
    """

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
        # end def __init__
    # end class Node

    def __init__(self, data=None):
        self.head = None
        if data is not None:
            self.head = self.Node(data)
    # end def __init__

    def insert(self, data, idx=None):
        """
        Insert node at any given index, by default at the end if idx is None
        """
        if self.head is None:
            self.head = self.Node(data)
            return
        # end if

        curr_node = self.head

        if idx is None:
            while curr_node.next is not None:
                curr_node = curr_node.next
            # end while
            curr_node.next = self.Node(data)

        elif idx == 0:
            old_head = self.head
            self.head = self.Node(data)
            self.head.next = old_head

        else:
            while idx > 1:
                curr_node = curr_node.next
                idx -= 1
            # end while

            new_node = self.Node(data)
            new_node.next = curr_node.next
            curr_node.next = new_node
        # end if
    # end def insert

    def print_linked_list(self):
        """
        Give a console output of the linked list in a fun format
        """
        curr_node = self.head

        while curr_node.next is not None:
            print(f"{curr_node.data} -> ", end='')
            curr_node = curr_node.next
        # end while

        print(curr_node.data)
    # end def print_linked_list

    def deletion(self, idx):
        """
        delete a node at a given idx
        """
        curr_node = self.head

        if idx == 0:
            self.head = self.head.next
        # end if

        while idx > 1:
            curr_node = curr_node.next
            idx -= 1
        # end while

        curr_node.next = curr_node.next.next
    # end def deletion

    def search(self, element):
        """
        search for a node with a given value
        """
        curr_node = self.head

        while curr_node.next is not None:
            if curr_node.data == element:
                return "Found"
            # end if
            curr_node = curr_node.next
        # end while

        return "Not Found"
    # end def search

    def update(self, data, idx):
        """
        update value of a node at a given position
        """
        curr_node = self.head

        while idx > 0:
            curr_node = curr_node.next
            idx -= 1
        # end while

        curr_node.data = data
    # end def update

    def traversal(self):
        """
        traverse from one node to other
        """
        raise NotImplementedError
    # end def traversal

    def get_ele_at_index(self, idx):
        """
        return element at a given idx
        """
        curr_node = self.head

        while idx > 0:
            curr_node = curr_node.next
            idx -= 1
        # end while
        return curr_node.data
    # end def get_ele_at_index

    def sort(self):
        """
        sort all the elements in the list
        """
        length = 1
        curr_node = self.head

        while curr_node.next is not None:
            length += 1
            curr_node = curr_node.next
        # end while

        for i in range(length - 1, 0, -1):
            for j in range(i):
                ele_j = self.get_ele_at_index(j)
                ele_j_plus_1 = self.get_ele_at_index(j + 1)
                if ele_j > ele_j_plus_1:
                    self.update(ele_j, j + 1)
                    self.update(ele_j_plus_1, j)
                # end if
            # end for
        # end for
    # end def sort

    def merge(self):
        """
        merge two linked list
        """
        raise NotImplementedError
    # end def merge
# end class LinkedList



