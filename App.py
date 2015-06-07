from requests_toolbelt import MultipartEncoder

import requests

def create_upload():
    return MultipartEncoder({
        'name': 'test',
        'file': ('sample.jpg', open('sample.jpg', 'rb'), 'text/plain'),
        })


if __name__ == '__main__':
    encoder = create_upload()
    r = requests.post('https://httpbin.org/post'
                      , data=encoder
                      , headers={'Content-Type': encoder.content_type})
    print(r.status_code)
    print(r.content.decode("utf-8"))