# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mini(self, root: Optional[TreeNode]):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
            if not root:
                return None
            if root.val < key:
                #right side
                root.right = self.deleteNode(root.right,key)
            elif root.val > key:
                root.left = self.deleteNode(root.left,key)
            
            else :#key == root.val
                if root.right == None and root.left == None:
                    return None
                if root.right == None:
                    return root.left
                elif root.left == None:
                    return root.right

                else:
                    minim = self.mini(root.right)
                    root.val = minim.val                    
                    root.right = self.deleteNode(root.right, minim.val)

            return root

