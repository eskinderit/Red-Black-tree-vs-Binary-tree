import pickle
import statistics
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import random
import sys

def random_vect(B):
    A=[]
    for i in range(B+1):
      A.append(random.randint(1, 800)) #TODO random.seed
    return A


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
        while x is not None and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def find(self, key1):
        return self.findSub(self.root, key1)

    def PreOrderTreeWalk(self, x):
        if x is not None:
            print(x.key)
            self.InorderTreeWalk(x.left)
            self.InorderTreeWalk(x.right)

    def maxDepth(self,x):
        if x is None:
            return 0
        else:
            leftHeight = self.maxDepth(x.left)
            rightHeight = self.maxDepth(x.right)
            return max(leftHeight, rightHeight) + 1


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
        if y.p.key == self.NilVertex.key:
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
        while x.key is not None and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def maxDepth(self, x):
        if x == self.NilVertex:
            return 0
        else:
            leftHeight = self.maxDepth(x.left)
            rightHeight = self.maxDepth(x.right)
            return max(leftHeight, rightHeight) + 1


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
    Times = []
    for i in range(0, len(num)):

        start = timer()
        T.find(random.randint(1, 9000))
        end = timer()
        Times.append(end-start)
    return statistics.mean(Times)


def RBT_multiple_search(T,num):
    Times = []
    for i in range(0, len(num)):

        start = timer()
        T.find(random.randint(1, 9000))
        end = timer()
        Times.append(end-start)
    return statistics.mean(Times)


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
   #TODO cambiare sul grafico il numero di elementi
    T1 = BinaryT()
    T2 = BrT()
    for j in range(1, len(Set)):
        print("Test: ", File, "Passo: ", j, "/", len(Set))
        BST_multiple_insert(T1, Set[j])
        RBT_multiple_insert(T2, Set[j])
        BI=[]
        RI=[]
        print("Altezza albero binario:", T1.maxDepth(T1.root))
        print("Altezza albero r-n:", T2.maxDepth(T2.root))
        rand_search = random_vect(numberstosearch)
        for k in range(0, rep+1):

            BI.append(BST_multiple_search(T1, rand_search))
            RI.append(RBT_multiple_search(T2, rand_search))
        BSTSearchGraph.append(statistics.mean(BI))
        RBTGraph.append(statistics.mean(RI))
        print("Tempo ABR: ",statistics.mean(BI))
        print("Tempo ARN:", statistics.mean(RI))

    Set = []
    ElementsNum = []
    pickle_in = open(File, "rb")
    Set = pickle.load(pickle_in)
    for z in range(1, len(Set)):
        A = Set[z]
        ElementsNum.append(len(A))
    plt.plot(ElementsNum, BSTSearchGraph,'--bo')
    plt.plot(ElementsNum, RBTGraph,'--ro')
    plt.xlabel('Numero di elementi (N)')
    plt.ylabel('Tempo di esecuzione (t)')
    plt.title('Ricerca: Albero Binario vs Albero RN')
    plt.legend(['Albero binario', 'Albero RN'])

    plt.grid(True)
    plt.xticks(ElementsNum)



    plt.show()


################### INSERT TESTS #######################

# AVERAGE CASE
#test_insert("randomBigDataset.pickle", 1)

# ORDERED CASE
#test_insert("incrBigDataset.pickle", 2)    FATTO



#################### SEARCH TESTS #####################

# AVERAGE CASE
#test_search("decrBigDataset.pickle", 20000, 10)
# ORDERED CASE
test_search("randomBigDataset.pickle", 4000, 200)


#
# pickle_in = open("decrBigDataset.pickle", "rb")
# Set = pickle.load(pickle_in)
#
# T1 = BinaryT()
# T2 = BrT()
# Set1 = Set.copy()
#
#
# BST_multiple_insert(T1, Set[9])
# print(T1.maxDepth(T1.root))
#
# RBT_multiple_insert(T2, Set1[9])
# print(T2.maxDepth(T2.root))
