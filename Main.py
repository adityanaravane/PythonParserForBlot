import requests
from PIL import Image
import csv
from io import BytesIO

image_url = 'https://www.santacruzbicycles.com/_next/image?url=https%3A%2F%2Fimages.prismic.io%2Fsantacruzbikesstatic%2FZmtVUpm069VX1u4H_MY25_V10_black_angled_desktop.jpg%3Fauto%3Dformat%2Ccompress&w=2100&q=99'


response = requests.get(image_url)
img = Image.open(BytesIO(response.content)).convert('L')


threshold = 100
width, height = img.size

csv_file = "V10"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([width, height])

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            if img.getpixel((x, y)) < threshold:
                value =0
            else:
                value =1
            writer.writerow([x, y, value])




