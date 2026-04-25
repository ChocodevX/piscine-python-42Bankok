import sys

if len(sys.argv) == 1:
    print("nope")
    sys.exit()

def downcase_it(s):
    return s.lower()

x = len(sys.argv)

for i in range(1, x):
    print(downcase_it(sys.argv[i]))
