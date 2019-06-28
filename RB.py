#class BT:
    #TODO Posso implementarlo come classe?
    #color
class Vertex:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.p = None
        self.key = key
    def getKey(self):
        return self.key

class BinaryT:

    # Constructor
    def __init__(self):
        self.root = None
    def getRoot(self):
        return self.root
    def setRoot(self,x):
        self.root = x
    def insert(self, z):

        y = None
        x = self.root

        while x is not None:
            y = x
            if z.getKey() < x.getKey():
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.setRoot(z)
        elif z.getKey() < y.getKey():
            y.left = z
        else:
            y.right = z
    def InorderTreeWalk(self, x):
        if x is not None:
            self.InorderTreeWalk(x.left)
            print(x.key)
            self.InorderTreeWalk(x.right)


#class RedBlackT(BinaryT):

T = BinaryT()
nodo1=Vertex(12)
nodo2=Vertex(5)
nodo3=Vertex(14)
T.insert(nodo1)
T.insert(nodo2)
T.insert(nodo3)
#print(T.getRoot().getKey())
T.InorderTreeWalk(T.root)
