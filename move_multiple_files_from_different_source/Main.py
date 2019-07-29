import os

# Function to move files
def main():
    i = 1

    for filename in os.listdir("/media/iit/Workspace/test/multipleFiles/srcFolder"):
        src = '/media/iit/Workspace/test/multipleFiles/srcFolder/' + filename
        dst = '/media/iit/Workspace/test/multipleFiles/destFolder/' + filename

        print(filename)
        # move all the files
        os.rename(src, dst)
        #i += 1

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()