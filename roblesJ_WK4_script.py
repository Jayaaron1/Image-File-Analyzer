'''
Jay Robles
9-20-23
CYBV 473
'''

import os
from PIL import Image
from prettytable import PrettyTable

def is_image(file_path):
    try:
        img = Image.open(file_path)
        img.close()
        return True
    except (IOError, OSError):
        return False

def search_for_images(directory_path):
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        return None

    image_files = [file for file in os.listdir(directory_path) if is_image(os.path.join(directory_path, file))]
    return image_files

def generate_report(directory_path, image_files):
    table = PrettyTable(["Image File", "Extension", "Format", "Width", "Height", "Mode"])
    table.align = "l"

    for file in image_files:
        file_path = os.path.join(directory_path, file)
        img = Image.open(file_path)
        extension = os.path.splitext(file)[1]
        format = img.format
        width, height = img.size
        mode = img.mode
        img.close()

        table.add_row([file, extension, format, width, height, mode])

    return table

def main():
    directory_path = input("Enter the directory path to search: ")

    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print("Invalid directory path.")
        return
    image_files = search_for_images(directory_path)

    if image_files is None:
        print("No valid image files found in the directory.")
    else:
        report = generate_report(directory_path, image_files)
        print(report)

if __name__ == "__main__":
    main()
