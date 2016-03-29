#!/usr/bin/env python3
#antuor:Alan

class AlanError(Exception):
    def __init__(self,msg):
        self.message = msg
    def __str__(self):
        return self.message
try:
    raise AlanError("我的异常")
except AlanError as e:
    print(e)
else:
    print (1)
finally:
    print("a")

