import requests
import json
#from bs4 import BeautifulSoup
import csv


def collect_data():
    total = requests.get('https://api.technodom.kz/katalog/api/v1/products/category/smartfony?city_id=5f5f1e3b4c8a49e692fefd70&limit=1&brands=apple&page=1&sorting=score&price=0').json()['total']
    response_JSON = requests.get(f'https://api.technodom.kz/katalog/api/v1/products/category/smartfony?city_id=5f5f1e3b4c8a49e692fefd70&limit={total}&brands=apple&sorting=score&price=0').json()

    with open('phones.json', 'w') as f:
        json.dump(response_JSON, f, indent=4, ensure_ascii=True)

    with open('phones.csv', 'w', encoding='utf8', newline='') as csvfile:
        fieldnames = ['Name', 'Cost(usd)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in response_JSON['payload']:
            phone_name = i['title'].replace('Смартфон ', '')
            phone_cost = i['price_usd']
            writer.writerow({'Name': phone_name, 'Cost(usd)': phone_cost})


def main():
    collect_data()

if __name__ == '__main__':
    main()
