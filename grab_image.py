__author__ = 'Caleb'
import urllib3
from PIL import Image, ImageTk
import tkinter as tk
import requests
from io import BytesIO

comic_url = "calvinandhobbes"
year_url = "2014"
month_url = "07"
day_url = "01"
url = "http://www.gocomics.com/" + comic_url + "/" + year_url + "/" + month_url + "/" + day_url

http = urllib3.PoolManager()
r = http.request('GET', url)
strip = str(r.data).find("class=\"strip\" src=\"")
width = str(r.data).find("\" width=\"600\" /><sp")
start_index = strip + len("class=\"strip\" src=\"")

image_url = str(r.data)[start_index : width]

response = requests.get(image_url)
img = Image.open(BytesIO(response.content))

root = tk.Tk()
tk_img = ImageTk.PhotoImage(img)
width = tk_img.width()
height = tk_img.height()

canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()
canvas.create_image(width/2, height/2, image=tk_img)

root.mainloop()