class TreeNode:
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left  # 左子树
        self.right = right  # 右子树
    def print_node(self):
        print(self.root, self.left, self.right)



def preTraverse(root):
    if root is None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)


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


if __name__ == '__main__':
    node_b = TreeNode(
        "B", TreeNode("D"),  # TreeNode("E")
    )
    node_c = TreeNode(
        "C", TreeNode("F"), TreeNode("G")
    )
    node1 = TreeNode("A", node_b, node_c)
    print(node1)
    # preTraverse(node1)
    print(levelOrder(node1))

    # print([node1].pop(0))
    # print([node1].pop(0))