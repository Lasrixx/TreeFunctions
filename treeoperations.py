# Definition for a binary tree node.
from email.mime import application
from unicodedata import name
from unittest.util import sorted_list_difference


class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

# ----------- Tree creation functions ------------
def arrayToBinaryTree(arr, i, arrLength):
    # This function inserts nodes in a level order fashion
    root = None
    if i < arrLength:
        if arr[i] != "None":
            root = TreeNode(arr[i])
            # Insert left child
            root.left = arrayToBinaryTree(arr, 2 * i + 1, arrLength)
            # Insert right child
            root.right = arrayToBinaryTree(arr, 2 * i + 2, arrLength)
    return root
              

def sortedArrayToBST(nums):
    # Root of a tree will always be middle element
    # This is true of all subtrees as well, using a divide and conquer approach
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    return root

def arrayToBinarySearchTree(arr):
    # Wrapper function to sort array in preparation of converting array to BST
    arr.sort()
    return sortedArrayToBST(arr)

# ----------- Tree traversal functions -------------
def breadthFirstTraversal(root):
    # Perform breadth-first traversal
    if not root:
        return []
    queue = [(0,root)]
    while queue:
        level, curr = queue.pop(0)
        # Print element at front of queue
        print(curr.val, end = ' ')
        # If there are children of the current node, push these to the back of the queue
        if curr.left: queue.append((level + 1, curr.left))
        if curr.right: queue.append((level + 1, curr.right))

def preOrderTraversalIterative(root):
    # Perform depth-first traversal
    if not root:
        return
    # Explicitly defined stack in place of recursive stack
    stack = [root]
    while stack:
        curr = stack.pop()
        # Print top element
        print(curr.val, end = ' ')
        # If children exist, push them to the top of the stack
        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)

def preOrderTraversalRecursive(curr):
    # Perform depth-first traversal
    if curr:
        # Print current element
        print(curr.val, end = ' ')
        # Keep going through children
        preOrderTraversalRecursive(curr.left)
        preOrderTraversalRecursive(curr.right)

def inOrderTraversalIterative(root):
    # Perform depth-first traversal
    if not root: 
        return
    stack = []
    curr = root
    while stack or curr:
        if curr:
            # Need to go as far down the tree as we can before hitting None
            stack.append(curr)
            curr = curr.left
        else:
            # If we hit a None, we can print the top element of the stack (this was out last visited element)
            curr = stack.pop()
            print(curr.val, end = ' ')
            # And move into the right subtree if we can 
            curr = curr.right

def inOrderTraversalRecursive(curr):
    # Perform depth-first traversal
    if curr:
        # Scan left subtree
        inOrderTraversalRecursive(curr.left)
        # Then the root
        print(curr.val, end = ' ')
        # Then the right subtree
        inOrderTraversalRecursive(curr.right)

def postOrderTraversalIterative(root):
    # Perform depth-first traversal
    if not root:
        return

    # Stack1 is our traversal stack
    stack1 = [root]
    # Stack2 is what will produce our output
    stack2 = []

    while stack1:
        curr = stack1.pop()

        # Append the current node to stack2
        stack2.append(curr)

        # Keep traversing the children if possible
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)

    # Print the contents of stack2 
    while stack2:
        curr = stack2.pop()
        print(curr.val, end = ' ')

def postOrderTraversalRecursive(curr):
    # Perform depth-first traversal
    if curr:
        # Traverse left subtree
        postOrderTraversalRecursive(curr.left)
        # Then right subtree
        postOrderTraversalRecursive(curr.right)
        # Then the root
        print(curr.val, end = ' ')

# ------------- Other functions -------------
def maxDepth(root):
    if root == None:
        return 0
    return max(maxDepth(root.left),maxDepth(root.right)) + 1

def invertTree(root):
    if root == None:
        return
    stack = [root]
    while stack:
        curr = stack.pop()
        # Flip current children
        temp = curr.left
        curr.left = curr.right
        curr.right = temp
        # Continue traversal
        if curr.right != None:
            stack.append(curr.right)
        if curr.left != None:
            stack.append(curr.left)
    return root

def lowestCommonAncestor(root, p, q):
    # Imagine the tree is a mountain,
    # From the root, we can see everything below us
    # As we start to descend, we lose sight of the other side of the mountain
    while root != None:
        # If both p and q are in the right subtree, 
        # We can go further into the right subtree to find the LCA
        if root.val < p and root.val < q:
            root = root.right
        # If both p and q are in the left subtree, continue into the left subtree
        elif root.val > p and root.val > q:
            root = root.left
        # Otherwise, p and q are in different subtrees so we are as low as we can get
        # Without losing 'sight' of either p or q
        else:
            return root.val
    return None

if __name__ == "__main__":
    arr = []
    print("Welcome to Tree Manager")
    while True:
        mode = input("Enter mode: \n\
            C - Create tree \n\
            T - Traverse tree \n\
            O - Other operations \n\
            Q - Exit application")
        
        if mode == 'C':
            arr = []
            tree = None
            creationType = input("Do you want to make a Binary Search Tree (Enter B) or Binary Tree (Enter N)?")
            length = int(input("Enter length of tree: "))
            i = 0
            while i < length:
                val = input("Enter node value (if making a binary tree None values are allowed): ")
                if creationType == 'B' and val == None:
                    print("invalid input - no None values allowed in Binary Search Tree")
                else:
                    arr.append(val)
                    i += 1
            if creationType == 'B':
                tree = arrayToBinarySearchTree(arr)
            else:
                tree = arrayToBinaryTree(arr, 0, len(arr))
        elif mode == 'T':
            traversalType = input("Enter traversal type: \n\
                    R - Breadth First Traversal \n\
                    T - Iterative PreOrder Traversal \n\
                    Y - Recursive PreOrder Traversal \n\
                    U - Iterative InOrder Traversal \n\
                    I - Recursive InOrder Traversal \n\
                    O - Iterative PostOrder Traversal \n\
                    P - Recursive PostOrder Traversal")
            if traversalType == 'R':
                breadthFirstTraversal(tree)
            elif traversalType == 'T':
                preOrderTraversalIterative(tree)
            elif traversalType == 'Y':
                preOrderTraversalRecursive(tree)
            elif traversalType == 'U':
                inOrderTraversalIterative(tree)
            elif traversalType == 'I':
                inOrderTraversalRecursive(tree)
            elif traversalType == 'O':
                postOrderTraversalIterative(tree)
            else:
                postOrderTraversalRecursive(tree)
        elif mode == 'O':
            type = input("Enter function: \n\
                    B - Find the maximum depth of the tree \n\
                    N - Flip the tree \n\
                    M - Find the lowest common ancestor")
            if type == 'B':
                print(maxDepth(tree))
            elif type == 'N':
                invertTree(tree)
            else:
                validP = False
                p = ""
                validQ = False
                q = ""
                while not validP:
                    p = input("Enter node: ")
                    if p in arr:
                        validP = True
                while not validQ:
                    q = input("Enter another node: ")
                    if q in arr:
                        validQ = True
                print(lowestCommonAncestor(tree,p,q))
        else:
            quit()
