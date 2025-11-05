""" Modes:->
            r - read
            w - write (re-write every time)
            a - append
            r+ - read + write (file should exist)
            w+ - read + write (file will be created if not exist)
            a+ - read + add (file will be created if not exist
"""

# with open('main') as f:
#     print(f.read())
lines_to_write = ['line1', 'line2', 'line3']
# with open('test.log', 'w') as f:
#     f.write('\n'.join(lines_to_write))

with open('test.log', 'a') as f:
    f.write('\n'.join(lines_to_write))