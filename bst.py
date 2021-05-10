from data_generator import randomSubset
class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent=None
    
class binary_search_tree:
    def __init__(self):
        self.root=None
    
    def insert(self, value):
        if self.root==None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value<cur_node.value:
            if cur_node.left==None:
                cur_node.left=Node(value)
                cur_node.left.parent=cur_node
            else:
                self._insert(value, cur_node.left)
        elif value>cur_node.value:
            if cur_node.right==None:
                cur_node.right=Node(value)
                cur_node.right.parent=cur_node
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value already in tree!")
    
    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)
    
    def _print_tree(self, cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left)
            print(str(cur_node.value))
            self._print_tree(cur_node.right)
    
    def height(self):
        if self.root!=None:
            return self._height(self.root, 0)
        else:
            return 0
        
    def _height(self, cur_node, cur_height):
        if cur_node==None: return cur_height
        left_height=self._height(cur_node.left, cur_height+1)
        right_height=self._height(cur_node.right, cur_height+1)
        return max(left_height, right_height)

    def find(self,value):
        if self.root!=None:
            return self._find(value, self.root)
        else:
            return None
    
    def _find(self, value, cur_node):
        if value==cur_node.value:
            return cur_node
        elif value<cur_node.value and cur_node.left!=None:
            return self._find(value, cur_node.left)
        elif value>cur_node.value and cur_node.right!=None:
            return self._find(value, cur_node.right)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        if node==None or self.find(node.value)==None:
            print("Node to be deleted not found in the tree!")
            return None 

        def min_value_node(n):
            current=n
            while current.left!=None:
                current=current.left
            return current

        def num_children(n):
            num_children=0
            if n.left!=None : num_children+=1
            if n.right!=None: num_children+=1
            return num_children

        node_parent=node.parent
        node_children=num_children(node)

        if node_children==0:
            if node_parent!=None:
                if node_parent.left==node:
                    node_parent.left=None
                else:
                    node_parent.right=None
            else:
                self.root=None
        
        if node_children==1:
            if node.left!=None:
                child=node.left
            else:
                child=node.right
            if node_parent!=None:
                if node_parent.left==node:
                    node_parent.left=child
                else:
                    node.parent.right=child
            else:
                self.root=child
            child.parent=node_parent

        if node_children==2:
            successor=min_value_node(node.right)
            node.value=successor.value
            self.delete_node(successor)

    def search(self, value):
        if self.root!=None:
            return self._search(value, self.root)
        else:
            return False
    
    def _search(self, value, cur_node):
        if value==cur_node.value:
            return True
        elif value<cur_node.value and cur_node.left!=None:
            return self._search(value, cur_node.left)
        elif value>cur_node.value and cur_node.right!=None:
            return self._search(value, cur_node.right)
        return False

def insert_arr(tree, arr):
    for i in arr:
        tree.insert(i)
    return tree

def deletePostorder(node, tree):
    if node==None:
        return 
    deletePostorder(node.left, tree)
    deletePostorder(node.right, tree)
    tree.delete_node(node)
    node=None

def returnInorder(node):
    if node==None:
        return []
    l = returnInorder(node.left)
    r = returnInorder(node.right)
    return l + [node.value] + r

def returnPostorder(node):
    lst = []
    if node:
        lst = returnPostorder(node.left)
        lst.extend(returnPostorder(node.right))
        lst.append(node)
    return lst

def sortedArrayToBST(arr):
    if not arr:
        return None
    mid = (len(arr)-1) // 2
    root = Node(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])
    return root

def preorder(root):
    lst = []
    if root:
        lst.append(root.value)
        lst.extend(preorder(root.left))
        lst.extend(preorder(root.right))
    return lst