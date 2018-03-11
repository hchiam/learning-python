class Node():
    def __init__(self,d):
        self.data = d
        self.next = None
    def add(self,d):
        if self.next == None:
            self.next = Node(d)
        else:
            self.next.add(d)

if __name__ == '__main__':
    # create and append 7 nodes
    n = Node(1)
    n.add(2)
    n.add(3)
    n.add(4)
    n.add(5)
    n.add(6)
    n.add(7)
    v = n
    while v != None:
        print(v.data)
        v = v.next
