from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  '''
  level order bfs pop(0)

  return the next item that comes after matching with key
  '''
  q = [root]
  returnNext = False

  while q:
    size = len(q)
    for _ in range(size):
      node = q.pop(0)

      if returnNext: 
        return node

      if node == key:
        returnNext = True

      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = find_successor(root, 12)
  if result:
    print(result.val)
  result = find_successor(root, 9)
  if result:
    print(result.val)


main()
