import requests
from bs4 import BeautifulSoup

base_urls = ['https://us.shop.gymshark.com/products/gymshark-apex-5-perform-shorts-black-aw22',
             'https://us.shop.gymshark.com/products/gymshark-apex-5-perform-shorts-silhouette-grey-aw22',
             'https://us.shop.gymshark.com/products/gymshark-apex-5-perform-shorts-pepper-red-aw22',
             'https://us.shop.gymshark.com/products/gymshark-apex-5-perform-shorts-cherry-brown-aw22']

for url in base_urls:
    session = requests.Session()
    params = {'page': 1}
    try:
        response = session.get(url, params=params)
        soup = BeautifulSoup(response.content, 'html.parser')
        product_target = soup.find(
            'button', {'data-locator-id': 'pdp-size-m-select'})
        print("\nChecking:  ", url)

        if product_target:
            class_attribute = product_target.get('class')
            if 'size_size--out-of-stock__hBcxj' in class_attribute:
                print("Product Out of Stock.")
            else:
                print("In Stock: ", url)
        else:
            print("Button with data-locator-id='pdp-size-m-select' not found.")

    except Exception as e:
        print("An error ocurred: ", e)

print("\nScraping completed.\n")
