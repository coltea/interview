class TreeNode:
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left  # 左子树
        self.right = right  # 右子树
    def print_node(self):
        print(self.root, self.left, self.right)


def level_order(root):
    queue = [root]
    res = []
    while queue:
        queue_len = len(queue)
        for i in range(queue_len):
            node = queue.pop(0)
            print(node.root)
            res.append(node.root)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res


node_b = TreeNode(
    "B", TreeNode("D"),  # TreeNode("E")
)
node_c = TreeNode(
    "C", TreeNode("F"), TreeNode("G")
)
node1 = TreeNode("A", node_b, node_c)




def level_order(root):
    res = []
    queue = [root]
    while queue:
        print(len(queue))
        for i in range(len(queue)):
            node = queue.pop(0)
            res.append(node.root)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return  res
print(level_order(node1))

