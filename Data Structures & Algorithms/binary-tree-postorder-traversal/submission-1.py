# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative solution
        parents = {}
        visited = set()
        curr = root

        traverse = []

        while curr is not None:
            if curr.left is not None and curr.left not in visited:
                parents[curr.left] = curr
                curr = curr.left
            elif curr.right is not None and curr.right not in visited:
                parents[curr.right] = curr
                curr = curr.right
            # If no unvisited children, process the node and backtrack
            else:
                traverse.append(curr.val)
                visited.add(curr)
                curr = parents.get(curr)

        return traverse

            
        