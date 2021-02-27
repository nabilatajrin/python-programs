import os

# Function to move files
def main():
    prevName = '/media/iit/Workspace/test/3.ppm.bz2'
    newName = '/media/iit/Workspace/test/destFolder/test/5.ppm.bz2'
    os.rename(prevName, newName)

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
