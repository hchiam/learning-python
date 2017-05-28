import time # to be able to add delays between prints

class node(object):
    val = None # value of node
    refL = None # right node if >
    refR = None # left node if =<
    
    def __init__(self,val):
        self.val = val
    
    def branch(self,newVal):
        if newVal > self.val:
            if self.refR == None:
                self.refR = node(newVal)
            else:
                self.refR.branch(newVal)
        elif newVal <= self.val:
            if self.refL == None:
                self.refL = node(newVal)
            else:
                self.refL.branch(newVal)
    
    def getPrintOut(self,currNode,level=1):
        # get current node
        output = str(currNode.val)
        # get left node or its branches
        if currNode.refL != None:
            output += str(self.getPrintOut(currNode.refL,level+1))
        # get right node or its branches
        if currNode.refR != None:
            output += "\n" + " "*level + str(self.getPrintOut(currNode.refR,level+1))
        return output


print("\ntree node Branching and Printout example")
print("")
print("")
time.sleep(2)
print("\n\"BRANCH\" = Larger number ; \"GROWTH\" = Smaller or Equal number\n")
time.sleep(3)

tree = node(1)

nodesToAdd = [5,3,7,2,4,6,0,9,8]

print('nodesToAdd = ', nodesToAdd, '\n')
time.sleep(1)

for currNode in nodesToAdd:
    # print tree so far
    print(tree.getPrintOut(tree))
    # add new line for final output
    print()
    # add branch to tree
    tree.branch(currNode)
    time.sleep(1)
