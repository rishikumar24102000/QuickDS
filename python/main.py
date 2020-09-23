"""
@Author: rishi
"""

from python.implementations.binarysearchtree import BinarySearchTree as bst
from python.implementations.inputformatter import InputFormatter
# Import required modules
from python.implementations.linkedlist import LinkedList
from python.implementations.list import List


# Main functions for linked list class


# Create linked list from array
def create_linked_list(array):
    """
    :param array: list of integers
    :return: head node of linked list
    """
    return LinkedList().create_linked_list(array)


# Create random linked list
def create_random_linked_list(length=10):
    """
    :param length: length of the linked list and range of the items in linked list
    :return: head of linked list
    """
    return LinkedList().create_random_linked_list(length)


# Print linked list
def pretty_print(head):
    """
    :param head: head node of the linked list to be printed
    """
    LinkedList().pretty_print(head)


# Main functions for list class

# Creates random list
def create_random_list(length=10):
    """
    :param length: length of the list and range of the items in list
    :return: random list
    """
    return List().create_random_list(length)


# Creates 2d random list
def create_random_2d_list(length=10):
    """
    :param length: length of the list and range of the items in list
    :return: random 2d list
    """
    return List().create_random_2d_list(length)


# Main functions for Input Formatter class


# Formats 1d char array
def format_1d_char_list(inp):
    """
    :param inp: string with 1d char array
    :return: 1d list
    """
    return InputFormatter().format_1d_char_list(inp)


# Formats 1d int array
def format_1d_int_list(inp):
    """
    :param inp: string with 1d int array
    :return: 1d list
    """
    return InputFormatter().format_1d_int_list(inp)


# Formats 2d int array
def format_2d_int_list(inp, row_length, col_length):
    """
    :param inp: string with 2d int array
    :param row_length: length of the 2d array rows
    :param col_length: length of the 2d array columns
    :return: 2d list
    """
    return InputFormatter().format_2d_int_list(inp, row_length, col_length)


# Formats 2d char array
def format_2d_char_list(inp, row_length, col_length):
    """
    :param inp: string with 2d int array
    :param row_length: length of the 2d array rows
    :param col_length: length of the 2d array columns
    :return:
    """
    return InputFormatter().format_2d_char_list(inp, row_length, col_length)


# Formats linked list
def format_linked_list(inp):
    """
    :param inp: string with int array
    :return: head node of linked list
    """
    return InputFormatter().format_linked_list(inp)


# Formats BST
def format_bst(inp):
    """
    :param inp: input string
    :return: root node of the tree
    """
    return InputFormatter().format_bst(inp)


# Main functions for Binary Search Tree class


# Creates random list
def create_random_binary_search_tree(length=10):
    """
    :param length: length of the list and range of the items in list
    :return: random list
    """
    return bst().create_random_binary_search_tree(length)


# Creates bst from sorted list
def convert_sorted_list_to_bst(array):
    """
    :param array: sorted array
    :return: root node of the bst created
    """
    return bst().convert_sorted_list_to_bst(array, 0, len(array) - 1)


# Creates BST from level order traversal
def convert_level_order_traversal_to_bst(array):
    """
    :param array: level order traversal of array
    :return: root node of the tree
    """
    return convert_sorted_list_to_bst(sorted(array))


# Converts bst to encoded string
def serialize(root):
    """
    :param root: root node of the tree
    :return: encoded string
    """
    return bst.serialize(root)


# Converts encoded string to BST
def deserialize(inp):
    """
    :param inp: encoded string
    :return: root node of the BST
    """
    return bst.deserialize(inp)


# Prints BST in viewable format
def pretty_print_bst(root):
    """
    :param root: root node of the BST
    """
    bst().pretty_print("", root, False)


# Print inorder of the BST
def print_bst(root):
    """
    :param root: root node of the tree
    """
    bst().inorder(root)