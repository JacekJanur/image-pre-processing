from PIL import Image, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, im: Image):
        self.im = im
        
    def add_colored_shape(self):
        draw = ImageDraw.Draw(self.im)
        draw.polygon([(0,self.im.size[0]*1/3), (0,  self.im.size[0]), (self.im.size[0],self.im.size[1])], fill = '#d09960'+ '80')
        
    def add_text(self, title: str):
        font_size = 110
        draw = ImageDraw.Draw(self.im)
        myFont = ImageFont.truetype('Poppins-Bold.ttf', font_size)
        draw.text((40, self.im.size[0]*2/3+font_size), title,  font=myFont, fill='#2b414e')
        
    def resize(self, size: int = 1080):
        aspect_ratio = self.im.width / self.im.height
        if aspect_ratio > 1: 
            new_height = size
            new_width = int(aspect_ratio * size)
        else:  
            new_width = size
            new_height = int(size / aspect_ratio)

        self.im = self.im.resize((new_width, new_height), Image.Resampling.LANCZOS)

        left = (new_width - size) / 2
        top = (new_height - size) / 2
        right = left + size
        bottom = top + size

        self.im = self.im.crop((left, top, right, bottom))
        
    def save(self, path: str):
        self.im.save(path)