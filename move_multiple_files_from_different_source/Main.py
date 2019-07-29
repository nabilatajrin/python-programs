import os

# Function to move files
def main():

    for filename in os.listdir("/media/iit/Workspace/test/multipleSrc"):
        print(filename)

        i = 1
        for filename2 in os.listdir("/media/iit/Workspace/test/multipleSrc/" + filename):
            print(filename2)

           #file = str(i) + ".ppm.bz2"
            src = '/media/iit/Workspace/test/multipleSrc/' + filename + '/' + filename2
            dst = '/media/iit/Workspace/test/multipleSrc/dstFolder/' + filename2

            # move all the files
            os.rename(src, dst)

            i += 1

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()