import requests

if __name__ == '__main__':
    
    baseurl = "https://httpbin.org/post"
    files = {
             "file" : ("sample.jpg", open("sample.jpg", 'rb'))
            }
    data = {
            "name" : "sample.jpg"
            }

    r = requests.post(baseurl
                      , data = data
                      , files = files)
    
    print(r.status_code)
    print(r.content.decode("utf-8"))