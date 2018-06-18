class Stack(object):
    def __init__(self):
        self.item=[]
    def push(self,item):
        self.item.append(item)
    def pop(self):
        return self.item.pop()
    def peek(self):
        return self.item[len(self.item)-1]
    def isEmpty(self):
        return self.item==[]
    def size(self):
        return len(self.item)

s=Stack()
print(s.size())
print(s.push(21))
print(s.push(12))
print(s.size())

