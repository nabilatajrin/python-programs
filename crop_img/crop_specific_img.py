from PIL import Image


def main():
    try:
        # Relative Path
        img = Image.open("Laabher_Bazar_07-08-2019_1601_0001.jpg")
        width, height = img.size

        #area = (0, 0, width / 2, height / 2)
        area = (60.4607142857, 335.6815286624, 144.5096938776, 397.0079617834)
        img = img.crop(area)

        # Saved in the same relative location
        img.save("cropped_picture1.jpg")

    except IOError:
        pass


if __name__ == "__main__":
    main()