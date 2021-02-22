class TreeNode:
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left  # 左子树
        self.right = right  # 右子树

    def print_node(self):
        print(self.root, self.left, self.right)


node = TreeNode(
    "0",
    TreeNode("1",
             TreeNode("3"),
             TreeNode("4", TreeNode("7"))),
    TreeNode("2",
             TreeNode("5", TreeNode("8"), TreeNode("9")),
             TreeNode("6", TreeNode("10")))
)


def preorder_traversal(n: TreeNode):
    res = []
    q = [n]
    while n:
        res.append(n)
        q.append(n)
        if n.left:
            n = n.left
        elif n.right:
            n = n.right
            # else:

    return res


if __name__ == '__main__':
    preorder_traversal(node)
