import sys

n = int(sys.stdin.readline().strip())
mapping = []
for i in range(n):
    line = sys.stdin.readline().strip()
    line_int = [int(char) for char in line]
    mapping.append(list(line_int))

print(mapping)