import sys

def count(n):

    if n < 1:
        return
    
    
    print(sys.argv[n])
    
    
    count(n - 1)


if len(sys.argv) == 1:
    
    sys.exit()

if len(sys.argv) > 1:
    print(f"Number of parameters: {len(sys.argv) - 1}")

count(len(sys.argv) - 1)