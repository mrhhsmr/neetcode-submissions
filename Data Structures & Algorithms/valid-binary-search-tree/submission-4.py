# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))

    def validate(self, node: Optional[TreeNode], low: float, high: float) -> bool:
        # 辅助方法：负责具体的逻辑校验
        
        # 1. 基准情况：碰到空节点，说明这一条路径查完了，没发现问题
        if not node:
            return True
        
        # 2. 核心校验：当前节点的值必须在 (low, high) 这个开区间内
        # 这就解决了你之前“只看父子，不看祖先”的问题
        if not (low < node.val < high):
            return False
        
        # 3. 递归向下：
        # 检查左边时：更新上限为当前节点值（左边所有数都要小于我）
        # 检查右边时：更新下限为当前节点值（右边所有数都要大于我）
        return self.validate(node.left, low, node.val) and self.validate(node.right, node.val, high)
        