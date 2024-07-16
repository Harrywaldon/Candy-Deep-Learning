import requests
from bs4 import BeautifulSoup
import os


def scrape_unsplash_images(query, folder_path, num_images=50):
    url = f"https://unsplash.com/s/photos/{query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    count = 0
    for i, img in enumerate(img_tags):
        img_url = img.get('src')
        if img_url and 'http' in img_url:
            img_data = requests.get(img_url).content
            with open(os.path.join(folder_path, f'{query}_unsplash_{i}.jpg'), 'wb') as handler:
                handler.write(img_data)
                count += 1
                if count >= num_images:
                    break


def scrape_shutterstock_images(query, folder_path, num_images=50):
    url = f"https://www.shutterstock.com/search/{query}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    count = 0
    for i, img in enumerate(img_tags):
        img_url = img.get('src')
        if img_url and 'http' in img_url:
            img_data = requests.get(img_url).content
            with open(os.path.join(folder_path, f'{query}_shutterstock_{i}.jpg'), 'wb') as handler:
                handler.write(img_data)
                count += 1
                if count >= num_images:
                    break


def scrape_getty_images(query, folder_path, num_images=50):
    url = f"https://www.gettyimages.com/photos/{query}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    count = 0
    for i, img in enumerate(img_tags):
        img_url = img.get('src')
        if img_url and 'http' in img_url:
            img_data = requests.get(img_url).content
            with open(os.path.join(folder_path, f'{query}_getty_{i}.jpg'), 'wb') as handler:
                handler.write(img_data)
                count += 1
                if count >= num_images:
                    break

def scrape_google_images(query, folder_path, num_images=100):
    url = f"https://www.google.com/search?hl=en&q={query}&tbm=isch"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    count = 0
    for i, img in enumerate(img_tags):
        img_url = img.get('src')
        if img_url and 'http' in img_url:
            img_data = requests.get(img_url).content
            with open(os.path.join(folder_path, f'{query}_bing_{i}.jpg'), 'wb') as handler:
                handler.write(img_data)
                count += 1
                if count >= num_images:
                    break


def scrape_images_from_multiple_sources(query, folder_path, num_images_per_source=50):
    # Scrape from Unsplash
    scrape_unsplash_images(query, folder_path, num_images=num_images_per_source)
    # Scrape from Pixabay
    scrape_shutterstock_images(query, folder_path, num_images=num_images_per_source)
    # Scrape from getty images
    scrape_getty_images(query, folder_path, num_images=num_images_per_source)
    # Scrape from bing
    scrape_google_images(query, folder_path, num_images=num_images_per_source)


candy_types = ["licorice candy"]
for candy in candy_types:
    scrape_images_from_multiple_sources(candy, f'./candy_images/{candy}', num_images_per_source=50)