from data_struct.TreeNode import TreeNode

head_node = TreeNode(
    "0",
    TreeNode(
        "1",
        TreeNode("3"),
        TreeNode("4", TreeNode("7"))
    ),
    TreeNode(
        "2",
        TreeNode("5", TreeNode("8"), TreeNode("9")),
        TreeNode("6", TreeNode("10"))
    )
)


def dfs_pre(node: TreeNode):
    res = []

    def run(n: TreeNode):
        if n is None:
            return
        res.append(n.root)
        print(n.root)
        run(n.left)
        run(n.right)

    run(node)
    return res


def dfs_inorder(node: TreeNode):
    res = []

    def run(n: TreeNode):
        if not n:
            return
        run(n.left)
        res.append(n.root)
        run(n.right)

    run(node)
    return res


def dfs_postorder(node: TreeNode):
    res = []

    def run(n: TreeNode):
        if not n:
            return
        run(n.left)
        run(n.right)
        res.append(n.root)

    run(node)
    return res


# print(dfs_pre(head_node))

print(dfs_inorder(head_node))
# [3、1、7、4、0、8、5、9、2、10、6]

print(dfs_postorder(head_node))
# [3、7、4、1、8、9、5、10、6、2、0]
