from PIL import Image, ImageDraw, ImageFont
import os
from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory()

if directory != "":
    print(directory)

    subfolder_name = "Stamped"
    subfolder_path = os.path.join(directory, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

    

    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):

            image_path = os.path.join(directory, filename)
            image = Image.open(image_path)

            width, height = image.size

            font_height = height//50
            font = ImageFont.truetype('arial.ttf', font_height)

            text_image = Image.new('RGB', (width, font_height+20), color='black')
            text_draw = ImageDraw.Draw(text_image)
            text_width, text_height = text_draw.textsize(os.path.splitext(filename)[0], font=font)
            text_draw.text(((width-text_width)//2, (70-text_height)//2), os.path.splitext(filename)[0], font=font, fill='white')

            combined_image = Image.new('RGB', (width, height + (font_height + 20)), color='black')
            combined_image.paste(image, (0,0))
            combined_image.paste(text_image, (0, height))

            new_filename = os.path.splitext(filename)[0] + '_stamped.jpg'
            combined_image.save(os.path.join(subfolder_path, new_filename))