import os
import tkinter as tk
from tkinter import filedialog

import customtkinter as ctk
from PIL import Image, ImageDraw, ImageFont

import constants as c

class App(ctk.CTk):
    """App GUI Class."""
    def __init__(self):
        super().__init__()
        self.geometry(f"{c.WIN_W}x{c.WIN_H}")
        self.title("DK Image Stamper")
        self.minsize(c.WIN_W, c.WIN_H)
        self.maxsize(c.WIN_W, c.WIN_H)
        self.iconbitmap(f"{os.path.dirname(__file__)}/icons/dk.ico")
        self.font = ctk.CTkFont(c.FONT[0], c.FONT[1], c.FONT[2])

        self.browse_frame = ctk.CTkFrame(master=self)
        self.browse_frame.grid(row=0, column=0, padx=10, pady=5)
        self.browse_entry = ctk.CTkEntry(master=self.browse_frame, placeholder_text='Image Folder:', font=c.FONT, width=c.FOLDER_W)
        self.browse_entry.grid(row=0, column=0, padx=10, pady=5)
        self.browse_btn = ctk.CTkButton(master=self.browse_frame, text='Browse', command=self.browse_callback, font=c.FONT)
        self.browse_btn.grid(row=0, column=1, padx=10, pady=5)


    def browse_callback(self):
        directory = filedialog.askdirectory()
        if directory != "":
            print(directory)
            self.stamp(directory)

    def stamp(self, directory):
        """Takes a folder and """
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
                combined_image.paste(image, (0, 0))
                combined_image.paste(text_image, (0, height))

                new_filename = os.path.splitext(filename)[0] + '_stamped.jpg'
                combined_image.save(os.path.join(subfolder_path, new_filename))

if __name__ == "__main__":
    app = App()
    app.mainloop()
