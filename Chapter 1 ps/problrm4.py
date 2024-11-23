import os

# Specify the directory path
directory_path = "/Edge 40 (Krishna)"

# List and print all files and directories in the specified path
try:
    contents = os.listdir(directory_path)
    print("Contents of the directory:")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
