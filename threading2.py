import requests
import time
import concurrent.futures

img_urls = [
    'https://wallpapercave.com/wp/wp2260440.jpg'
]
t1 = time.perf_counter()

#Process
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

#This approach has already been encapsulated
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')