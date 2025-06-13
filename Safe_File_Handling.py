from contextlib import contextmanager

@contextmanager
def Safe_File(file_name , mode):
    try:
        print(f"Opening {file_name}")
        f = open(file_name , mode)
        yield f
    except FileNotFoundError as e:
        print(f"Error: {e}")
    finally:
        f.close()
        print(f"Closing {file_name}")

print("\n")

with Safe_File("demo.txt","r") as f:
    print(f.read())

print("\n")

with Safe_File("demo1.txt","w") as f:
    text = "Another Way for safe File Handling is using context manager via Class"
    f.write("text")
    print(text)

print("\n")