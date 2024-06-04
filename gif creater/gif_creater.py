# gif creater 
import imageio.v3 as iio

filenames = ["gif creater\\image1.jpg","gif creater\\image2.jpg"]

images = []
for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite("gif creater\\images.gif", images, duration=500, loop= 0) 

print("Gif created successfully")