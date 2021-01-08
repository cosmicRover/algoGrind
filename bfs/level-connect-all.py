from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
  '''
  level order traversal bfs pop(0)
  '''

  q = [root]

  #save previous and current node at a higher level 
  #so that we may always have a hook to connect them to
  prev, curr = None, None

  while q:
    level = len(q)

    for _ in range(level):
      curr = q.pop(0)
      
      #hook prev.next
      if prev:
        prev.next = curr
      
      #always re-write prev with current
      prev = curr

      if curr.left:
        q.append(curr.left)
      if curr.right:
        q.append(curr.right)


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()


main()
