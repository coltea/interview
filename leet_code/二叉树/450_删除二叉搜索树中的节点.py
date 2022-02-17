from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        pass


if __name__ == '__main__':
    s = Solution()
    r = s.deleteNode([5, 3, 6, 2, 4, None, 7], key=3)
    print(f"res:{r}")
