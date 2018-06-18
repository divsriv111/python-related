class Queue(object):
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return self.item==[]
    def enqueue(self,item):
        self.item.append(item)
    def dequeue(self):
        return self.item.pop()
    def size(self):
        return len(self.item)
