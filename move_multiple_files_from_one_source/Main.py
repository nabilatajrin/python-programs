import os

# Function to move files
def main():

    src = '/media/iit/R a i n/2019/Intelligent Machines Ltd/face-propagation/dummy-data-set/colorferet/colorferet/dvd2/gray_feret_cd2/data/images'
    dst = '/media/iit/R a i n/2019/Intelligent Machines Ltd/face-propagation/dummy-data-set/colorferet/colorferet/dvd1/data/images/dstFolder_01/'

    for filename in os.listdir(src):
        print(filename)

        srcFolder = src + '/' + filename
        dstFolder = dst + filename

        # move all the files
        os.rename(srcFolder, dstFolder)

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()