import sys

inp = sys.stdin.readline()
for i in range(0, len(inp), 10):
    try:
        print(inp[i:i + 10])
    except IndexError:
        print(inp[i:])

