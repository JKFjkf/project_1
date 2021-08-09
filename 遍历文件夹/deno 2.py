import os

path = "C:/Users/hp/Desktop/test"
for root, dirs, files in os.walk(path):
    for d in dirs:
        print(os.path.join(root, d))
    # 遍历文件
    for f in files:
        #print(os.path.join(root, f))
        #print(f)
        file_name = os.path.join(root, f)
        print(file_name)
        print(os.path.basename(file_name))
        #print(os.path.split(path)[-1])

        #print(file_name.lstrip(path))
        #print(os.path.split(path)[-1] + file_name.lstrip(path))
        b=os.path.split(path)[-1] + file_name.lstrip(path)
        #print(os.path.dirname(b))
        c= os.path.dirname(b)
        #print(c.replace('\\','/'))