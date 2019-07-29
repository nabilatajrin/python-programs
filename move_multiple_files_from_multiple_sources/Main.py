import os

# Function to move files
def main():

    src = '/media/iit/R a i n/2019/Intelligent Machines Ltd/face-propagation/dummy-data-set/colorferet/colorferet/dvd2/smaller'
    dst = '/media/iit/R a i n/2019/Intelligent Machines Ltd/face-propagation/dummy-data-set/colorferet/colorferet/dvd1/data/images/dstFolder_01/'

    for filename in os.listdir(src):
        print(filename)

        for filename2 in os.listdir(src + '/' + filename):
            print('filename2:' + filename2)

            srcFolder = src + '/' + filename + '/' + filename2
            dstFolder = dst + filename2

            # move all the files
            os.rename(srcFolder, dstFolder)

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()