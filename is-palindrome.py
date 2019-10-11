def is_palindrome(sequence):
  # zip() and reversed() don't copy the list, and instead return lazy iterators
  # so this does not take extra memory
  for n, m in zip(sequence, reversed(sequence)):
    if n != m:
      return False
  return True
