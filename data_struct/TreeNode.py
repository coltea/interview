class TreeNode:
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left  # 左子树
        self.right = right  # 右子树

    def print_node(self):
        print(self.root, self.left, self.right)


def level_order(root):
    res = []
    queue = [root]
    while queue:
        for i in range(len(queue)):
            node = queue.pop(0)
            res.append(node.root)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res


node = TreeNode(
    "0",
    TreeNode("1",
             TreeNode("3"),
             TreeNode("4", TreeNode("7"))),
    TreeNode("2",
             TreeNode("5", TreeNode("8"), TreeNode("9")),
             TreeNode("6", TreeNode("10")))

)print(level_order(node))
