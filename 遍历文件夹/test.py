import os
import hashlib

# 遍历文件夹
def walkFile(file):
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        #遍历所有的文件夹
        for d in dirs:
                print(os.path.join(root, d))
        # 遍历文件
        for f in files:
            print(os.path.join(root, f))
            file_name = os.path.join(root, f)
            with open(file_name, 'rb') as fp:
                data = fp.read()
            file_md5 = hashlib.md5(data).hexdigest()
            print(file_md5)
            file_path = file_name + 'MD5' + '.log'
            line = os.path.split(path)[-1]+file_name.lstrip(path) + ';' + file_md5
            log_file = open(file_path, 'a')
            line = line + '\n'
            log_file.write(line)




if __name__ == '__main__':
    path = "C:/Users/hp/Desktop/test"
    walkFile(path)
