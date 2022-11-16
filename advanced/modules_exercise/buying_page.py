from json import load
from PIL import Image, ImageTk
from modules_exercise.helpers import clean_screen
from modules_exercise.canvas import frame


def display_products():
    clean_screen()
    display_stock()


def display_stock():
    with open("db/products_data.json", "r") as stock:
        info = load(stock)

    x = 150
    y = 50

    for item_name, item_info in info.items():
        item_img = ImageTk.PhotoImage(Image.open(item_info["image"]))
        images.append(item_img)

        frame.create_text(x, y, text=item_name, font=("Comic Sans MS", 15))
        frame.create_image(x, y + 100, image=item_img)

images = []