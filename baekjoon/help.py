
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
  #    1
  #  3   2
  # 5
  #
  #    2
  #  1    3
  #   4     7

class Solution:
    # def addTrees(self, t1, t2):
    #     if t1 is not None and t2 is not None:
    #         t1.val = t1.val + t2.val
    #         self.addTrees(t1.left, t2.left)
    #         self.addTrees(t1.right, t2.right)
    #     elif t1 is None and t2 is not None:
    #         t1 = t2
    #         self.addTrees(t1.left, t2.left)
    #         self.addTrees(t1.right, t2.right)


    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # Code Here
        t1Copy = t1

        if t1Copy is None:
            return t2
        if t2 is None:
            return t1Copy

        t1Copy.val += t2.val
        t1Copy.left = self.mergeTrees(t1Copy.left, t2.left)
        t1Copy.right = self.mergeTrees(t1Copy.right, t2.right)

        return t1Copy

test_tree_1_root = TreeNode(1)
test_tree_1_root.left = TreeNode(3)
test_tree_1_root.right = TreeNode(2)
test_tree_1_root.left.left = TreeNode(5)

test_tree_2_root =TreeNode(2)
test_tree_2_root.left =TreeNode(1)
test_tree_2_root.right =TreeNode(3)
test_tree_2_root.left.right =TreeNode(4)
test_tree_2_root.right.right =TreeNode(7)

tester = Solution()

print(tester.mergeTrees(test_tree_1_root,test_tree_2_root).val)
print(tester.mergeTrees(test_tree_1_root,test_tree_2_root).left.val)
print(tester.mergeTrees(test_tree_1_root,test_tree_2_root).right.val)
print(tester.mergeTrees(test_tree_1_root,test_tree_2_root).left.left.val)
print(tester.mergeTrees(test_tree_1_root,test_tree_2_root).left.right.val)
print(tester.mergeTrees(test_tree_1_root,test_tree_2_root).right.left==None)
print(tester.mergeTrees(test_tree_1_root,test_tree_2_root).right.right.val)