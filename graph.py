# キューの実装
class Queue():
    def __init__(self):
        self.queue_list = []

    def enqueue(self, data):
        self.queue_list.insert(0, data)

    def dequeue(self):
        self.queue_list.pop()

    def size(self):
        return len(self.queue_list)
    
    def print(self):
        print(self.queue_list)

# グラフの実装
class Graph:
    def __init__(self):
