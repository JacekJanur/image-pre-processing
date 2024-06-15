from PIL import Image, ImageOps
import os, os.path

from image_processor import ImageProcessor

path = "./images"
valid_images = [".jpg",".gif",".png",".tga"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    
    with Image.open(f'{path}/{f}') as im:
        im = ImageOps.exif_transpose(im)
        processor = ImageProcessor(im)
        processor.resize()
        processor.add_colored_shape()
        processor.add_text(f.split('.')[0].capitalize())
        processor.save(f'{path}/changed_{f}')
