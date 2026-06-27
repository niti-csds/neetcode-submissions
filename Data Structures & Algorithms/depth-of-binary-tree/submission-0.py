# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        def bfs(root):
            level = 0
            if not root:
                return level

            else :
                queue.append(root)
            while(len(queue)>0):
                for i in range(len(queue)):
                    cur = queue.popleft()
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                
                level+=1

            return level

        return bfs(root)


            


        
        





            


            


            


            

            
                
