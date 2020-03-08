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


class QueueNode:
    """
    This class contains single node for a queue.
    """
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer


class Queue:
    """
    Simple implementation of queue data structure.
    """
    def __init__(self):
        self.length = 0
        self.first = None
        self.last = None

    def isEmpty(self):
        return self.length == 0

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.first.value

    def enqueue(self, value):
        if self.isEmpty():
            self.first = QueueNode(value)
            self.last = self.last
        elif self.length == 1:
            self.last = QueueNode(value)
            self.first.pointer = self.last
        else:
            self.last.pointer = QueueNode(value, self.last)
            self.last = self.last.pointer
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        elif self.length == 1:
            result = self.first.value
            self.first = None
            self.last = None
        else:
            result = self.first.value
            self.first = self.first.pointer
        self.length -= 1
        return result


class StackNode:
    """
    This class contains single node for a stack.
    """
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer


class Stack:
    """
    Simple implementation of stack data structure.
    """
    def __init__(self):
        self.length = 0
        self.top = None
        self.bottom = None

    def is_empty(self):
        return self.length == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.value

    def push(self, value):
        if self.is_empty():
            self.top = StackNode(value)
            self.bottom = self.top
        else:
            self.top = StackNode(value, self.top)
        self.length += 1

    def pop(self):
        if self.is_empty():
            return None
        elif self.length == 1:
            result = self.top.value
            self.top = None
            self.bottom = None
        else:
            result = self.top.value
            self.top = self.top.pointer
        self.length -= 1
        return result


class TreeNode:
    """
    This class contains single node for a tree.
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    """
    Under work:
        Extend logic while inserting values
    Simple implementation of Tree data structure.
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            current_tree_node = self.root
            while True:
                if value < current_tree_node.value:
                    if current_tree_node.left is not None:
                        next_tree_node = current_tree_node.left
                    else:
                        current_tree_node.left = TreeNode(value)
                        break
                else:
                    if current_tree_node.right is not None:
                        next_tree_node = current_tree_node.right
                    else:
                        current_tree_node.right = TreeNode(value)
                        break
                current_tree_node = next_tree_node

    def lookup(self, value):
        current_tree_node = self.root
        while True:
            if current_tree_node is None:
                return False
            elif current_tree_node.value == value:
                return True
            elif value < current_tree_node.value:
                current_tree_node = current_tree_node.left
            else:
                current_tree_node = current_tree_node.right
