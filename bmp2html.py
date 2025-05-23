import os
from PIL import Image

def convert_bmp_to_png(directory):
    png_files = []
    for file in os.listdir(directory):
        if file.endswith(".bmp"):
            png_name = file.replace(".bmp", ".png")
            img = Image.open(os.path.join(directory, file))
            img.save(os.path.join(directory, png_name))
            png_files.append(png_name)
    return png_files

def create_html_gallery(png_files, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("<html>\n<head>\n<title>Image Gallery</title>\n")
        f.write("<style>\nbody { background-color: darkblue; color: white; text-align: center; }\n")
        f.write("img { margin: 5px; border: 2px solid white; }\n")
        f.write("</style>\n</head>\n<body>\n")

        for image in png_files:
            f.write(f"<p>{image}</p>\n")
            f.write(f"<img src='{image}' width='150'>\n")

        f.write("</body>\n</html>")

directory = os.getcwd()
png_files = convert_bmp_to_png(directory)
create_html_gallery(png_files, "index.html")

print("Conversion completed. Gallery saved as index.html!")
