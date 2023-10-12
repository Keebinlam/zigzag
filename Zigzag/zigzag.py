import time
import sys

indent = 0
indentincrease = True

try:
    while True:
        print(' ' * indent, end='')
        print('*****')
        time.sleep(.1)

        if indentincrease:
            indent = indent + 1
            if indent == 20:
                indentincrease = False
        else:
            indent = indent - 1
            if indent == 0:
                indentincrease = True

except KeyboardInterrupt:
    SystemExit
