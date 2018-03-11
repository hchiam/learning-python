# import and rename shorter
import linked_list_node as llnode
Node = llnode.Node

def remove(head,val):
    if head == None:
        return None
    elif head.data == val:
        return head.next
    else:
        n = head
        while n.next:
            if n.next.data == val:
                n.next = n.next.next
                return head
            n = n.next
    return head

# unit testing
import unittest
class test(unittest.TestCase):
    def test_values(self):
        a = Node(1)
        self.assertEqual(a.data, 1)
        a.add(2)
        remove(a,2)
        self.assertEqual(a.data, 1)
        self.assertEqual(a.next, None)
unittest.main()
