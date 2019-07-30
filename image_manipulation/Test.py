size_300 = (300, 300)

#resize the image to 300*300 and save into 300 folder
        image1.thumbnile(size_300)
        image1.save('300/{}_300{}'.format(fn, fext))