class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    node = llist_2.head
    while node :
        llist_1.append(node)
        node = node.next
    return llist_1

def intersection(llist_1, llist_2):
    values_in_llist_1 = set()
    
    node = llist_1.head
    while node :
        values_in_llist_1.add(node.value)
        node = node.next
    
    intersection_list1_list2 = LinkedList()
    
    node = llist_2.head
    while node :
        if (node.value in values_in_llist_1) :
            intersection_list1_list2.append(node)
        node = node.next
        
    # Your Solution Here
    return intersection_list1_list2


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# [3,2,4,35,6,65,6,4,3,21,6,32,4,9,6,1,11,21,1]
print (intersection(linked_list_1,linked_list_2))
# [6,32,4,9,6,1,11,21,1]

# Test case 2

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# [3,2,4,35,6,65,6,4,3,23,1,7,8,9,11,21,1]
print (intersection(linked_list_1,linked_list_2))
# []

# Test case 3

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1,2,3]
element_2 = [3,2,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# [1,2,3,3,2,1]
print (intersection(linked_list_1,linked_list_2))
# [3,2,1]

# Test case 4

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = [4,5,6]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# [4,5,6]
print (intersection(linked_list_1,linked_list_2))
# []

# Test case 5

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# []
print (intersection(linked_list_1,linked_list_2))
# []