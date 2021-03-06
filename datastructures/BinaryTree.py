class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def findVal(self, data):
        if self.data is None:
            print("Empty tree!!")
            return
        if data < self.data:
            if self.left is None:
                print(str(data)+" Not Found !")
                return
            return self.left.findVal(data)
        elif data > self.data:
            if self.right is None:
                print(str(data)+" not Found !")
                return
            return self.right.findVal(data)
        else:
            print("Data found {:1}".format(self.data))


    def printTree(self):
        if self.data:
            print(self.data)
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()


if __name__ == "__main__":
    root = Node(10)
    root.insert(4)
    root.insert(16)
    root.insert(8)
    root.insert(20)
    root.printTree()
    root.findVal(16)
    root.findVal(55)


