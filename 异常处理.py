#!/usr/bin/env python3
#antuor:Alan

try:
    a = [12.23,31]
    1 + a
except TypeError as a: #(python2.7except Exception,e)

    a = 3
    b = 1 + a
    print(b)
else:
    pass
finally:
    pass



try:
    pass
except ValueError: #从详细到万能，详细在万能之上
    pass
except Exception:
    pass