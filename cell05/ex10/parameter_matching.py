import sys

if len(sys.argv) == 1:
    print("nope")
    sys.exit()

x = input("What was the parameter? : ")

if x == sys.argv[1]:
    print("Good Job!")
else:
        print("Nope , Sorry")

print(x)
print(sys.argv[1:])