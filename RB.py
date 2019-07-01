
class BstVertex:
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
    def insert(self, k):
        z = BstVertex(k)
        y = None
        x = self.root

        while x is not None:
            y = x
            if z.getKey() <= x.getKey():
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
    def findSub(self, x, key):
        if x is None:
            return False
        elif x.getKey() == key:
            return True
        elif key < x.getKey():
            return self.findSub(x.left, key)
        else:
            return self.findSub(x.right, key)

    def find(self, key1):
        return self.findSub(self.root, key1)


class BrVertex(BstVertex):
    def __init__(self):
        self.color = None
    def setColor(self, col):
        self.color=col
    def getColor(self):
        return self.color

T = BinaryT()

T.insert(4)
T.insert(7)
T.insert(2)
T.insert(6)
T.insert(5)
T.insert(1)
T.insert(7)
T.insert(3)

print(T.find(10))
#print(T.getRoot().getKey())
T.InorderTreeWalk(T.root)

B=BrVertex()
B.setColor("black")
print(B.getColor())
