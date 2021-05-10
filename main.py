from copy import deepcopy

class node:
    def __init__(self, value=None, left = None, right = None, parent = None):
        self.value = value
        self.right = right
        self.left = left
        self.parent = parent

    def addValue(self, value):
        if self.value == None:
            self.value = value
            return
        current = self
        while True:
            if value < current.value:
                if current.left == None:
                    current.left = node(value, parent = current)
                    break
                current = current.left
            elif value > current.value:
                if current.right == None:
                    current.right = node(value, parent = current)
                    break
                current = current.right
            else:
                print("Value is in the tree.")
                return
        while current.parent != None:
            current = current.parent
        self.left = current.left
        self.right = current.right

    def addValues(self, values):
        lenValues = len(values)
        if lenValues == 0:
            pass
        elif lenValues%2 == 0:
            self.addValue(values[int(lenValues/2)])
            self.addValues(values[0:int(lenValues/2)])
            self.addValues(values[int(lenValues/2)+1:lenValues])
        elif lenValues == 1:
            self.addValue(values[0])
        elif lenValues%2 == 1:
            self.addValue(values[int((lenValues-1)/2)])
            self.addValues(values[0:int((lenValues-1)/2)])
            self.addValues(values[int((lenValues-1)/2)+1:lenValues])

    def preOrder(self, toReturn = []):
        current = self
        if current.parent == None:
            toReturn = []
        toReturn.append(current.value)
        if current.left != None:
            current.left.preOrder(toReturn)
        if current.right != None:
            current.right.preOrder(toReturn)
        if current.parent == None:
            return toReturn

    def postOrder(self, toReturn = []):
        current = self
        if current.parent == None:
            toReturn = []
        if current.left != None:
            current.left.postOrder(toReturn)
        if current.right != None:
            current.right.postOrder(toReturn)
        toReturn.append(current.value)
        if current.parent == None:
            return toReturn

    def inOrder(self, toReturn = []):
        current = self
        if current.parent == None:
            toReturn = []
        if current.left != None:
            current.left.inOrder(toReturn)
        toReturn.append(current.value)
        if current.right != None:
            current.right.inOrder(toReturn)
        if current.parent == None:
            return toReturn

    def findMin(self):
        current = self
        while current.left != None:
            current = current.left
        return current.value

    def findMax(self):
        current = self
        while current.right != None:
            current = current.right
        return current.value

    def removeValue(self, value, direction = "left"):
        current = self
        lastTurn = None
        while True:
            if value < current.value:
                current = current.left
                lastTurn = "left"
            elif value > current.value:
                current = current.right
                lastTurn = "right"
            else:
                break
        if current.left == None and current.right == None:
            current = current.parent
            if lastTurn == "left":
                current.left = None
            elif lastTurn == "roght":
                current.right = None
        elif (current.left != None or current.right != None) and not (current.left != None and current.right != None):
            if current.left != None:
                current = current.left
                while current.right != None:
                    current = current.right
                toSwap = current
                current = current.parent
                current.left = None
                while current.value != value:
                    current = current.parent
                current.value = toSwap.value
            elif current.left != None:
                current = current.right
                while current.left != None:
                    current = current.left
                toSwap = current
                current = current.parent
                current.right = None
                while current.value != value:
                    current = current.parent
                current.value = toSwap.value
        elif current.left != None and current.right != None:
            if direction == "left":
                current = current.left
                while current.right != None:
                    current = current.right
                toSwap = deepcopy(current)
                current = current.parent
                self.removeValue(toSwap.value)
                while current.value != value:
                    current = current.parent
                current.value = toSwap.value
            elif direction == "right":
                current = current.right
                while current.left != None:
                    current = current.left
                toSwap = deepcopy(current)
                self.removeValue(toSwap.value)
                current = current.parent
                while current.value != value:
                    current = current.parent
                current.value = toSwap.value

    def secondSort(self, values = None, newNode=None):
        trueNewNode = False
        if newNode == None:
            values = self.inOrder()
            trueNewNode = True
            newNode = node()
        lenValues = len(values)
        if lenValues == 0:
            pass
        elif lenValues%2 == 0:
            newNode.addValue(values[int(lenValues/2)-1])
            newNode.secondSort(values[0:int(lenValues/2)-1], newNode)
            newNode.secondSort(values[int(lenValues/2):lenValues], newNode)
        elif lenValues == 1:
            newNode.addValue(values[0])
        elif lenValues%2 == 1:
            newNode.addValue(values[int((lenValues-1)/2)])
            newNode.secondSort(values[0:int((lenValues-1)/2)], newNode)
            newNode.secondSort(values[int((lenValues-1)/2)+1:lenValues], newNode)
        if trueNewNode:
            return newNode



model = node()
toAdd = [10,7,9,1,5,4,8,12,11,17,16,15]
toAdd.sort()

model.addValues(toAdd)

print("---")

print(model.preOrder())

newNode = model.secondSort()

print(model.preOrder())
print(newNode.preOrder())
