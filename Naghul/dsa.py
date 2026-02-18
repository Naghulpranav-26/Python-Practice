class listadt:
    def__init__(self,max_size):
        self.array=[]
        self.max_size=max_size
    def is_empty(self):
        return len(self.array)==0
    def insert_front(self,item):
        if self.is_full():
            raise exception("List is full")
        self.array.insert(0,item)
    def insert_end(self,item):
        if self.is_full():
            raise exception("List is Full")
        self.array.append(item)
    def insert_at(self,index,item):
        if self.is_full():
            raise exception("List is Full")
        if index<0 or index>len(self.array):
            raise index error ("Index out of range")
        self.array.insert(index,item)
    def delete_front(self):
        if self.is_empty
