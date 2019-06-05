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
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
    
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect(b, a, dist)

    def connect(self, node1, node2, distance=1):
        self.graph_dict.setdefault(node1, {})[node2] = distance
        if not self.directed:
            self.graph_dict.setdefault(node2, {})[node1] = distance
    
    def get(self, node1, node2=None):
        links = self.graph_dict.setdedault(node1, {})
        if node2 is None:
            return links
        else:
            return links.get(node2)

    