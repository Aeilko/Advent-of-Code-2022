class BinaryTreeNode:

    data = None
    left = None
    right = None

    parent = None

    def __init__(self, left=None, right=None, data=None, parent=None):
        self.left = left
        self.right = right
        self.data = data
        self.parent = parent

    def __str__(self):
        if self.data is not None:
            return str(self.data)
        else:
            return "[" + str(self.left) + "," + str(self.right) + "]"


def NextLeafRight(node, depth=0):
    cur_node = node
    going_up = True
    if node.parent is None or type(node.right) == BinaryTreeNode:
        going_up = False
        cur_node = cur_node.right
        if type(cur_node) != BinaryTreeNode:
            return None, None, None
        depth += 1

    while True:
        if going_up:
            prev_node = cur_node
            cur_node = cur_node.parent
            depth -= 1
            if cur_node is None:
                break

            if cur_node.right == prev_node:
                continue
            elif type(cur_node.right) == BinaryTreeNode:
                cur_node = cur_node.right
                depth += 1
                going_up = False
            else:
                return cur_node.right, cur_node, depth  # val, node, depth
        else:
            if type(cur_node.left) == BinaryTreeNode:
                cur_node = cur_node.left
                depth += 1
            else:
                return cur_node.left, cur_node, depth  # val, node, depth

    return None, None, None


def NextLeafLeft(node, depth=0):
    cur_node = node
    going_up = True
    if node.parent is None or type(node.left) == BinaryTreeNode:
        going_up = False
        cur_node = cur_node.left
        if type(cur_node) != BinaryTreeNode:
            return None, None, None
        depth += 1

    while True:
        if going_up:
            prev_node = cur_node
            cur_node = cur_node.parent
            depth -= 1
            if cur_node is None:
                break

            if cur_node.left == prev_node:
                continue
            elif type(cur_node.left) == BinaryTreeNode:
                cur_node = cur_node.left
                depth += 1
                going_up = False
            else:
                return cur_node.left, cur_node, depth  # val, node, depth
        else:
            if type(cur_node.right) == BinaryTreeNode:
                cur_node = cur_node.right
                depth += 1
            else:
                return cur_node.right, cur_node, depth  # val, node, depth

    return None, None, None
