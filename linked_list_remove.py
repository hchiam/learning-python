# import and rename shorter
import linked_list_node as llnode
Node = llnode.Node

def remove(head,val):
    n = head
    if head.data == val:
        return head.next
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
        a = remove(a,2)
        self.assertEqual(a.data, 1)
        self.assertNotEqual(a.data, None)
        self.assertEqual(a.next, None)
        a = remove(a,1)
        self.assertEqual(a, None)
        a = Node(1)
        a.add(2)
        a.add(3)
        a.add(4)
        a.add(5)
        a = remove(a,3)
        a = remove(a,5)
        a = remove(a,2)
        a = remove(a,4)
        a = remove(a,1)
        self.assertEquals(a, None)

if __name__ == '__main__':
    unittest.main()
