
from aip import AipOcr

APP_ID = '23552805'
API_KEY = 'rj3qLOTF64aj0hZMuvGBx4uu'
SECRET_KEY = 'GFi5p5vBKGzqjlb3FRNFLXfcUEKKUoEj'

client = AipOcr(appId=APP_ID,apiKey=APP_ID,secretKey=SECRET_KEY)

def get_file_content(filepath):
    with open(filepath,'rb') as f:
        return f.read()
def get_imag_content(img):
    image_content = ''
    content = client.basicAccurate(image=img)
    print(content)
    for item in content['words_result']:
        print(item['words'])
        image_content += item['words']
    print(image_content)
    with open('demo.txt','w',encoding='utf-8') as f:
        f.write(image_content)

if __name__ == '__main__':
    img = get_file_content('screen.jpg')
    get_imag_content(img)