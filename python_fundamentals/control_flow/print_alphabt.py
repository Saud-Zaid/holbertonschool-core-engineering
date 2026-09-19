#!/usr/bin/env python3
output = ""
for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'e' and chr(i) != 'q':
        output += chr(i)
print(output)
