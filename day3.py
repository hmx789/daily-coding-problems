# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# NOTE NEED TO REVIEW SOLUTION


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(self, root: Node) -> [int]:
    serialized = []

    def preOrderSerialize(node):
        if node:
            serialized.append(node.val)
        else:
            serialized.append(node)

        if node != None:
            preOrderSerialize(node.left)
            preOrderSerialize(node.right)

    preOrderSerialize(root)
    return serialized


def deserialize(self, data: [int]) -> Node:
    data = data

    def preOrderDeserialize(data):
        val = data.pop(0)
        if val == None:
            return None

        root = Node(val)
        root.left = preOrderDeserialize(data)
        root.right = preOrderDeserialize(data)

        return root
    return preOrderDeserialize(data)
# The following test should pass:


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
