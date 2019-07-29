import os

# Function to move files
def main():

    src = '/media/iit/Workspace/test/multipleSrc'
    dst = '/media/iit/Workspace/test/multipleSrc/dstFolder'

    for filename in os.listdir(src):
        print(filename)

        for filename2 in os.listdir(src + "/" + filename):
            print(filename2)

            srcFolder = src + '/' + filename + '/' + filename2
            dstFolder = dst + '/' + filename2

            # move all the files
            os.rename(srcFolder, dstFolder)

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()