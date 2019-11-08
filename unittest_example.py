import unittest, gc

class TestCase(unittest.TestCase):
  """
  must start with the word "test" or "Test"
  """
  def setUp(self):
    self.a = 1
  def tearDown(self):
    gc.collect()
  def testEquals(self):
    """
    must start with the word "test" (lowercase) but NOT "Test"
    """
    assert self.a == 1, 'not 1'

unittest.main(argv=[''],exit=False)
