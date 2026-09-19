#!/usr/bin/env python3
def uppercase(str):
    for c in str:
        code = ord(c)
        if ord('a') <= code <= ord('z'):
            code -= 32
        print("{}".format(chr(code)), end="")
    print("")
