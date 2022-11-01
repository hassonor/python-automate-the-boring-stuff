import requests

pics_of_fruits = ["apple_juice.jpg", "apple_pressings.jpg", "dumplings.jpg", "lemon_juice.jpg", "bad_fruit.jpg"]

for pic in pics_of_fruits:
    website = requests.get("https://juice-shop.herokuapp.com/assets/public/images/products/" + pic)

    if website.status_code == 200:
        with open(pic, 'wb') as pic_to_download:
            pic_to_download.write(website.content)
