class Node:
    
    def __init__(self, key, data, next = None, prev = None):
        self.key = key
        self.data = data
        self.next = next
        self.prev = prev
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def move_to_front(self, node):
        node.prev.next = node.next
        node.prev = node
        node.next = self.head
        self.head = node
        return None
    
    def append_to_front(self, node):
        node.next = self.head
        self.head.prev = node
        self.head = node
        return None
    
    def drop_tail(self):
        self.tail = self.tail.prev
        self.tail.next = None
        return None


class Cache:
    
    def __init__(self, MAX_SIZE):
        self.MAX_SIZE = MAX_SIZE
        self.size = 0
        self.lookup = {}
        self.linked_list = LinkedList()
        
    def get(self, key):
        """ 
        retrieve an entry and set it as the most recent item
        """
        node = self.lookup[key]
        if node is None:
            return none
        self.linked_list.move_to_front(node)
        return node.data
    
    def set(self, key, data):
        """
        insert or update an item
        """
        node = self.lookup[key]
        if not node is None:
            node.data = data
            self.linked_list.move_to_front(node)
        else:
            node = Node(key, data)
            self.lookup[key] = node
            if self.size == self.MAX_SIZE:
                self.linked_list.drop_tail()
                self.lookup.pop(key, None)
            else:
                self.size += 1
            self.linked_list.append_to_front(node)
        return None