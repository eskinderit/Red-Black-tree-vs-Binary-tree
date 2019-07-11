import pickle
import statistics
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import random
import sys
class BstVertex:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.p = None
        self.key = key

class BinaryT:

    # Constructor
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def setRoot(self, x):
        self.root = x

    def insert(self, k):

        z = BstVertex(k)
        y = None
        x = self.root

        while x is not None:
            y = x
            if z.key <= x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.setRoot(z)
        elif z.key < y.key:
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
        elif x.key == key:
            return True
        elif key < x.key:
            return self.findSub(x.left, key)
        else:
            return self.findSub(x.right, key)

    def find(self, key1):
        return self.findSub(self.root, key1)

    def PreOrderTreeWalk(self, x):
        if x is not None:
            print(x.key)
            self.InorderTreeWalk(x.left)
            self.InorderTreeWalk(x.right)

class BrVertex(BstVertex):
    def __init__(self, key):
        super().__init__(key)
        self.color = None

    def setColor(self, col):
        if col == "R" or col == 1:
            self.color = 1
        elif col == "B" or col == 0:
            self.color = 0
        else:
            print("ERRORE NELL' IMMISSIONE COLORE")

class BrT:
    def __init__(self):
        self.NilVertex=BrVertex(None)
        self.NilVertex.color = 0
        self.root = self.NilVertex

    def InorderTreeWalk(self, x):
        if x != self.NilVertex:
            self.InorderTreeWalk(x.left)
            print(x.key)
            self.InorderTreeWalk(x.right)

    def PreOrderTreeWalk(self,x):
        if x != self.NilVertex:
            print(x.key)
            self.InorderTreeWalk(x.left)
            self.InorderTreeWalk(x.right)

    def insert(self, k):

        z = BrVertex(k)
        y = self.NilVertex
        x = self.root
        while x != self.NilVertex:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.NilVertex:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.NilVertex
        z.right = self.NilVertex
        z.color = 1
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.p.color == 1:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == 1:
                    z.p.color = 0
                    y.color = 0
                    z.p.p.color = 1
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.leftRotate(z)
                    z.p.color = 0
                    z.p.p.color = 1
                    self.rightRotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == 1:
                    z.p.color = 0
                    y.color = 0
                    z.p.p.color = 1
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.rightRotate(z)
                    z.p.color = 0
                    z.p.p.color = 1
                    self.leftRotate(z.p.p)
        self.root.color = 0
    def leftRotate(self,x):
        y = x.right
        x.right = y.left
        if y.left != self.NilVertex:
            y.left.p = x
        y.p = x.p
        if x.p == self.NilVertex:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def rightRotate(self,y):
        x = y.left
        y.left = x.right
        if x.right != self.NilVertex:
            x.right.p = y
        x.p = y.p
        if y.p == self.NilVertex:
            self.root=x
        elif y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x
        x.right = y
        y.p = x

    def find(self, key1):
        return self.findSub(self.root, key1)

    def findSub(self, x, key):
        if x is self.NilVertex:
            return False
        elif x.key == key:
            return True
        elif key < x.key:
            return self.findSub(x.left, key)
        else:
            return self.findSub(x.right, key)


# TODO self e right rotate
# TODO controllare da else in poi il fixup
#TODO cancellazione su ABR (Cose' che manca, che non abbiamo fatto a lezione??)
#TODO cancellazione su ARN non obbligatoria
#TODO inserimento con fixup
#TODO test


# T=BinaryT()
#
# T.insert(4)
# T.insert(7)
# T.insert(2)
# T.insert(6)
# T.insert(5)
# T.insert(1)
# T.insert(7)
# T.insert(3)
#
# print(T.find(10))
# #print(T.getRoot().getKey())
# T.InorderTreeWalk(T.root)
#
# B = BrVertex(5)
# B.setColor(5)
# B.setColor(1)
# print(B.color)
# print(B.key)

# print ("prove Alberi RN")
# OK = BrT()
#
#
# OK.insert(10)
#
# print("radice: ", OK.root.key)
#
# OK.insert(7)
# OK.insert(3)
# OK.PreOrderTreeWalk(OK.root)

# print("radice: ", OK.root.key)

############################## TESTS START ###############################

# receiving a Tree, inserts a vector of values in it

def BST_multiple_insert(T,A):
    start=timer()
    for i in range (0,len(A)):
        T.insert(A[i])
    end=timer()
    return end-start


def RBT_multiple_insert(T,A):
    start = timer()
    for i in range(0, len(A)):
        T.insert(A[i])
    end=timer()
    return end-start
# receiving a Tree, finds num numbers


def BST_multiple_search(T,num):
    start = timer()
    for i in range(0, num):
        T.find(random.randint(0, 100000))
    end = timer()
    return end-start


def RBT_multiple_search(T,num):
    start = timer()
    for i in range(0, num):
        T.find(random.randint(0, 100000))
    end = timer()
    return end-start


def test_insert(File, repeat):
    BSTSearchGraph = []
    RBTGraph = []
    pickle_in = open(File, "rb")
    Set = pickle.load(pickle_in)
    Set1 = Set.copy()
    for j in range(1, len(Set)):
        print("Test: ", File, "Passo: ", j, "/", len(Set))
        R1 = []
        M1 = []
        T1=BinaryT()
        T2=BrT()
        for k in range(0, repeat):
            R1.append(BST_multiple_insert(T1, Set[j]))
            M1.append(RBT_multiple_insert(T2, Set1[j]))
        BSTSearchGraph.append(statistics.mean(R1))
        RBTGraph.append(statistics.mean(M1))
    Set = []
    ElementsNum = []
    pickle_in = open(File, "rb")
    Set = pickle.load(pickle_in)
    for z in range(1, len(Set)):
        A = Set[z]
        ElementsNum.append(len(A))
    plt.plot(ElementsNum, BSTSearchGraph)
    plt.plot(ElementsNum, RBTGraph)
    plt.xlabel('Numero di elementi')
    plt.ylabel('Tempo di esecuzione')
    plt.title('Inserimento: Albero Binario vs Albero RN')
    plt.legend(['Albero binario', 'Albero RN'])
    plt.show()


def test_search(File, numberstosearch,rep):
    BSTSearchGraph = []
    RBTGraph = []
    pickle_in = open(File, "rb")
    Set = pickle.load(pickle_in)
    Set1 = Set.copy()
    for j in range(1, len(Set)):
        print("Test: ", File, "Passo: ", j, "/", len(Set))
        T1=BinaryT()
        T2=BrT()
        BST_multiple_insert(T1, Set[j])
        RBT_multiple_insert(T2, Set1[j])
        BI=[]
        RI=[]
        for k in (0, rep+1):
            BI.append(BST_multiple_search(T1, numberstosearch + 1))
            RI.append(RBT_multiple_search(T2, numberstosearch + 1))
        BSTSearchGraph.append(statistics.mean(BI))
        RBTGraph.append(statistics.mean(RI))

    Set = []
    ElementsNum = []
    pickle_in = open(File, "rb")
    Set = pickle.load(pickle_in)
    for z in range(1, len(Set)):
        A = Set[z]
        ElementsNum.append(len(A))
    plt.plot(ElementsNum, BSTSearchGraph)
    plt.plot(ElementsNum, RBTGraph)
    plt.xlabel('Numero di elementi')
    plt.ylabel('Tempo di esecuzione')
    plt.title('Ricerca: Albero Binario vs Albero RN')
    plt.legend(['Albero binario', 'Albero RN'])
    plt.show()

sys.setrecursionlimit(4100)

print(sys.getrecursionlimit())


##### INSERT TESTS #####

#test_insert("randomBigDataset.pickle",1 )


##### SEARCH TESTS #####


#test_search("incrBigDataset.pickle", 20000, 50)
#test_search("randomBigDataset.pickle", 20000, 500)
#test_search("ordBigDataset2.pickle", 40000, 30)
