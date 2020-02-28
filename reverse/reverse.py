class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = Node()

    def display_list(self):
        if self.head.next_node == None:
            print("List is empty")
            return

        p = self.head.next_node
        print("List is :  ")
        while p is not None:
            print(p.value, " ")
            p = p.next_node
        print()

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def create_list(self):
        n = int(input("Enter the number of nodes : "))
        for _ in range(n):
            value = int(input("Enter the element to be inserted : "))
            self.insert_at_end(value)

    def insert_at_end(self, value):
        new = Node(value)

        p = self.head
        while p.next_node is not None:
            p = p.next_node
        p.next_node = new

    # def contains(self, value):
    #     if not self.head:
    #         return False
    #     # get a reference to the node we're currently at; update this as we traverse the list
    #     current = self.head
    #     # check to see if we're at a valid node
    #     while current:
    #         # return True if the current value we're looking at matches our target value
    #         if current.get_value() == value:
    #             return True
    #         # update our current node to the current node's next node
    #         current = current.get_next()
    #     # if we've gotten here, then the target node isn't in our list
    #     return False

    def reverse_list(self):
        prev = None
        p = self.head.next_node
        while p is not None:
            next = p.next_node
            p.next_node = prev
            prev = p
            p = next
        self.head.next_node = prev


lst = LinkedList()

lst.create_list()

lst.reverse_list()

lst.display_list()
