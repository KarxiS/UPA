# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# -------------------IMPORTY
import requests

from webscraping.websiteBrowser import websiteBrowser


# ------------------DEFINICIE

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# -----------------MAIN
# Press the green button in the gutter to run the script.

URL = "https://www.rolecosplay.com/catalog/category/view/id/59"

analyzator = websiteBrowser(URL);
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
