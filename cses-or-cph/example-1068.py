# https://cses.fi/problemset/task/1068/

# https://cses.fi/howto/

# a,b = [int(x) for x in input().split()]

n = int(input())
output = str(n)
while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n = n * 3+1
    output += ' ' + str(int(n))
print(output)
