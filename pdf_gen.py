#This program assumes all the images have been named as follows: page<number><.extension>
#Importing modules
from PIL import Image

#Enter start and End number of images
start = 1
end = 200
#Insert image type extension here:
im_type = ".png"
#Insert the directory here
dir = ""
filename = "file.pdf"

im_list = []
for i in range(start, end + 1):
    image = dir + "/page" + str(i) + im_type
    im_list.append(Image.open(image).convert("RGB"))
im_list[0].save(dir + "/" + filename, save_all = True, append_images = im_list)
