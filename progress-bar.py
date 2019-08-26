# https://realpython.com/python-print/#printing-with-style

from time import sleep

def progress(percent=0, width=30):
    fill = width * percent // 100
    empty = width - fill
    print('\r[', '#' * fill, ' ' * empty, ']',
          f' {percent:+.1f}%',
          sep='', end='', flush=True)

for i in range(101):
    progress(i)
    sleep(0.01)

print('\n')