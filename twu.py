from ll             import LinkedList
from bst            import binary_search_tree, insert_arr, returnPostorder
from data_generator import randomSubset
from timeit         import default_timer as timer
from copy           import deepcopy
import              pandas as pd
import              xlsxwriter

linked_creation =   []
linked_search   =   []
linked_deletion =   []
binary_creation =   []
binary_search   =   []
binary_deletion =   []
elements        =   []

if __name__=='__main__':
    
    dataSets=randomSubset(25000, 1000)

    # with open('bst.txt', 'r') as f:
    #     dataSets=[[]]
    #     for line in f:
    #         line=line.replace('\n','')
    #         dataSets[0].append(int(line))

    for a in dataSets:

        # d=deepcopy(a)
        # d.sort()
        start=timer()
        ll=LinkedList()
        ll.insert_values(a, 1)
        endtime=timer()-start
        linked_creation.append(endtime)

        start=timer()
        for i in a:
            ll.exist(i)
        endtime=timer()-start
        linked_search.append(endtime)
        
        start=timer()
        ll.delete()
        endtime=timer()-start
        linked_deletion.append(endtime)

        start=timer()
        tree=binary_search_tree()
        tree=insert_arr(tree, a)
        endtime=timer()-start
        binary_creation.append(endtime)

        start=timer()
        for i in a:
            tree.search(i)
        endtime=timer()-start
        binary_search.append(endtime)

        postorder=returnPostorder(tree.root)

        if len(a)>0:
            start=timer()
            for p in postorder:
                tree.delete_node(p)
            endtime=timer()-start
            binary_deletion.append(endtime)
        else:
            start=timer()
            endtime=timer()-start
            binary_deletion.append(endtime)

        elements.append(len(a))

df = pd.DataFrame.from_dict(
    {
        'rozmiar zbioru'    :   elements, 
        'LL creation'       :   linked_creation, 
        'BST creation'      :   binary_creation, 
        'LL search'         :   linked_search, 
        'BST search'        :   binary_search, 
        'LL deletion'       :   linked_deletion, 
        'BST deletion'      :   binary_deletion
    }
)

df.to_excel('twu.xlsx', header=True, index=False)