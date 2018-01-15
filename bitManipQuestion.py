# Reworked version of: https://github.com/w-hat/ctci-solutions/blob/master/ch-05-bit-manipulation/08-draw-line.py

# See CtCI for the programming question.

# Note for this question: byte != pixel (i.e. bit)

# Draw a horizontal line from (x1, y) to (x2, y).

def draw_line(screen, width, x1, x2, y):
  
  # how many bytes per row
  bytes_per_row = width / 8 # how many complete multiples of 8 fit into width
  # len = h * w .'. h = len / w
  height = len(screen) / bytes_per_row
  
  # get start and end indices
  # (account for flipped numbers)
  if x1 < x2:
    x_start, x_end = x1, x2
  else:
    x_start, x_end = x2, x1
  
  # (check for bad input)
  if x_start < 0 or x_end > width or y > height:
    return None
  
  # y starts at 0, so y * bytes_per_row = number of preceding bytes
  # x_start / 8 = number of bytes down the current row
  # x_start % 8 = number of pixels left from zero on the current byte
  # - 1 to get from 00010000 to 00001111
  byte = y * bytes_per_row + x_start / 8
  # fill the start byte
  screen[byte] = (1 << (x_start % 8)) - 1
  # + 1 to see next byte
  byte += 1
  
  # y * bytes_per_row = number of preceding bytes
  # x_end / 8 = number of bytes down the current row
  byte_end = y * bytes_per_row + x_end / 8
  
  # fill the "full" bytes between the start and end bytes
  while byte < byte_end:
    screen[byte] = 0xFF # 0xFF = 0b11111111
    byte += 1 # check the next byte
  
  # fill the end byte
  # x_end % 8 = number of pixels left from zero on the current byte
  # - 1 to get from 00010000 to 00001111
  # 0xFF ^ to get from 00001111 to 11110000 (without the complications of using ~)
  screen[byte] = 0xFF ^ ((1 << (x_end % 8)) - 1) # ^ = XOR

# instead of building testing from scratch, make use of unit testing class template
import unittest

class Test(unittest.TestCase):
  # use a def to create a test to be run by unittest.main():
  def test_draw_line(self):
    screen = [0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0]
    draw_line(screen, 64, 20, 42, 1)
    self.assertEqual(screen, [0]*8 + [0, 0, 15, 255, 255, 252, 0, 0] + [0]*8)

# if running this file directly (vs. as an import), then run the following code
if __name__ == "__main__":
  unittest.main()
