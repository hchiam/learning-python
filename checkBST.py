from timeperfdecorator import timePerfWrapper

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# need to check if ALL left/(right) descendants are less/(more) than root!

def getAllDataBelowAndAt(node):
    list_l = [node.data]
    if node.left != None:
        list_l.extend(getAllDataBelowAndAt(node.left))
    if node.right != None:
        list_l.extend(getAllDataBelowAndAt(node.right))
    return list_l

def check_order(node):
    if node == None:
        return True
    else:
        # get data from all nodes grouped by left subtree and right subtree
        l = node.left
        r = node.right
        list_l_subtree = []
        list_r_subtree = []
        if l != None:
            list_l_subtree = getAllDataBelowAndAt(l)
        if r != None:
            list_r_subtree = getAllDataBelowAndAt(r)
        # are they alll less than this node?
        check_l = True
        for vals in list_l_subtree:
            if vals >= node.data:
                check_l = False
        check_r = True
        for vals in list_r_subtree:
            if vals <= node.data:
                check_r = False
        check_l_and_r = check_l and check_r
        return check_l_and_r and check_order(l) and check_order(r)

# def check_gets_smaller(node):
#     l = node.left
#     if l == None:
#         return True
#     else:
#         if l.data >= node.data:
#             return False
#         else:
#             return check_gets_smaller(l) and check_gets_bigger(l)
# 
# def check_gets_bigger(node):
#     r = node.right
#     if r == None:
#         return True
#     else:
#         if r.data <= node.data:
#             return False
#         else:
#             return check_gets_bigger(r) and check_gets_smaller(r)

@timePerfWrapper
def check_binary_search_tree_():
    root = a
    # checks = check_gets_smaller(root) and check_gets_bigger(root) and check_order(root)
    checks = check_order(root)
    print '\nBinary Search Tree? ' + str(checks)


# 2
# 1 2 3 4 5 6 7
# Yes

a = node(4)
b = node(2)
c = node(6)
d = node(1)
e = node(3)
f = node(5)
g = node(7)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

check_binary_search_tree_()

# 2
# 1 2 4 3 5 6 7
# No
# why? the 4!!! it's to the left of the 3! (wouldn't be there in normal BST insertion)

a = node(3)
b = node(2)
c = node(6)
d = node(1)
e = node(4)
f = node(5)
g = node(7)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

check_binary_search_tree_()