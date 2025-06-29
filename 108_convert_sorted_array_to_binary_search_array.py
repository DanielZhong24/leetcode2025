#2025-6-9 time: 9:06
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def helper(l,r):
            if l>r:
                return None
            mid = (l+r)//2

            root = TreeNode(nums[mid])

            root.left = helper(l,mid-1)
            root.right = helper(mid+1,r)

            return root
        return helper(0,len(nums)-1)