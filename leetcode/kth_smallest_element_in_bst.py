# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/790/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        tracker = 0
        answer = None

        def iot(n: TreeNode, k: int) -> int:
            nonlocal tracker, answer
            if n and n.left:
                iot(n.left, k)
            tracker += 1
            if (tracker is k) and n:
                answer = n.val
            if n and n.right:
                iot(n.right, k)

        iot(root, k)

        return answer

    def kthSmallest_concise(self, root: TreeNode, k: int) -> int:

        def iot(n: TreeNode) -> [int]:
            left = iot(n.left) if n and n.left else []
            mid = [n.val] if n else []
            right = iot(n.right) if n and n.right else []
            return left + mid + right

        output = iot(root)
        return output[k-1] if k > 0 and k-1 < len(output) else None

    def kthSmallest_faster(self, root: TreeNode, k: int) -> int:
        # replace the recursion with a stack

        stack = []

        """
        intuition:
        traversing left-down from a node = getting to (sub)tree min
        traversing right-down from a node = count that node (in array POV)
        example: 4    [4], root = 1, k = 2
                /
               1      [4,1], root = None
                \     [4], root = 1, k = 1, root = 3
                 3    [4,3], root = 2
                /     [4,3,2], root = None
               2      [4,3], root = 2, k = 0
        """
        while True:
            if root:
                # breadcrumbs along path to min:
                stack.append(root)
                # get left-most node = (sub)tree min:
                root = root.left
            elif stack:
                root = stack.pop()
                k -= 1  # count down to 0 = found
                if k == 0:
                    return root.val
                # check for any right nodes:
                root = root.right
            else:
                # handle empty root and empty stack:
                break


n = TreeNode(5)
n.left = TreeNode(1)
n.left.right = TreeNode(3)
n.left.right.left = TreeNode(2)
n.left.right.right = TreeNode(4)
n.right = TreeNode(6)

answer = Solution()
# output = answer.kthSmallest
# output = answer.kthSmallest_concise
output = answer.kthSmallest_faster

print('✅' if output(n, 1) == 1 else '❌')
print('✅' if output(n, 2) == 2 else '❌')
print('✅' if output(n, 3) == 3 else '❌')
print('✅' if output(n, 4) == 4 else '❌')
print('✅' if output(n, 5) == 5 else '❌')
print('✅' if output(n, 6) == 6 else '❌')
print('✅' if output(n, 7) == None else '❌')
print('✅' if output(None, 1) == None else '❌')
print('✅' if output(TreeNode(), 0) == None else '❌')
print('✅' if output(TreeNode(2), 1) == 2 else '❌')
print('✅' if output(TreeNode(2), 2) == None else '❌')
