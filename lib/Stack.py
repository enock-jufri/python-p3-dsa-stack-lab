class Stack:

    def __init__(self, items = [], limit = 100):
        self.items=items
        self.limit=limit

    def isEmpty(self):
        return len(self.items)==0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items)!=0:
            return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        stack_b=[]
        for i in range(self.limit):
            stack_b.append(self.items[i])
        self.items.clear()
        self.items=stack_b
        return stack_b

    def search(self, target):
        print(self.items)
        for i in range(len(self.items)):
            if target==self.items[i]:
                return len(self.items)-1 - i
        
        return -1


