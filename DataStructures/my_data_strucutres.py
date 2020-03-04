# -*- coding: utf-8 -*-
"""
This module contains various data structures implemented directly in Python.
For most of the cases, there are faster implementations easy available.

The module was implemented only for educational and practise purposes as well
as a memorization method.
"""


class Array:
    """
    Simple array emulation.
    """

    def __init__(self):
        self.length = 0
        self.data = {}

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return self.length

    def __str__(self):
        result = ''
        for i in range(self.length-1):
            result = result+str(i)+':'+str(self.data[i])+', '
        if self.length > 0:
            result = result+str(self.length-1)+':'+str(self.data[self.length-1])
        return result

    def append(self, item):
        self.data[self.length] = item
        self.length += 1

    def remove(self, index): #delete
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1

    def reverse(self):
        result = self.data.copy()
        for i in range(self.length//2):
            pair_index_to_swap = self.length-1-i
            result[i], result[pair_index_to_swap] = result[pair_index_to_swap], result[i]
        return result


class SingleLinkedNode:
    """
    This class contains single node for a linked list.
    """
    def __init__(self, value, pointer=None):
        self.value = value
        self.next_pointer = pointer


class LinkedList:
    """
    Simple implementation of a linked list.
    
    To be done:
        * add get and set methods to node class and use them in the class 
    """
    def __init__(self, first_value):
        self.head = SingleLinkedNode(first_value)
        self.tail = self.head

    def __str__(self):
        next_node = self.head
        result = ''
        while next_node:
            result += str(next_node.value)+', '
            next_node = next_node.next_pointer
        return result[:-2]

    def append(self, last_value):
        new_node = SingleLinkedNode(last_value)
        self.tail.next_pointer, self.tail = new_node, new_node

    def prepend(self, first_value):
        self.head = SingleLinkedNode(first_value, self.head)

    def get_pointer(self, index):
        current_node = self.head
        for _ in range(0, index):
            current_node = current_node.next_pointer
            if current_node is None:
                raise IndexError
        return current_node

    def insert(self, inserted_value, index):
        if index == 0:
            self.prepend(inserted_value)
        else:
            current_node = self.get_pointer(index-1)
            if current_node == self.tail:
                self.append(inserted_value)
            else:
                current_node.next_pointer = SingleLinkedNode(inserted_value, current_node.next_pointer)

    def popleft(self):
        result, self.head = self.head.value, self.head.next_pointer
        return result

    def delete(self, index):
        if index == 0:
            self.popleft()
        else:
            current_node = self.get_pointer(index-1)
            if current_node.next_pointer == self.tail:
                current_node.next_pointer = None
                self.tail = current_node
            else:
                current_node.next_pointer = current_node.next_pointer.next_pointer

    def reverse(self):
        prev_pointer = self.head.next_pointer
        current_pointer = self.head
        self.tail = self.head
        while prev_pointer is not None:
            temp = prev_pointer.next_pointer
            prev_pointer.next_pointer = current_pointer
            current_pointer = prev_pointer
            prev_pointer = temp
        self.tail.next_pointer = None
        self.head = current_pointer



