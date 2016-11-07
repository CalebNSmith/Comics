#Alex_Colegrove CS1111, Fall 2016

__author__ = 'Caleb'
import urllib3
import datetime
from PIL import Image, ImageTk
import tkinter as tk
import requests
from io import BytesIO

url_lst =  ['calvinandhobbes', 'garfield','nonsequitur' ]

class comic_image:
        comics = ""
        date = datetime.date.today()
        index = 0
        root = tk.Toplevel()
        http = urllib3.PoolManager()
        def __init__(self, arg):
            self.comics = arg

        def on_key_press(self, event):
            self.root.destroy()
            print(ord(event.char))

            if ord(event.char) == 63232:
                self.date += datetime.timedelta(days=1)

            if ord(event.char) == 63233:
                self.date -= datetime.timedelta(days=1)

            if ord(event.char) == 63234:
                self.index += 1
                if self.index > len(self.comics):
                    self.index = 0

            if ord(event.char) == 63235:
                self.index -= 1
                if self.index < 0:
                    self.index = -1
        
            self.display_image()

        def get_url(self):
            return "http://www.gocomics.com/" + self.comics[self.index] + "/" + self.date.strftime('%Y') + "/" + self.date.strftime('%M') + "/" + self.date.strftime('%d')

        def display_image(self):
            r = self.http.request('GET', self.get_url())
            strip = str(r.data).find("class=\"strip\" src=\"")
            width = str(r.data).find("\" width=\"600\" /><sp")
            start_index = strip + len("class=\"strip\" src=\"")

            image_url = str(r.data)[start_index: width]

            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            tk_img = ImageTk.PhotoImage(img)
            width = tk_img.width()
            height = tk_img.height()
            self.root.bind('<KeyPress>', test.on_key_press)
            canvas = tk.Canvas(self.root, width=width, height=height)
            canvas.pack()
            canvas.create_image(width / 2, height / 2, image=tk_img)

            self.root.mainloop()




test = comic_image(url_lst)
test.display_image()

