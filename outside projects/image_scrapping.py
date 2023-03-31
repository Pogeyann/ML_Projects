import requests
from bs4 import BeautifulSoup
import urllib

search_term = "rebar spalling"

num_images = 10

url = f'https://www.google.com/search?q={search_term}&sxsrf=AJOqlzV2aYT622SoRLTBXzRxhD94xuHmCA:1679386107901&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi4ppvjyOz9AhXncGwGHXhlDtEQ_AUoAXoECAIQAw&biw=1366&bih=636&dpr=1'


response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

img_tags = soup.find_all('img')

urls = []

for img in img_tags:
    try:
        url = img['src']
        urls.append(url)
    except KeyError:
        continue

for i in range(num_images):
    try:
        response = requests.get(urls[i],stream=True)

        path = f'{search_term}{i}.jpg'

        with open(path, 'wb') as f:
            f.write(response.content)

    except:
        continue




# import requests
# from bs4 import BeautifulSoup
# import urllib

# # Define search query
# search_term = "dogs"

# # Define the number of images to collect
# num_images = 1000

# # Define the URL to scrape
# url = f"https://www.google.com/search?q={search_term}&rlz=1C1GCEU_enUS832US832&source=lnms&tbm=isch"

# # Define the user agent (optional)
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# # Make a request to the URL
# response = requests.get(url, headers=headers)

# # Parse the HTML content of the page
# soup = BeautifulSoup(response.content, "html.parser")

# # Find all image tags
# img_tags = soup.find_all("img")

# # Collect image URLs
# urls = []
# for img in img_tags:
#     try:
#         # Get the URL of the image
#         url = img["data-src"]
#         # Append the URL to the list
#         urls.append(url)
#     except KeyError:
#         continue

# # Download images
# for i in range(num_images):
#     try:
#         # Open the URL image, set stream to True, and retrieve the content
#         response = requests.get(urls[i], stream=True)
#         # Set the path and filename to save the image
#         path = f"images/{search_term}{i}.jpg"
#         # Open the file and write the content of the image to the file
#         with open(path, 'wb') as f:
#             f.write(response.content)
#     except:
#         continue

# print(f"{num_images} images of {search_term} have been downloaded to the images folder.")
