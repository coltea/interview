class TreeNode:
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left  # 左子树
        self.right = right  # 右子树

    def print_node(self):
        print(self.root, self.left, self.right)


node_b = TreeNode(
    "B", TreeNode("D"),  # TreeNode("E")
)
node_c = TreeNode(
    "C", TreeNode("F"), TreeNode("G")
)
node1 = TreeNode("A", node_b, node_c)


def level_order(root):
    res_lt, queue = [], [root]
    if not root.root:
        return res_lt
    while queue:
        for i in range(len(queue)):
            print(len(queue), queue)
            node = queue.pop(0)
            if node.root:
                res_lt.append(node.root)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res_lt


def levelOrder(root):
    res = []
    if root is None:
        return res
    queue = [root]
    while queue:
        for i in range(len(queue)):
            print(queue, len(queue))
            node = queue.pop(0)
            res.append(node.root)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res


print(level_order(node1))
