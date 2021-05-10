from bst            import binary_search_tree, insert_arr,returnInorder, sortedArrayToBST, preorder
from data_generator import randomSubset
from copy           import deepcopy
import              pandas as pd
import              xlsxwriter
import              sys
sys.setrecursionlimit(1000000000)

elements =  []
bst      =  []
avl      =  []

if __name__=='__main__':
    
    dataSets=randomSubset(25000,1000)

    for a in dataSets:

        tree=binary_search_tree()
        tree=insert_arr(tree, a)
        bst.append(tree.height())

        inorder=returnInorder(tree.root)
        root = sortedArrayToBST(inorder)
        p=preorder(root)

        avltree=binary_search_tree()
        avltree=insert_arr(avltree, p)
        avl.append(avltree.height())

        elements.append(len(a))

df = pd.DataFrame.from_dict(
    {
        'rozmiar zbioru'    :   elements, 
        'BST height'        :   bst, 
        'AVL height'        :   avl, 
    }
)

df.to_excel('avl.xlsx', header=True, index=False)