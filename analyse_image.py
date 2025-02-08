import pytesseract
from PIL import Image
import easyocr
import requests
from io import BytesIO

# URL of the image
link = 'https://instagram.falg2-2.fna.fbcdn.net/v/t51.29350-15/472618865_553628964328570_2328748727613046951_n.webp?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE0NDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.falg2-2.fna.fbcdn.net&_nc_cat=110&_nc_oc=Q6cZ2AG9AzjfsI1ZGUn9Gdskxip7JT_31N9ncI-sgFnjFaAc1kxJTYZc7rhzxecIP0wGk2o&_nc_ohc=-L-iC4e3grsQ7kNvgGq_gLN&_nc_gid=e12a5b15f8cf44e497b743015e7a3710&edm=AP4sbd4BAAAA&ccb=7-5&ig_cache_key=MzU0MTg2MjAyNjI0OTMzNzA5NA%3D%3D.3-ccb7-5&oh=00_AYDaHeSVYCVp0ctBr8Pq4wSx-3EY0fQaKuMsha7zfTeeRA&oe=67AD0D58&_nc_sid=7a9f4b'

# Download the image
response = requests.get(link)

# Check if the request was successful
if response.status_code == 200:
    # Open the image using BytesIO
    webp_image = Image.open(BytesIO(response.content))

    # Convert and save as PNG
    webp_image.save('example.png', 'PNG')
    print("WebP image converted to PNG!")

    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])  # Specify languages

    # Extract text from the PNG image
    result = reader.readtext('example.png')
    for detection in result:
        print(detection[1])  # Extracted text
else:
    print(f"Failed to download image. Status code: {response.status_code}")