import keyboard
import time
from PIL import ImageGrab
from aip import AipOcr

APP_ID ='23552805'
API_KEY ='rj3qLOTF64aj0hZMuvGBx4uu'
SECRET_KEY ='GFi5p5vBKGzqjlb3FRNFLXfcUEKKUoEj'

client = AipOcr(appId=APP_ID,apiKey=API_KEY,secretKey=SECRET_KEY)

#截取图片
def screen():
    print('开始截图：')
    keyboard.wait('alt+a')
    keyboard.wait('enter')
    time.sleep(0.5)
    image = ImageGrab.grabclipboard()#调用grabclipboard方法获取到剪切板上图片
    image.save('screen.jpg')
    print('图片保存完成！')
#读取图片
def get_file_content(filepath):
    with open(filepath,'rb') as f:
        return f.read()
def get_imag_content(img):
    image_content = ''
    content = client.basicAccurate(image=img)
    #print(content)
    for words in content['words_result']:
        #print(words)
        image_content += words['words']
    print(image_content)
    with open('demo.txt','w',encoding='utf-8') as f:
        f.write(image_content)



if __name__ == '__main__':
    screen()
    img = get_file_content('screen.jpg')
    get_imag_content(img)

input()