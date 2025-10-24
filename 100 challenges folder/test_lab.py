"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
    except FileNotFoundError:
        print("Error: File not found.")
    else:
        print("File contents:", contents)
    finally:
        print()
        print("----------End of file content-----------")

# Example usage:
process_file("example.txt")