import requests as req
from PIL import Image
from io import BytesIO


def download(query: str, page_number: int):
    header = {'Authorization': '563492ad6f917000010000019f787de32d894606bf9f4f70d9dc303f'}
    url = f'https://api.pexels.com/v1/search'
    params = {'query': query, 'per_page': 1}
    page = 1

    while page <= page_number:
        r = req.get(url, headers=header, params=params)
        if r.status_code == 200:
            _r = r.json()
            for item in _r.get('photos'):
                print(item)
        page += 1

def main():
    query = input('query ')
    page_number = int(input('page number '))
    download(query, page_number)


if __name__ == '__main__':
    main()
