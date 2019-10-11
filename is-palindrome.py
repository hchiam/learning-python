def is_palindrome(sequence):
  # zip() and reversed() don't copy the list,
  # and instead return lazy iterators
  # so this does not take extra memory
  
  # all() checks if all values are true in the generator
  # alternatively, we could use "not any(n != m ..." (albeit harder to read)
  return all(
    n == m
    for n, m in zip(sequence, reversed(sequence))
  )

is_palindrome('1a12') # False
is_palindrome('1a1') # True
