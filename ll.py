class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def print(self):
        if self.head is None:
            print('{}')
            return
        itr=self.head
        listr=''
        while(itr):
            listr+=str(itr.data)+', '
            itr=itr.next
        print('{'+listr+'}')

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def get_index(self, data):
        count=0
        itr=self.head
        while itr:
            if itr.data==data:
                return count
            count+=1
            itr=itr.next
        return count
    
    def exist(self, data):
        itr=self.head
        while itr:
            if itr.data==data:
                return True
            itr=itr.next

    def get_place(self, data):
        count=0
        itr=self.head
        while itr:
            if itr.data>data:
                return count
            count+=1
            itr=itr.next
        return count

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception('Invalid index')
        if index==0:
            self.insert_at_beginnig(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data, itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
            
    def insert_at_end(self, data):
        if self.head is None:
            self.head=Node(data, None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data, None)
    
    def insert_at_beginnig(self, data):
        node=Node(data, self.head)
        self.head=node
    
    def insert_with_sort(self, data):
        if self.head is None:
            self.head=Node(data, None)
            return
        itr=self.head
        if itr.data>data:
            count=0
            while itr:
                if count==self.get_index(itr.data):
                    self.insert_at_beginnig(data)
                    break
                elif count<self.get_index(itr.data):
                    self.insert_at_beginnig(data)
                itr=itr.next
                count+=1
        else:
            self.insert_at(self.get_place(data), data)

    def insert_values(self, data_list, switch=1):
        self.head=None
        if switch==1:
            for data in data_list:
                self.insert_with_sort(data)
        elif switch==0:
            for data in data_list:
                self.insert_at_end(data)
    
    def delete(self):
        while (self.head != None):
            self.head = None