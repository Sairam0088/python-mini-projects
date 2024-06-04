#Image resizer

from PIL import Image

def image_resizer(input_path,output_path,size):
    original_image = Image.open(input_path)
    resized_image = original_image.resize(size)
    resized_image.save(output_path)
    print("Image resized to",size)

input_path = "gif creater\\image3.jpg"
size = (300, 200)
output_path = "gif creater\\image2.jpg"

image_resizer(input_path,output_path,size)