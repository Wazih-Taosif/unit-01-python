import sys

# sys.argv[0] is the script name
# sys.argv[1] is the first argument
if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}!")
else:
    print("Hello, stranger!")