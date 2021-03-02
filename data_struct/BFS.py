from data_struct.TreeNode import TreeNode

head_node = TreeNode(
    "0",
    TreeNode("1",
             TreeNode("3"),
             TreeNode("4", TreeNode("7"))),
    TreeNode("2",
             TreeNode("5", TreeNode("8"), TreeNode("9")),
             TreeNode("6", TreeNode("10"))))


def bfs(n: TreeNode):
    queue = [n]
    res = []
    while queue:
        node = queue.pop(0)
        res.append(node.root)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return res


print(bfs(head_node))
# print(level_order(node))
