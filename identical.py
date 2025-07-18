class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def is_identical(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_identical(p.left, q.left) and is_identical(p.right, q.right)
p= TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

p.left = node2
p.right = node3
node2.left = node4
node2.right = node5

q= TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

q.left = node2
q.right = node3
node2.left = node4
node2.right = node5
print(is_identical(p,q))
