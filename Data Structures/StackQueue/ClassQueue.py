#Creating a queue class in python
class Queue():
    def __init__(self):
        self.size = 0
        self.list=[]

    def enqueue(self,data):
        self.list.append(data)
        self.size+=1

    def dequeue(self,data):
        try:
            self-=1
            return self.list.pop(0)
        except Exception as error:
            print(f'{error} is not possible')

    def xprint(self,index):
        print(self.list[index])



