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
        root = tk.Tk()
        http = urllib3.PoolManager()
        def __init__(self, arg):
            self.comics = arg

        def on_key_press(self, event):

            self.root.destroy()
            self.root = tk.Tk()
            if ord(event.char) == 63232:
                self.date += datetime.timedelta(days=1)

            if ord(event.char) == 63233:
                self.date -= datetime.timedelta(days=1)

            if ord(event.char) == 63235:
                self.index += 1
                if self.index >= len(self.comics):
                    self.index = 0

            if ord(event.char) == 63234:
                self.index -= 1
                if self.index < 0:
                    self.index = -1

            self.display_image()

        def get_url(self):
            return "http://www.gocomics.com/" + self.comics[self.index] + "/" + self.date.strftime('%Y') + "/" + self.date.strftime('%m') + "/" + self.date.strftime('%d')

        def display_image(self):
            r = self.http.request('GET', self.get_url())
            print(self.get_url())
            strip = str(r.data).find("class=\"strip\" src=\"")
            start_index = strip + len("class=\"strip\" src=\"")

            end_index = 0
            while(str(r.data)[start_index + end_index] != "\""):
                end_index += 1

            image_url = str(r.data)[start_index: start_index + end_index]

            response = requests.get(image_url)
            screen_height = self.root.winfo_screenheight()
            screen_width = self.root.winfo_screenwidth()

            img = Image.open(BytesIO(response.content))
            tk_img = ImageTk.PhotoImage(img)
            width = tk_img.width()
            height = tk_img.height()
            self.root.bind('<KeyPress>', test.on_key_press)

            canvas = tk.Canvas(self.root, width=width, height=height)
            canvas.delete("all")
            canvas.pack()
            canvas.create_image(width / 2, height / 2, image=tk_img)
            canvas.canvasx(0)
            canvas.canvasy(0)

            self.root.mainloop()    




test = comic_image(url_lst)
test.display_image()

